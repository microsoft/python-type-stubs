from typing_extensions import assert_type

from numpy import ndarray
from sklearn.tree._splitter import Splitter
from sklearn.tree._tree import BestFirstTreeBuilder, DepthFirstTreeBuilder
from sklearn.utils._seq_dataset import ArrayDataset32, ArrayDataset64, CSRDataset32, CSRDataset64


class DatasetSubclass(ArrayDataset64): ...


def check_dataset_constructors(X: ndarray, y: ndarray, weights: ndarray, indptr: ndarray, indices: ndarray) -> None:
    assert_type(ArrayDataset32(X, y, weights), ArrayDataset32)
    assert_type(ArrayDataset64(X, y, weights, seed=2), ArrayDataset64)
    assert_type(CSRDataset32(X, indptr, indices, y, weights), CSRDataset32)
    assert_type(CSRDataset64(X, indptr, indices, y, weights, seed=2), CSRDataset64)
    assert_type(DatasetSubclass(X, y, weights), DatasetSubclass)


def check_tree_builder_constructors(splitter: Splitter) -> None:
    assert_type(DepthFirstTreeBuilder(splitter, 2, 1, 0.0, 10, 0.0), DepthFirstTreeBuilder)
    assert_type(BestFirstTreeBuilder(splitter, 2, 1, 0.0, 10, 20, 0.0), BestFirstTreeBuilder)
