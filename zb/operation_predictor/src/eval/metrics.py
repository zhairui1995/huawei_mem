"""Evaluation metrics for application and operation prediction.

该模块包含常用评估指标的实用实现：命中（hit@k）、召回、精确度、MRR
以及 top-k 准确率。输入标签可以是：
- 集合形式的标签 id（例如 {1, 3}）
- 列表/可迭代的 id（例如 [1, 3]）
- 多热编码形式的列表（例如 [0, 1, 0, 1]）

函数会将这些输入规范化为一组整数 id 以便计算。
注释以中文提供，便于代码阅读与维护。
"""

from __future__ import annotations

from collections.abc import Iterable


def _label_set(labels: Iterable[int] | set[int]) -> set[int]:
    """Normalize various label formats to a set of integer ids.

    支持的输入形式：
    - 已是 `set` 的情况：直接返回其副本
    - 可迭代的 id 列表：如 [1, 3] -> {1, 3}
    - 多热（multi-hot）向量：如 [0,1,0,1] -> {1, 3}

    返回一个由整数 id 组成的 `set`（若输入为空则返回空集）。
    """
    # 如果已经是集合，直接返回其副本以保证返回值可变且不修改原对象
    if isinstance(labels, set):
        return set(labels)

    # 将可迭代对象转换为列表以便多次遍历和长度判断
    values = list(labels)
    if not values:
        return set()

    # 判断是否为多热向量：所有元素都属于 {0,1,False,True} 且长度大于2
    # （长度 > 2 用以避免将短的二分类向量误判为 multi-hot）
    is_multihot = all(v in (0, 1, False, True) for v in values) and len(values) > 2
    if is_multihot:
        # 返回所有为真的索引位置作为标签 id
        return {idx for idx, value in enumerate(values) if value}

    # 否则，假设 values 是可转换为整数的 id 列表
    return {int(v) for v in values}


def hit_at_k(pred_topk: Iterable[int], labels: Iterable[int] | set[int]) -> int:
    """Hit@K: 如果预测的 top-k 中包含任一真实标签则返回 1，否则返回 0。

    - `pred_topk`: 可迭代的预测 id 列表（长度通常为 k）
    - `labels`: 真实标签（支持多种格式，参见 `_label_set`）
    """
    label_ids = _label_set(labels)
    # 如果没有真实标签，定义命中为 0（不可计算）
    return int(bool(set(pred_topk) & label_ids)) if label_ids else 0


def recall_at_k(pred_topk: Iterable[int], labels: Iterable[int] | set[int]) -> float:
    """Recall@K: 预测 top-k 中命中的真实标签数 / 真实标签总数。

    返回值在 0.0 到 1.0 之间；当没有真实标签时返回 0.0。
    """
    label_ids = _label_set(labels)
    if not label_ids:
        return 0.0
    return len(set(pred_topk) & label_ids) / len(label_ids)


def precision_at_k(pred_topk: Iterable[int], labels: Iterable[int] | set[int]) -> float:
    """Precision@K: 预测 top-k 中命中的真实标签数 / k。

    当 `pred_topk` 为空时返回 0.0。
    """
    preds = list(pred_topk)
    if not preds:
        return 0.0
    return len(set(preds) & _label_set(labels)) / len(preds)


def mrr(pred_ranked_list: Iterable[int], labels: Iterable[int] | set[int]) -> float:
    """Mean Reciprocal Rank (MRR) for a single query.

    对于给定的按概率/得分排序的预测列表，返回第一个命中真实标签的倒数排名：
    例如第一个命中位于第 3 位，则返回 1/3。若无命中或没有真实标签返回 0.0。
    """
    label_ids = _label_set(labels)
    if not label_ids:
        return 0.0
    for rank, pred in enumerate(pred_ranked_list, start=1):
        if pred in label_ids:
            return 1.0 / rank
    return 0.0


def topk_accuracy(pred_topk: Iterable[int], label: int) -> int:
    """Top-K accuracy for a single-label case.

    如果真实单标签 `label` 出现在预测的 top-k 中返回 1，否则返回 0。
    """
    return int(label in set(pred_topk))


def _self_test() -> None:
    # 简单的自检用例，覆盖各函数的典型输入形式
    assert hit_at_k([1, 3], [0, 1, 0, 0]) == 1
    assert hit_at_k([2, 3], {1}) == 0
    assert recall_at_k([1, 2], {1, 3}) == 0.5
    assert precision_at_k([1, 2], {1, 3}) == 0.5
    assert mrr([4, 2, 1], {1}) == 1 / 3
    assert topk_accuracy([4, 2, 1], 2) == 1
    print("metrics self-test passed")


if __name__ == "__main__":
    _self_test()
