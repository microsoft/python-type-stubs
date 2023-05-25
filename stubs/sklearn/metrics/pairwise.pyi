from typing import Callable, Iterator, Sequence
from ..exceptions import DataConversionWarning as DataConversionWarning
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from joblib import effective_n_jobs as effective_n_jobs
from scipy.spatial import distance
from ..metrics import DistanceMetric as DistanceMetric
from ..utils.fixes import sp_version as sp_version, parse_version as parse_version
from ..preprocessing import normalize as normalize
from scipy.sparse import csr_matrix as csr_matrix, issparse as issparse
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .. import config_context as config_context
from ..utils.validation import check_non_negative as check_non_negative
from ..gaussian_process.kernels import ExpSineSquared
from numpy import ndarray
from functools import partial as partial
from ..utils import (
    check_array as check_array,
    gen_even_slices as gen_even_slices,
    gen_batches as gen_batches,
    get_chunk_n_rows as get_chunk_n_rows,
    is_scalar_nan as is_scalar_nan,
)
from ..gaussian_process.kernels import Kernel as GPKernel
from ._pairwise_distances_reduction import ArgKmin as ArgKmin
from .._typing import MatrixLike, ArrayLike, Int, Float

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Robert Layton <robertlayton@gmail.com>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Philippe Gervais <philippe.gervais@inria.fr>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
# License: BSD 3 clause

import itertools
import warnings

import numpy as np


def check_pairwise_arrays(
    X: MatrixLike,
    Y: None | MatrixLike,
    *,
    precomputed: bool = False,
    dtype: None | Sequence[type] | str | type = None,
    accept_sparse: Sequence[str] | str | bool = "csr",
    force_all_finite: str | bool = True,
    copy: bool = False,
) -> tuple[ndarray, ndarray]:
    ...


def check_paired_arrays(X: MatrixLike, Y: MatrixLike) -> tuple[ndarray, ndarray]:
    ...


# Pairwise distances
def euclidean_distances(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    *,
    Y_norm_squared: None | MatrixLike | ArrayLike = None,
    squared: bool = False,
    X_norm_squared: None | MatrixLike | ArrayLike = None,
) -> ndarray:
    ...


def nan_euclidean_distances(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    *,
    squared: bool = False,
    missing_values: float | int = ...,
    copy: bool = True,
) -> ndarray:
    ...


def pairwise_distances_argmin_min(
    X: MatrixLike,
    Y: MatrixLike,
    *,
    axis: Int = 1,
    metric: str | Callable = "euclidean",
    metric_kwargs: None | dict = None,
) -> tuple[ndarray, ndarray]:
    ...


def pairwise_distances_argmin(
    X: MatrixLike,
    Y: MatrixLike,
    *,
    axis: Int = 1,
    metric: str | Callable = "euclidean",
    metric_kwargs: None | dict = None,
) -> ndarray:
    ...


def haversine_distances(X: MatrixLike, Y: None | MatrixLike = None) -> ndarray:
    ...


def manhattan_distances(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    *,
    sum_over_features: str | bool = "deprecated",
) -> ndarray:
    ...


def cosine_distances(X: MatrixLike, Y: None | MatrixLike = None) -> ndarray:
    ...


# Paired distances
def paired_euclidean_distances(X: MatrixLike, Y: MatrixLike) -> ndarray:
    ...


def paired_manhattan_distances(X: MatrixLike, Y: MatrixLike) -> ndarray:
    ...


def paired_cosine_distances(X: MatrixLike, Y: MatrixLike) -> ndarray:
    ...


PAIRED_DISTANCES: dict = ...


def paired_distances(
    X: ArrayLike, Y: ArrayLike, *, metric: str | Callable = "euclidean", **kwds
) -> ndarray:
    ...


# Kernels
def linear_kernel(
    X: MatrixLike, Y: None | MatrixLike = None, dense_output: bool = True
) -> ndarray:
    ...


def polynomial_kernel(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    degree: Int = 3,
    gamma: None | Float = None,
    coef0: Float = 1,
) -> ndarray:
    ...


def sigmoid_kernel(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    gamma: None | Float = None,
    coef0: Float = 1,
) -> ndarray:
    ...


def rbf_kernel(
    X: MatrixLike, Y: None | MatrixLike = None, gamma: None | Float = None
) -> ndarray:
    ...


def laplacian_kernel(
    X: MatrixLike, Y: None | MatrixLike = None, gamma: None | Float = None
) -> ndarray:
    ...


def cosine_similarity(
    X: MatrixLike, Y: None | MatrixLike = None, dense_output: bool = True
) -> ndarray:
    ...


def additive_chi2_kernel(X: MatrixLike, Y: None | MatrixLike = None) -> ndarray:
    ...


def chi2_kernel(
    X: MatrixLike, Y: None | MatrixLike = None, gamma: Float = 1.0
) -> ndarray:
    ...


# Helper functions - distance
PAIRWISE_DISTANCE_FUNCTIONS: dict = ...


def distance_metrics() -> dict:
    ...


_VALID_METRICS: list = ...

_NAN_METRICS: list = ...


def pairwise_distances_chunked(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    *,
    reduce_func: None | Callable = None,
    metric: str | Callable = "euclidean",
    n_jobs: None | Int = None,
    working_memory: None | Int = None,
    **kwds,
) -> Iterator[None | ndarray | tuple[ndarray, ndarray]]:
    ...


def pairwise_distances(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    metric: str | Callable = "euclidean",
    *,
    n_jobs: None | Int = None,
    force_all_finite: str | bool = True,
    **kwds,
) -> ndarray:
    ...


# These distances require boolean arrays, when using scipy.spatial.distance
PAIRWISE_BOOLEAN_FUNCTIONS: list = ...

# Helper functions - distance
PAIRWISE_KERNEL_FUNCTIONS: dict = ...


def kernel_metrics() -> dict:
    ...


KERNEL_PARAMS: dict = ...


def pairwise_kernels(
    X: MatrixLike,
    Y: None | MatrixLike = None,
    metric: ExpSineSquared | str | Callable = "linear",
    *,
    filter_params: bool = False,
    n_jobs: None | Int = None,
    **kwds,
) -> ndarray:
    ...
