"""Simple scoring helpers for the benchmark collection."""

from collections import Counter


def token_f1(prediction: str, reference: str) -> float:
    pred_tokens = Counter(prediction.lower().split())
    ref_tokens = Counter(reference.lower().split())
    overlap = sum((pred_tokens & ref_tokens).values())
    if not pred_tokens or not ref_tokens:
        return 0.0
    precision = overlap / sum(pred_tokens.values())
    recall = overlap / sum(ref_tokens.values())
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)
