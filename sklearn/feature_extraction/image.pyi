from numpy import ndarray
from typing import Optional, Tuple, Type, Any
from numpy.typing import NDArray, ArrayLike, DTypeLike

# Authors: Emmanuelle Gouillart <emmanuelle.gouillart@normalesup.org>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Olivier Grisel
#          Vlad Niculae
# License: BSD 3 clause

from itertools import product
import numbers
import numpy as np
from numpy.random import RandomState
from scipy import sparse
from numpy.lib.stride_tricks import as_strided

from ..utils import check_array, check_random_state
from ..base import BaseEstimator
from scipy.sparse._coo import coo_matrix

__all__ = [
    "PatchExtractor",
    "extract_patches_2d",
    "grid_to_graph",
    "img_to_graph",
    "reconstruct_from_patches_2d",
]

###############################################################################
# From an image to a graph

def _make_edges_3d(n_x: int, n_y: int, n_z: int = 1) -> ndarray: ...
def _compute_gradient_3d(edges: ndarray, img: ndarray) -> ndarray: ...

# XXX: Why mask the image after computing the weights?

def _mask_edges_weights(mask: ndarray, edges: ndarray, weights: Optional[ndarray] = None) -> Tuple[ndarray, ndarray]: ...
def _to_graph(
    n_x: int,
    n_y: int,
    n_z: int,
    mask: Optional[ndarray] = None,
    img: Optional[ndarray] = None,
    return_as: Type[coo_matrix] = sparse.coo_matrix,
    dtype: Optional[Type[int]] = None,
) -> coo_matrix: ...
def img_to_graph(
    img: NDArray, *, mask: NDArray | None = None, return_as: NDArray = ..., dtype: DTypeLike | None = None
) -> NDArray: ...
def grid_to_graph(
    n_x: int, n_y: int, n_z: int = 1, *, mask: NDArray | None = None, return_as: NDArray = ..., dtype: DTypeLike = ...
) -> NDArray: ...

###############################################################################
# From an image to a set of small image patches

def _compute_n_patches(i_h: int, i_w: int, p_h: int, p_w: int, max_patches: Optional[int] = None) -> int: ...
def _extract_patches(arr: ndarray, patch_shape: Tuple[int, int, int] = ..., extraction_step: int = 1) -> ndarray: ...
def extract_patches_2d(
    image: NDArray,
    patch_size: tuple[int, int],
    *,
    max_patches: int | float | None = None,
    random_state: int | RandomState | None = None,
) -> NDArray: ...
def reconstruct_from_patches_2d(patches: NDArray, image_size: tuple[int, int] | tuple[int, int, int]) -> NDArray: ...

class PatchExtractor(BaseEstimator):
    def __init__(
        self,
        *,
        patch_size: tuple[int, int] | None = None,
        max_patches: int | float | None = None,
        random_state: int | RandomState | None = None,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def transform(self, X: NDArray) -> NDArray: ...
    def _more_tags(self): ...
