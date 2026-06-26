"""Parametric linear scorer for in-app next-operation prediction."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Iterable


class OpParametricModel:
    """A lightweight one-vs-best linear model over operation candidates.

    The model is intentionally dependency-free so it can be used as an
    experiment group alongside the Markov baseline in the current pipeline.
    """

    def __init__(
        self,
        op_vocab: dict[str, dict[str, int]] | None = None,
        epochs: int = 5,
        learning_rate: float = 0.1,
    ) -> None:
        if epochs <= 0:
            raise ValueError("epochs must be positive")
        if learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        self.op_vocab = op_vocab or {}
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.weights: dict[str, Counter[str]] = defaultdict(Counter)
        self.label_counts: dict[str, Counter[int]] = defaultdict(Counter)
        self.candidates: dict[str, list[int]] = {}
        self._prediction_cache: dict[tuple[str, tuple[int, ...]], list[int]] = {}
        self._cache_enabled = False

    def _pad_id(self, app: str) -> int | None:
        value = self.op_vocab.get(app, {}).get("<PAD>")
        return int(value) if value is not None else None

    def _unk_id(self, app: str) -> int | None:
        value = self.op_vocab.get(app, {}).get("<UNK>")
        return int(value) if value is not None else None

    def _candidate_ids(self, app: str) -> list[int]:
        vocab = self.op_vocab.get(app, {})
        pad_id = self._pad_id(app)
        ids = {int(op_id) for op_id in vocab.values() if int(op_id) != pad_id}
        ids.update(self.label_counts.get(app, {}).keys())
        return sorted(ids)

    def _history(self, app: str, history_ops: Iterable[int]) -> list[int]:
        pad_id = self._pad_id(app)
        return [int(op_id) for op_id in history_ops if int(op_id) != pad_id]

    def _features(self, app: str, history_ops: Iterable[int], candidate: int) -> list[tuple[str, float]]:
        history = self._history(app, history_ops)
        feats: list[tuple[str, float]] = [
            ("bias", 1.0),
            (f"cand={candidate}", 1.0),
            (f"hist_len={min(len(history), 8)}", 1.0),
        ]
        if not history:
            return feats

        counts = Counter(history)
        feats.append(("cand_seen_in_history", 1.0 if candidate in counts else 0.0))
        feats.append(("cand_history_count", float(counts.get(candidate, 0))))

        for offset, op_id in enumerate(reversed(history[-4:]), start=1):
            feats.append((f"recent_{offset}={op_id}", 1.0))
            feats.append((f"recent_{offset}={op_id}|cand={candidate}", 1.0))
            if op_id == candidate:
                feats.append((f"recent_{offset}_same_candidate", 1.0))

        for order in range(1, min(4, len(history)) + 1):
            context = ",".join(str(op_id) for op_id in history[-order:])
            feats.append((f"context_{order}={context}|cand={candidate}", 1.0))
        return feats

    def _score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        weights = self.weights[app]
        return sum(weights[name] * value for name, value in self._features(app, history_ops, candidate))

    def _ranked_candidates(self, app: str, history_ops: Iterable[int]) -> list[int]:
        history = tuple(self._history(app, history_ops))
        cache_key = (app, history)
        if self._cache_enabled and cache_key in self._prediction_cache:
            return list(self._prediction_cache[cache_key])

        candidate_ids = self.candidates.get(app) or self._candidate_ids(app)
        ranked = [
            op_id
            for op_id, _ in sorted(
                ((op_id, self._score(app, history, op_id)) for op_id in candidate_ids),
                key=lambda item: (-item[1], item[0]),
            )
        ]
        if self._cache_enabled:
            self._prediction_cache[cache_key] = ranked
        return list(ranked)

    def _update(self, app: str, history_ops: Iterable[int], label: int, pred: int) -> None:
        weights = self.weights[app]
        for name, value in self._features(app, history_ops, label):
            weights[name] += self.learning_rate * value
        for name, value in self._features(app, history_ops, pred):
            weights[name] -= self.learning_rate * value

    def fit(self, samples: Iterable[dict]) -> None:
        self._cache_enabled = False
        self._prediction_cache.clear()
        rows = list(samples)
        for sample in rows:
            app = sample["app"]
            label = int(sample["label_next_op"])
            if label != self._pad_id(app):
                self.label_counts[app][label] += 1

        self.candidates = {app: self._candidate_ids(app) for app in self.label_counts}

        for _ in range(self.epochs):
            for sample in rows:
                app = sample["app"]
                label = int(sample["label_next_op"])
                if label == self._pad_id(app):
                    continue
                ranked = self._ranked_candidates(app, sample.get("history_ops", []))
                if not ranked:
                    continue
                pred = ranked[0]
                if pred != label:
                    self._update(app, sample.get("history_ops", []), label, pred)
        self._cache_enabled = True
        self._prediction_cache.clear()

    def predict_topk(self, app: str, history_ops: Iterable[int], k: int = 5) -> list[int]:
        unk_id = self._unk_id(app)
        ranked = self._ranked_candidates(app, history_ops)
        non_unk = [op_id for op_id in ranked if op_id != unk_id]
        if non_unk:
            ranked = non_unk
        return ranked[:k]
