from numpy import ndarray
from numpy.typing import NDArray

# Author: Nicolas Hug

import numpy as np

class TreePredictor:
    def __init__(
        self,
        nodes: NDArray,
        binned_left_cat_bitsets: NDArray,
        raw_left_cat_bitsets: NDArray,
    ) -> None: ...
    def get_n_leaf_nodes(self): ...
    def get_max_depth(self): ...
    def predict(
        self, X: NDArray, known_cat_bitsets: NDArray, f_idx_map: NDArray, n_threads: int
    ) -> NDArray: ...
    def predict_binned(
        self, X: NDArray, missing_values_bin_idx: int, n_threads: int
    ) -> NDArray: ...
    def compute_partial_dependence(
        self, grid: NDArray, target_features: NDArray, out: NDArray
    ) -> None: ...
