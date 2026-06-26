"""Generalized additive scorer for in-app next-operation prediction."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import log
from typing import Iterable


class OpGamModel:
    """A dependency-free GAM-style additive scorer.

    For each application, the model estimates independent additive components
    from training counts: candidate prior, recent-position effects, repeat
    effects, and simple time effects. Candidate scores are the sum of those
    learned components.
    """

    def __init__(
        self,
        op_vocab: dict[str, dict[str, int]] | None = None,
        smoothing: float = 1.0,
    ) -> None:
        if smoothing <= 0:
            raise ValueError("smoothing must be positive")
        self.op_vocab = op_vocab or {}
        self.smoothing = smoothing
        self.label_counts: dict[str, Counter[int]] = defaultdict(Counter)
        self.components: dict[str, Counter[str]] = defaultdict(Counter)
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

    def _feature_keys(self, app: str, history_ops: Iterable[int], candidate: int) -> list[str]:
        history = self._history(app, history_ops)
        keys = [f"prior|cand={candidate}", f"hist_len={min(len(history), 8)}|cand={candidate}"]
        if not history:
            return keys

        counts = Counter(history)
        if candidate in counts:
            keys.append(f"repeat_count={min(counts[candidate], 4)}|cand={candidate}")

        for offset, op_id in enumerate(reversed(history[-4:]), start=1):
            keys.append(f"recent_{offset}={op_id}|cand={candidate}")
            if op_id == candidate:
                keys.append(f"recent_{offset}_repeat|cand={candidate}")

        for order in range(1, min(4, len(history)) + 1):
            context = ",".join(str(op_id) for op_id in history[-order:])
            keys.append(f"context_{order}={context}|cand={candidate}")
        return keys

    @staticmethod
    def _add_log_effect(
        effects: Counter[str],
        positives: Counter[str],
        totals: Counter[str],
        labels: int,
        smoothing: float,
    ) -> None:
        for key, total in totals.items():
            pos = positives.get(key, 0)
            effects[key] = log((pos + smoothing) / (total + smoothing * labels))

    def fit(self, samples: Iterable[dict]) -> None:
        self._cache_enabled = False
        self._prediction_cache.clear()
        rows = list(samples)
        by_app_rows: dict[str, list[dict]] = defaultdict(list)
        for sample in rows:
            app = sample["app"]
            label = int(sample["label_next_op"])
            if label == self._pad_id(app):
                continue
            self.label_counts[app][label] += 1
            by_app_rows[app].append(sample)

        self.candidates = {app: self._candidate_ids(app) for app in self.label_counts}

        for app, app_rows in by_app_rows.items():
            candidates = self.candidates.get(app, [])
            if not candidates:
                continue

            positives: Counter[str] = Counter()
            totals: Counter[str] = Counter()
            for sample in app_rows:
                label = int(sample["label_next_op"])
                history = sample.get("history_ops", [])
                for candidate in candidates:
                    for key in self._feature_keys(app, history, candidate):
                        totals[key] += 1
                        if candidate == label:
                            positives[key] += 1

            self._add_log_effect(
                self.components[app],
                positives,
                totals,
                labels=max(len(candidates), 1),
                smoothing=self.smoothing,
            )
        self._cache_enabled = True
        self._prediction_cache.clear()

    def _score(self, app: str, history_ops: Iterable[int], candidate: int) -> float:
        effects = self.components[app]
        return sum(effects.get(key, 0.0) for key in self._feature_keys(app, history_ops, candidate))

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
