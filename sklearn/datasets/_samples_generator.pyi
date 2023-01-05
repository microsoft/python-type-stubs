from numpy import ndarray
from collections.abc import Iterable
from numpy.typing import ArrayLike, NDArray

# Authors: B. Thirion, G. Varoquaux, A. Gramfort, V. Michel, O. Grisel,
#          G. Louppe, J. Nothman
# License: BSD 3 clause

import numbers
import array
import warnings
from collections.abc import Iterable

import numpy as np
from scipy import linalg
import scipy.sparse as sp

from ..preprocessing import MultiLabelBinarizer
from ..utils import check_array, check_random_state
from ..utils import shuffle as util_shuffle
from ..utils.random import sample_without_replacement
from numpy.random.mtrand import RandomState
from typing import List, Tuple, Union

def _generate_hypercube(samples: int, dimensions: int, rng: RandomState) -> ndarray: ...
def make_classification(
    n_samples: int = 100,
    n_features: int = 20,
    *,
    n_informative: int = 2,
    n_redundant: int = 2,
    n_repeated: int = 0,
    n_classes: int = 2,
    n_clusters_per_class: int = 2,
    weights: ArrayLike | None = None,
    flip_y: float = 0.01,
    class_sep: float = 1.0,
    hypercube: bool = True,
    shift: float | NDArray | None = 0.0,
    scale: float | NDArray | None = 1.0,
    shuffle: bool = True,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray]: ...
def make_multilabel_classification(
    n_samples: int = 100,
    n_features: int = 20,
    *,
    n_classes: int = 5,
    n_labels: int = 2,
    length: int = 50,
    allow_unlabeled: bool = True,
    sparse: bool = False,
    return_indicator: Literal["dense", "sparse"] | Literal[False] = "dense",
    return_distributions: bool = False,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray, NDArray, np.ndarray]: ...
def make_hastie_10_2(n_samples: int = 12000, *, random_state: int | RandomState | None = None) -> tuple[np.ndarray, NDArray]: ...
def make_regression(
    n_samples: int = 100,
    n_features: int = 100,
    *,
    n_informative: int = 10,
    n_targets: int = 1,
    bias: float = 0.0,
    effective_rank: int | None = None,
    tail_strength: float = 0.5,
    noise: float = 0.0,
    shuffle: bool = True,
    coef: bool = False,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray, NDArray]: ...
def make_circles(
    n_samples: int | tuple = 100,
    *,
    shuffle: bool = True,
    noise: float | None = None,
    random_state: int | RandomState | None = None,
    factor: float = 0.8,
) -> tuple[np.ndarray, NDArray]: ...
def make_moons(
    n_samples: int | tuple = 100,
    *,
    shuffle: bool = True,
    noise: float | None = None,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, NDArray]: ...
def make_blobs(
    n_samples: int | ArrayLike = 100,
    n_features: int = 2,
    *,
    centers: int | NDArray | None = None,
    cluster_std: float | ArrayLike = 1.0,
    center_box: tuple[float] = ...,
    shuffle: bool = True,
    random_state: int | RandomState | None = None,
    return_centers: bool = False,
) -> tuple[NDArray, NDArray, np.ndarray]: ...
def make_friedman1(
    n_samples: int = 100,
    n_features: int = 10,
    *,
    noise: float = 0.0,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray]: ...
def make_friedman2(
    n_samples: int = 100,
    *,
    noise: float = 0.0,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, NDArray]: ...
def make_friedman3(
    n_samples: int = 100,
    *,
    noise: float = 0.0,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, NDArray]: ...
def make_low_rank_matrix(
    n_samples: int = 100,
    n_features: int = 100,
    *,
    effective_rank: int = 10,
    tail_strength: float = 0.5,
    random_state: int | RandomState | None = None,
) -> NDArray: ...

# TODO(1.3): Change argument `data_transposed` default from True to False.
# TODO(1.3): Deprecate data_transposed, always return data not transposed.
def make_sparse_coded_signal(
    n_samples: int,
    *,
    n_components: int,
    n_features: int,
    n_nonzero_coefs: int,
    random_state: int | RandomState | None = None,
    data_transposed: bool = "warn",
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: ...
def make_sparse_uncorrelated(
    n_samples: int = 100,
    n_features: int = 10,
    *,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray]: ...
def make_spd_matrix(n_dim: int, *, random_state: int | RandomState | None = None) -> np.ndarray: ...
def make_sparse_spd_matrix(
    dim: int = 1,
    *,
    alpha: float = 0.95,
    norm_diag: bool = False,
    smallest_coef: float = 0.1,
    largest_coef: float = 0.9,
    random_state: int | RandomState | None = None,
) -> NDArray: ...
def make_swiss_roll(
    n_samples: int = 100,
    *,
    noise: float = 0.0,
    random_state: int | RandomState | None = None,
    hole: bool = False,
) -> tuple[np.ndarray, NDArray]: ...
def make_s_curve(
    n_samples: int = 100,
    *,
    noise: float = 0.0,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, NDArray]: ...
def make_gaussian_quantiles(
    *,
    mean: NDArray | None = None,
    cov: float = 1.0,
    n_samples: int = 100,
    n_features: int = 2,
    n_classes: int = 3,
    shuffle: bool = True,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray]: ...
def _shuffle(data, random_state=None): ...
def make_biclusters(
    shape: Iterable,
    n_clusters: int,
    *,
    noise: float = 0.0,
    minval: int = 10,
    maxval: int = 100,
    shuffle: bool = True,
    random_state: int | RandomState | None = None,
) -> Tuple[ndarray, ndarray, ndarray]: ...
def make_checkerboard(
    shape: tuple,
    n_clusters: int | ArrayLike,
    *,
    noise: float = 0.0,
    minval: int = 10,
    maxval: int = 100,
    shuffle: bool = True,
    random_state: int | RandomState | None = None,
) -> Tuple[ndarray, ndarray, ndarray]: ...
