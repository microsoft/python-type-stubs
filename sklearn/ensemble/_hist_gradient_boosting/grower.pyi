from numpy import ndarray
from sklearn.ensemble._hist_gradient_boosting.predictor import TreePredictor
from sklearn.ensemble._hist_gradient_boosting.grower import TreeNode
from numpy.typing import NDArray, ArrayLike

# Author: Nicolas Hug

from heapq import heappush, heappop
import numpy as np
from timeit import default_timer as time
import numbers

from typing import Dict, List, Optional, Tuple, Union

EPS = ...  # to avoid zero division errors

class TreeNode:

    split_info: None = ...
    left_child: None = ...
    right_child: None = ...
    histograms: None = ...

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
        depth: int,
        sample_indices: NDArray,
        sum_gradients: float,
        sum_hessians: float,
        value=None,
    ): ...
    def set_children_bounds(self, lower: float, upper: float) -> None: ...
    def __lt__(self, other_node: TreeNode) -> bool: ...

class TreeGrower:
    def __init__(
        self,
        X_binned: NDArray,
        gradients: NDArray,
        hessians: NDArray,
        max_leaf_nodes: int | None = None,
        max_depth: int | None = None,
        min_samples_leaf: int = 20,
        min_gain_to_split: float = 0.0,
        n_bins: int = 256,
        n_bins_non_missing: NDArray | None = None,
        has_missing_values: bool | NDArray = False,
        is_categorical: NDArray | None = None,
        monotonic_cst: ArrayLike | None = None,
        l2_regularization: float = 0.0,
        min_hessian_to_split: float = 1e-3,
        shrinkage: float = 1.0,
        n_threads: int | None = None,
    ) -> None: ...
    def _validate_parameters(
        self,
        X_binned: ndarray,
        max_leaf_nodes: int,
        max_depth: None,
        min_samples_leaf: int,
        min_gain_to_split: float,
        l2_regularization: float,
        min_hessian_to_split: float,
    ) -> None: ...
    def grow(self) -> None: ...
    def _apply_shrinkage(self) -> None: ...
    def _intilialize_root(self, gradients: ndarray, hessians: ndarray, hessians_are_constant: bool) -> None: ...
    def _compute_best_split_and_push(self, node: TreeNode) -> None: ...
    def split_next(self) -> tuple[TreeNode, TreeNode]: ...
    def _finalize_leaf(self, node: TreeNode) -> None: ...
    def _finalize_splittable_nodes(self) -> None: ...
    def make_predictor(self, binning_thresholds: ArrayLike) -> TreePredictor: ...

def _fill_predictor_arrays(
    predictor_nodes: ndarray,
    binned_left_cat_bitsets: ndarray,
    raw_left_cat_bitsets: ndarray,
    grower_node: TreeNode,
    binning_thresholds: List[ndarray],
    n_bins_non_missing: ndarray,
    next_free_node_idx: int = 0,
    next_free_bitset_idx: int = 0,
) -> Tuple[int, int]: ...
