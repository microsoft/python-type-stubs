from .histogram import HistogramBuilder as HistogramBuilder
from .utils import sum_parallel as sum_parallel
from .predictor import TreePredictor
from ..._typing import Int, ArrayLike, Float, MatrixLike
from timeit import default_timer as time
from numpy import ndarray
from .splitting import Splitter as Splitter, SplitInfo as SplitInfo
from heapq import heappush as heappush, heappop as heappop
from .common import (
    PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE,
    X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE,
    Y_DTYPE as Y_DTYPE,
    MonotonicConstraint as MonotonicConstraint,
)
from ._bitset import (
    set_raw_bitset_from_binned_bitset as set_raw_bitset_from_binned_bitset,
)
import numpy as np
import numbers


EPS = ...  # to avoid zero division errors


class TreeNode:

    split_info: SplitInfo | None = ...
    left_child: TreeNode | None = ...
    right_child: TreeNode | None = ...
    histograms = ...

    # start and stop indices of the node in the splitter.partition
    # array. Concretely,
    # self.sample_indices = view(self.splitter.partition[start:stop])
    # Please see the comments about splitter.partition and
    # splitter.split_indices for more info about this design.
    # These 2 attributes are only used in _update_raw_prediction, because we
    # need to iterate over the leaves and I don't know how to efficiently
    # store the sample_indices views because they're all of different sizes.
    partition_start: int = ...
    partition_stop: int = ...

    def __init__(
        self,
        depth: Int,
        sample_indices: ArrayLike,
        sum_gradients: Float,
        sum_hessians: Float,
        value=None,
    ) -> None:
        ...

    def set_children_bounds(self, lower: float, upper: float) -> None:
        ...

    def __lt__(self, other_node: TreeNode) -> bool:
        ...


class TreeGrower:
    def __init__(
        self,
        X_binned: MatrixLike,
        gradients: ArrayLike,
        hessians: ArrayLike,
        max_leaf_nodes: None | Int = None,
        max_depth: None | Int = None,
        min_samples_leaf: Int = 20,
        min_gain_to_split: Float = 0.0,
        n_bins: Int = 256,
        n_bins_non_missing: None | ArrayLike = None,
        has_missing_values: ndarray | bool | ArrayLike = False,
        is_categorical: None | ArrayLike = None,
        monotonic_cst: None | ArrayLike = None,
        interaction_cst: None | list[set[int]] = None,
        l2_regularization: Float = 0.0,
        min_hessian_to_split: Float = 1e-3,
        shrinkage: Float = 1.0,
        n_threads: None | Int = None,
    ) -> None:
        ...

    def grow(self) -> None:
        ...

    def split_next(self) -> tuple[TreeNode, TreeNode]:
        ...

    def make_predictor(self, binning_thresholds: ArrayLike) -> TreePredictor:
        ...
