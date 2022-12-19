from numpy import float64, ndarray
import numpy as np

from typing import (
    Any,
    Dict,
    Iterator,
    Optional,
    Tuple,
    Union,
    Literal,
    Callable,
    Mapping,
    Sequence,
)
from numpy.typing import ArrayLike, NDArray

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Robert Layton <robertlayton@gmail.com>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Philippe Gervais <philippe.gervais@inria.fr>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
# License: BSD 3 clause

import itertools
from functools import partial
import warnings

import numpy as np
from scipy.spatial import distance
from scipy.sparse import csr_matrix
from scipy.sparse import issparse

from .. import config_context
from ..utils.validation import _num_samples
from ..utils.validation import check_non_negative
from ..utils import check_array
from ..utils import gen_even_slices
from ..utils import gen_batches, get_chunk_n_rows
from ..utils import is_scalar_nan
from ..utils.extmath import row_norms, safe_sparse_dot
from ..preprocessing import normalize
from ..utils._mask import _get_mask
from ..utils.fixes import delayed
from ..utils.fixes import sp_version, parse_version

from ..exceptions import DataConversionWarning
import scipy.sparse._csr
from sklearn.gaussian_process.kernels import ExpSineSquared

# Utility Functions
def _return_float_dtype(
    X: Union[ndarray, scipy.sparse._csr.csr_matrix],
    Y: Optional[Union[scipy.sparse._csr.csr_matrix, ndarray]],
) -> Any: ...
def check_pairwise_arrays(
    X: NDArray | ArrayLike,
    Y: NDArray | ArrayLike,
    *,
    precomputed: bool = False,
    dtype: str | type | ArrayLike | None = None,
    accept_sparse: str | bool | Sequence[str] | tuple[str, ...] = "csr",
    force_all_finite: bool | Literal["allow-nan"] = True,
    copy: bool = False,
) -> tuple[NDArray | ArrayLike, NDArray | ArrayLike]: ...
def check_paired_arrays(X: NDArray | ArrayLike, Y: NDArray | ArrayLike) -> tuple[NDArray | ArrayLike, NDArray | ArrayLike]: ...

# Pairwise distances
def euclidean_distances(
    X: NDArray | ArrayLike,
    Y: NDArray | ArrayLike | None = None,
    *,
    Y_norm_squared: ArrayLike | None = None,
    squared: bool = False,
    X_norm_squared: ArrayLike | None = None,
) -> np.ndarray: ...
def _euclidean_distances(
    X: Union[ndarray, scipy.sparse._csr.csr_matrix],
    Y: Union[ndarray, scipy.sparse._csr.csr_matrix],
    X_norm_squared: None = None,
    Y_norm_squared: Optional[ndarray] = None,
    squared: bool = False,
) -> ndarray: ...
def nan_euclidean_distances(
    X: ArrayLike,
    Y: ArrayLike | None = None,
    *,
    squared: bool = False,
    missing_values: float | int = ...,
    copy: bool = True,
) -> np.ndarray: ...
def _euclidean_distances_upcast(
    X: ndarray,
    XX: None = None,
    Y: Optional[ndarray] = None,
    YY: None = None,
    batch_size: None = None,
) -> ndarray: ...
def _argmin_min_reduce(dist, start): ...
def _argmin_reduce(dist, start): ...
def pairwise_distances_argmin_min(
    X: NDArray | ArrayLike,
    Y: NDArray | ArrayLike,
    *,
    axis: int = 1,
    metric: str | Callable = "euclidean",
    metric_kwargs: Mapping | None = None,
) -> tuple[NDArray, NDArray]: ...
def pairwise_distances_argmin(
    X: ArrayLike,
    Y: ArrayLike,
    *,
    axis: int = 1,
    metric: str | Callable = "euclidean",
    metric_kwargs: Mapping | None = None,
) -> NDArray: ...
def haversine_distances(X: ArrayLike, Y: ArrayLike | None = None) -> np.ndarray: ...
def manhattan_distances(X: ArrayLike, Y: ArrayLike | None = None, *, sum_over_features: bool = True) -> np.ndarray: ...
def cosine_distances(X: NDArray | ArrayLike, Y: NDArray | ArrayLike | None = None) -> np.ndarray: ...

# Paired distances
def paired_euclidean_distances(X: ArrayLike, Y: ArrayLike) -> NDArray: ...
def paired_manhattan_distances(X: ArrayLike, Y: ArrayLike) -> NDArray: ...
def paired_cosine_distances(X: ArrayLike, Y: ArrayLike) -> NDArray: ...

PAIRED_DISTANCES: dict = ...

def paired_distances(X: NDArray, Y: NDArray, *, metric: str | Callable = "euclidean", **kwds) -> NDArray: ...

# Kernels
def linear_kernel(X: NDArray, Y: NDArray | None = None, dense_output: bool = True) -> np.ndarray: ...
def polynomial_kernel(
    X: NDArray,
    Y: NDArray | None = None,
    degree: int = 3,
    gamma: float | None = None,
    coef0: float = 1,
) -> np.ndarray: ...
def sigmoid_kernel(X: NDArray, Y: NDArray | None = None, gamma: float | None = None, coef0: float = 1) -> np.ndarray: ...
def rbf_kernel(X: NDArray, Y: NDArray | None = None, gamma: float | None = None) -> np.ndarray: ...
def laplacian_kernel(X: NDArray, Y: NDArray | None = None, gamma: float | None = None) -> np.ndarray: ...
def cosine_similarity(X: NDArray, Y: NDArray | None = None, dense_output: bool = True) -> np.ndarray: ...
def additive_chi2_kernel(X: ArrayLike, Y: NDArray | None = None) -> np.ndarray: ...
def chi2_kernel(X: ArrayLike, Y: NDArray | None = None, gamma: float = 1.0) -> np.ndarray: ...

# Helper functions - distance
PAIRWISE_DISTANCE_FUNCTIONS: dict = ...

def distance_metrics() -> Mapping: ...
def _dist_wrapper(dist_func, dist_matrix, slice_, *args, **kwargs): ...
def _parallel_pairwise(
    X: Union[ndarray, scipy.sparse._csr.csr_matrix],
    Y: Optional[Union[scipy.sparse._csr.csr_matrix, ndarray]],
    func: Union[Callable, partial],
    n_jobs: Optional[int],
    **kwds,
) -> ndarray: ...
def _pairwise_callable(X, Y, metric, force_all_finite=True, **kwds): ...

_VALID_METRICS: list = ...

_NAN_METRICS: list = ...

def _check_chunk_size(reduced: Optional[Union[Tuple[ndarray, ndarray], ndarray]], chunk_size: int) -> None: ...
def _precompute_metric_params(
    X: Union[ndarray, scipy.sparse._csr.csr_matrix],
    Y: Union[ndarray, scipy.sparse._csr.csr_matrix],
    metric: Optional[str] = None,
    **kwds,
) -> Dict[Any, Any]: ...
def pairwise_distances_chunked(
    X: NDArray,
    Y: NDArray | None = None,
    *,
    reduce_func: Callable | None = None,
    metric: str | Callable = "euclidean",
    n_jobs: int | None = None,
    working_memory: int | None = None,
    **kwds,
) -> Iterator[Union[Tuple[ndarray, ndarray], None, ndarray]]: ...
def pairwise_distances(
    X: NDArray,
    Y: NDArray | None = None,
    metric: str | Callable = "euclidean",
    *,
    n_jobs: int | None = None,
    force_all_finite: bool | Literal["allow-nan"] = True,
    **kwds,
) -> np.ndarray: ...

# These distances require boolean arrays, when using scipy.spatial.distance
PAIRWISE_BOOLEAN_FUNCTIONS: list = ...

# Helper functions - distance
PAIRWISE_KERNEL_FUNCTIONS: dict = ...

def kernel_metrics() -> Mapping: ...

KERNEL_PARAMS: dict = ...

def pairwise_kernels(
    X: NDArray,
    Y: NDArray | None = None,
    metric: str | Callable = "linear",
    *,
    filter_params: bool = False,
    n_jobs: int | None = None,
    **kwds,
) -> np.ndarray: ...
