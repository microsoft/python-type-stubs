from typing_extensions import Self, disjoint_base

import numpy as np

@disjoint_base
class SequentialDataset32:
    current_index: int
    index: np.ndarray
    index_data_ptr: int
    n_samples: int
    seed: int

    def shuffle(self, seed: int) -> None: ...
    def next(self, x_data_ptr, x_ind_ptr, nnz, y, sample_weight) -> None: ...
    def random(self, x_data_ptr, x_ind_ptr, nnz, y, sample_weight) -> int: ...

@disjoint_base
class SequentialDataset64:
    current_index: int
    index: np.ndarray
    index_data_ptr: int
    n_samples: int
    seed: int

    def shuffle(self, seed: int) -> None: ...
    def next(self, x_data_ptr, x_ind_ptr, nnz, y, sample_weight) -> None: ...
    def random(self, x_data_ptr, x_ind_ptr, nnz, y, sample_weight) -> int: ...

@disjoint_base
class ArrayDataset32(SequentialDataset32):
    def __new__(cls, X, Y, sample_weights, seed=1) -> Self: ...

@disjoint_base
class ArrayDataset64(SequentialDataset64):
    def __new__(cls, X, Y, sample_weights, seed=1) -> Self: ...

@disjoint_base
class CSRDataset64(SequentialDataset64):
    def __new__(cls, X_data, X_indptr, X_indices, Y, sample_weights, seed=1) -> Self: ...

@disjoint_base
class CSRDataset32(SequentialDataset32):
    def __new__(cls, X_data, X_indptr, X_indices, Y, sample_weights, seed=1) -> Self: ...
