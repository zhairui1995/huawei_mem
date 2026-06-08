"""Per-application Markov baseline for next-operation prediction."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Iterable


class OpMarkovModel:
    def __init__(self, order: int = 1, op_vocab: dict[str, dict[str, int]] | None = None) -> None:
        if order not in (1, 2, 3, 4):
            raise ValueError("order must be between 1 and 4")
        self.order = order
        self.op_vocab = op_vocab or {}
        self.transitions: dict[str, dict[tuple[int, ...], Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
        self.global_counts: dict[str, Counter[int]] = defaultdict(Counter)

    def _pad_id(self, app: str) -> int | None:
        vocab = self.op_vocab.get(app, {})
        return vocab.get("<PAD>")

    def _unk_id(self, app: str) -> int | None:
        vocab = self.op_vocab.get(app, {})
        return vocab.get("<UNK>")

    def fit(self, samples: Iterable[dict]) -> None:
        for sample in samples:
            app = sample["app"]
            pad_id = self._pad_id(app)
            history = [int(op_id) for op_id in sample.get("history_ops", []) if int(op_id) != pad_id]
            label = int(sample["label_next_op"])
            if label == pad_id:
                continue

            for op_id in history:
                self.global_counts[app][op_id] += 1
            self.global_counts[app][label] += 1

            max_context_order = min(self.order, len(history))
            for idx in range(1, len(history)):
                for context_order in range(1, min(self.order, idx) + 1):
                    context = tuple(history[idx - context_order : idx])
                    self.transitions[app][context][history[idx]] += 1

            for context_order in range(1, max_context_order + 1):
                context = tuple(history[-context_order:])
                self.transitions[app][context][label] += 1

    def _rank(self, app: str, counts: Counter[int], k: int) -> list[int]:
        pad_id = self._pad_id(app)
        unk_id = self._unk_id(app)
        candidates = [(op_id, count) for op_id, count in counts.items() if op_id != pad_id]
        non_unk = [(op_id, count) for op_id, count in candidates if op_id != unk_id]
        if non_unk:
            candidates = non_unk
        return [
            op_id
            for op_id, _ in sorted(candidates, key=lambda item: (-item[1], item[0] == unk_id, item[0]))[:k]
        ]

    def predict_topk(self, app: str, history_ops: Iterable[int], k: int = 5) -> list[int]:
        history = [int(op_id) for op_id in history_ops if int(op_id) != self._pad_id(app)]
        counts: Counter[int] | None = None
        for context_order in range(min(self.order, len(history)), 0, -1):
            context = tuple(history[-context_order:])
            counts = self.transitions.get(app, {}).get(context)
            if counts:
                break
        if not counts:
            counts = self.global_counts.get(app, Counter())
        return self._rank(app, counts, k)
