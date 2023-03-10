from typing import Any
from ..utils._param_validation import Interval as Interval
from numpy.random import RandomState
from .._typing import MatrixLike, ArrayLike, Int
from scipy import sparse as sparse
from ..base import BaseEstimator
from numpy import ndarray
from itertools import product as product
from ..utils import check_array as check_array, check_random_state as check_random_state
from scipy.sparse._coo import coo_matrix
from numbers import Integral as Integral, Number as Number, Real as Real
from scipy.sparse import spmatrix
from numpy.lib.stride_tricks import as_strided as as_strided
import numpy as np

__all__ = [
    "PatchExtractor",
    "extract_patches_2d",
    "grid_to_graph",
    "img_to_graph",
    "reconstruct_from_patches_2d",
]


def img_to_graph(
    img: MatrixLike,
    *,
    mask: None | MatrixLike = None,
    return_as: MatrixLike | ArrayLike = ...,
    dtype=None
) -> ndarray | coo_matrix:
    ...


def grid_to_graph(
    n_x: Int,
    n_y: Int,
    n_z: Int = 1,
    *,
    mask: None | MatrixLike = None,
    return_as: MatrixLike | ArrayLike = ...,
    dtype=...
) -> spmatrix | ndarray | coo_matrix:
    ...


def extract_patches_2d(
    image: MatrixLike,
    patch_size: tuple[int, int],
    *,
    max_patches: int | float | None = None,
    random_state: RandomState | None | Int = None
) -> ndarray:
    ...


def reconstruct_from_patches_2d(
    patches: MatrixLike, image_size: tuple[int, int] | tuple[int, int, int]
) -> ndarray:
    ...


class PatchExtractor(BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        patch_size: tuple[int, int] | None = None,
        max_patches: int | float | None = None,
        random_state: RandomState | None | Int = None
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
