#!/usr/bin/env python3
"""Evaluate inference latency for in-app operation prediction models."""

from __future__ import annotations

import argparse
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.op_gam import OpGamModel
from src.models.op_markov import OpMarkovModel
from src.models.op_mogp import OpMogpModel
from src.models.op_parametric import OpParametricModel
from src.models.op_quantile import OpQuantileModel
from src.models.op_scnn import OpScnnModel
from src.utils.io_utils import load_json, load_pickle, save_csv


MODEL_CHOICES = ["markov", "gam", "mogp", "parametric", "quantile", "scnn"]


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    if len(values) == 1:
        return values[0]
    ordered = sorted(values)
    position = (len(ordered) - 1) * pct
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def build_model(name: str, op_vocab: dict, args: argparse.Namespace):
    if name == "markov":
        return OpMarkovModel(order=args.order, op_vocab=op_vocab)
    if name == "gam":
        return OpGamModel(op_vocab=op_vocab, smoothing=args.smoothing)
    if name == "mogp":
        return OpMogpModel(
            op_vocab=op_vocab,
            length_scale=args.length_scale,
            correlation_weight=args.correlation_weight,
        )
    if name == "parametric":
        return OpParametricModel(op_vocab=op_vocab, epochs=args.epochs, learning_rate=args.learning_rate)
    if name == "quantile":
        return OpQuantileModel(
            op_vocab=op_vocab,
            hidden_size=args.hidden_size,
            epochs=args.epochs,
            learning_rate=args.quantile_learning_rate,
        )
    if name == "scnn":
        return OpScnnModel(op_vocab=op_vocab, epochs=args.epochs, learning_rate=args.learning_rate)
    raise ValueError(f"unsupported model: {name}")


def evaluate_latency(model, model_name: str, test_samples: list[dict], k_values: list[int], warmup: int) -> list[dict]:
    max_k = max(k_values)
    warmup_samples = test_samples[: min(warmup, len(test_samples))]
    for sample in warmup_samples:
        model.predict_topk(sample["app"], sample.get("history_ops", []), k=max_k)

    durations_ms: list[float] = []
    for sample in test_samples:
        start = time.perf_counter()
        model.predict_topk(sample["app"], sample.get("history_ops", []), k=max_k)
        durations_ms.append((time.perf_counter() - start) * 1000.0)

    total_ms = sum(durations_ms)
    throughput = len(durations_ms) / (total_ms / 1000.0) if total_ms > 0.0 else 0.0
    rows = []
    for k in k_values:
        rows.append(
            {
                "model": model_name,
                "k": k,
                "avg_latency_ms": statistics.fmean(durations_ms) if durations_ms else 0.0,
                "p50_latency_ms": percentile(durations_ms, 0.50),
                "p95_latency_ms": percentile(durations_ms, 0.95),
                "p99_latency_ms": percentile(durations_ms, 0.99),
                "throughput_samples_per_sec": throughput,
                "num_samples": len(durations_ms),
                "warmup_samples": len(warmup_samples),
            }
        )
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate operation model inference latency.")
    parser.add_argument("--train", default="data/processed/train_op.pkl")
    parser.add_argument("--test", default="data/processed/test_op.pkl")
    parser.add_argument("--op-vocab", default="data/vocab/op_vocab.json")
    parser.add_argument("--models", nargs="+", choices=MODEL_CHOICES, default=MODEL_CHOICES)
    parser.add_argument("--top-k", nargs="+", type=int, default=[1, 3, 5])
    parser.add_argument("--warmup", type=int, default=100)
    parser.add_argument("--output", default="outputs/results/op_latency_results.csv")

    parser.add_argument("--order", type=int, choices=[1, 2, 3, 4], default=4)
    parser.add_argument("--smoothing", type=float, default=1.0)
    parser.add_argument("--length-scale", type=float, default=2.0)
    parser.add_argument("--correlation-weight", type=float, default=0.35)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--learning-rate", type=float, default=0.1)
    parser.add_argument("--quantile-learning-rate", type=float, default=0.05)
    parser.add_argument("--hidden-size", type=int, default=512)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    train_samples = load_pickle(args.train)
    test_samples = load_pickle(args.test)
    if not train_samples or not test_samples:
        raise ValueError("train/test samples must be non-empty")

    op_vocab = load_json(args.op_vocab)
    rows: list[dict] = []
    for model_name in args.models:
        model = build_model(model_name, op_vocab, args)
        train_start = time.perf_counter()
        model.fit(train_samples)
        train_time_ms = (time.perf_counter() - train_start) * 1000.0
        model_rows = evaluate_latency(model, model_name, test_samples, args.top_k, args.warmup)
        for row in model_rows:
            row["train_time_ms"] = train_time_ms
        rows.extend(model_rows)
        print(f"{model_name}: train_time_ms={train_time_ms:.3f}")

    fieldnames = [
        "model",
        "k",
        "avg_latency_ms",
        "p50_latency_ms",
        "p95_latency_ms",
        "p99_latency_ms",
        "throughput_samples_per_sec",
        "num_samples",
        "warmup_samples",
        "train_time_ms",
    ]
    save_csv(rows, args.output, fieldnames)
    print(f"saved: {args.output}")


if __name__ == "__main__":
    main()
