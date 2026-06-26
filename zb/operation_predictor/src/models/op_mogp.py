"""Multi-output Gaussian-process-style scorer for operation prediction."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import exp, sqrt
from typing import Iterable


class OpMogpModel:
    """A dependency-free MOGP-style experiment group.

    Each operation candidate is treated as one output. Training samples are
    summarized as prototype contexts per output, and prediction combines an RBF
    context similarity with output co-occurrence correlations.
    """

    def __init__(
        self,
        op_vocab: dict[str, dict[str, int]] | None = None,
        length_scale: float = 2.0,
        correlation_weight: float = 0.35,
    ) -> None:
        if length_scale <= 0:
            raise ValueError("length_scale must be positive")
        if correlation_weight < 0:
            raise ValueError("correlation_weight must be non-negative")
        self.op_vocab = op_vocab or {}
        self.length_scale = length_scale
        self.correlation_weight = correlation_weight
        self.label_counts: dict[str, Counter[int]] = defaultdict(Counter)
        self.context_sums: dict[str, dict[int, list[float]]] = defaultdict(dict)
        self.context_counts: dict[str, Counter[int]] = defaultdict(Counter)
        self.ngram_counts: dict[str, dict[tuple[int, ...], Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
        self.co_counts: dict[str, dict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
        self.candidates: dict[str, list[int]] = {}
        self._prediction_cache: dict[tuple[str, tuple[int, ...]], list[int]] = {}
        self._cache_enabled = False

    def _pad_id(self, app: str) -> int | None:
        value = self.op_vocab.get(app, {}).get("<PAD>")
        return int(value) if value is not None else None

    def _unk_id(self, app: str) -> int | None:
        value = self.op_vocab.get(app, {}).get("<UNK>")
        return int(value) if value is not None else None

    def _history(self, app: str, history_ops: Iterable[int]) -> list[int]:
        pad_id = self._pad_id(app)
        return [int(op_id) for op_id in history_ops if int(op_id) != pad_id]

    def _candidate_ids(self, app: str) -> list[int]:
        vocab = self.op_vocab.get(app, {})
        pad_id = self._pad_id(app)
        ids = {int(op_id) for op_id in vocab.values() if int(op_id) != pad_id}
        ids.update(self.label_counts.get(app, {}).keys())
        return sorted(ids)

    def _vector(self, app: str, history_ops: Iterable[int]) -> list[float]:
        history = self._history(app, history_ops)
        if not history:
            return [0.0, 0.0, 0.0, 0.0]

        recent = history[-4:]
        counts = Counter(recent)
        last = float(recent[-1])
        prev = float(recent[-2]) if len(recent) >= 2 else 0.0
        repeat_ratio = max(counts.values()) / len(recent)
        diversity = len(counts) / len(recent)
        return [last, prev, repeat_ratio, diversity]

    @staticmethod
    def _add_to_sum(acc: list[float], values: list[float]) -> None:
        for idx, value in enumerate(values):
            acc[idx] += value

    @staticmethod
    def _mean(values: list[float], count: int) -> list[float]:
        return [value / count for value in values]

    @staticmethod
    def _distance_sq(left: list[float], right: list[float]) -> float:
        return sum((a - b) * (a - b) for a, b in zip(left, right))

    def _kernel(self, left: list[float], right: list[float]) -> float:
        return exp(-self._distance_sq(left, right) / (2.0 * self.length_scale * self.length_scale))

    def fit(self, samples: Iterable[dict]) -> None:
        self._cache_enabled = False
        self._prediction_cache.clear()
        rows = list(samples)
        for sample in rows:
            app = sample["app"]
            label = int(sample["label_next_op"])
            if label == self._pad_id(app):
                continue

            vector = self._vector(app, sample.get("history_ops", []))
            self.label_counts[app][label] += 1
            self.context_counts[app][label] += 1
            if label not in self.context_sums[app]:
                self.context_sums[app][label] = [0.0 for _ in vector]
            self._add_to_sum(self.context_sums[app][label], vector)

            history = self._history(app, sample.get("history_ops", []))
            for order in range(1, min(4, len(history)) + 1):
                self.ngram_counts[app][tuple(history[-order:])][label] += 1

            for op_id in set(history):
                self.co_counts[app][op_id][label] += 1

        self.candidates = {app: self._candidate_ids(app) for app in self.label_counts}
        self._cache_enabled = True
        self._prediction_cache.clear()

    def _prototype_score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        count = self.context_counts.get(app, {}).get(candidate, 0)
        if not count:
            return 0.0
        vector = self._vector(app, history_ops)
        mean = self._mean(self.context_sums[app][candidate], count)
        prior = sqrt(self.label_counts[app][candidate])
        return self._kernel(vector, mean) * prior

    def _correlation_score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        history = self._history(app, history_ops)
        if not history:
            return 0.0
        score = 0.0
        for offset, op_id in enumerate(reversed(history[-4:]), start=1):
            score += self.co_counts[app].get(op_id, {}).get(candidate, 0) / offset
        return self.correlation_weight * score

    def _ngram_score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        history = self._history(app, history_ops)
        for order in range(min(4, len(history)), 0, -1):
            counts = self.ngram_counts.get(app, {}).get(tuple(history[-order:]))
            if counts:
                total = sum(counts.values())
                return 100.0 * counts.get(candidate, 0) / total
        return 0.0

    def _score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        return (
            self._ngram_score(app, history_ops, candidate)
            + self._prototype_score(app, history_ops, candidate)
            + self._correlation_score(app, history_ops, candidate)
        )

    def predict_topk(self, app: str, history_ops: Iterable[int], k: int = 5) -> list[int]:
        history = tuple(self._history(app, history_ops))
        cache_key = (app, history)
        if self._cache_enabled and cache_key in self._prediction_cache:
            return self._prediction_cache[cache_key][:k]

        unk_id = self._unk_id(app)
        candidates = self.candidates.get(app) or self._candidate_ids(app)
        ranked = [
            op_id
            for op_id, _ in sorted(
                ((op_id, self._score(app, history, op_id)) for op_id in candidates),
                key=lambda item: (-item[1], item[0]),
            )
        ]
        non_unk = [op_id for op_id in ranked if op_id != unk_id]
        if non_unk:
            ranked = non_unk
        if self._cache_enabled:
            self._prediction_cache[cache_key] = ranked
        return ranked[:k]
