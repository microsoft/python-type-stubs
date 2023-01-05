from numpy import bool_, float64, ndarray
from typing import Dict, List, Optional, Tuple, Union, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Jake Vanderplas <vanderplas@astro.washington.edu>
#          Fabian Pedregosa <fabian.pedregosa@inria.fr>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Sparseness support by Lars Buitinck
#          Multi-output support by Arnaud Joly <a.joly@ulg.ac.be>
#
# License: BSD 3 clause (C) INRIA, University of Amsterdam
from functools import partial

import warnings
from abc import ABCMeta, abstractmethod
import numbers

import numpy as np
from scipy.sparse import csr_matrix, issparse

from ..base import BaseEstimator, MultiOutputMixin
from ..base import is_classifier
from ..metrics import pairwise_distances_chunked
from ..metrics.pairwise import PAIRWISE_DISTANCE_FUNCTIONS

from ..utils import (
    check_array,
    gen_even_slices,
    _to_object_array,
)
from ..utils.multiclass import check_classification_targets
from ..utils.validation import check_is_fitted
from ..utils.validation import check_non_negative
from ..utils.fixes import delayed, sp_version
from ..utils.fixes import parse_version
from ..exceptions import DataConversionWarning, EfficiencyWarning
import scipy.sparse._csr
from pandas.core.series import Series
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.neighbors._graph import KNeighborsTransformer
from sklearn.neighbors._kd_tree import KDTree
from sklearn.neighbors._lof import LocalOutlierFactor
from sklearn.neighbors._regression import KNeighborsRegressor
from sklearn.neighbors._unsupervised import NearestNeighbors

VALID_METRICS = ...

VALID_METRICS_SPARSE = ...

def _check_weights(weights: str) -> str: ...
def _get_weights(dist: Optional[ndarray], weights: str) -> Optional[ndarray]: ...
def _is_sorted_by_data(graph: scipy.sparse._csr.csr_matrix) -> bool_: ...
def _check_precomputed(
    X: scipy.sparse._csr.csr_matrix,
) -> scipy.sparse._csr.csr_matrix: ...
def _kneighbors_from_graph(
    graph: scipy.sparse._csr.csr_matrix, n_neighbors: int, return_distance: bool
) -> Union[ndarray, Tuple[ndarray, ndarray]]: ...
def _radius_neighbors_from_graph(graph, radius, return_distance): ...

class NeighborsBase(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        n_neighbors: Optional[int] = None,
        radius: Optional[Union[float, float64]] = None,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: Optional[int] = 2,
        metric_params: None = None,
        n_jobs: Optional[int] = None,
    ) -> None: ...
    def _check_algorithm_metric(self) -> None: ...
    def _fit(
        self,
        X: Union[ndarray, scipy.sparse._csr.csr_matrix, NearestNeighbors],
        y: Optional[Union[ndarray, Series]] = None,
    ) -> Union[KNeighborsTransformer, NearestNeighbors, KNeighborsRegressor, KNeighborsClassifier, LocalOutlierFactor,]: ...
    def _more_tags(self) -> Dict[str, bool]: ...

def _tree_query_parallel_helper(tree: KDTree, *args, **kwargs) -> Union[Tuple[ndarray, ndarray], ndarray]: ...

class KNeighborsMixin:
    def _kneighbors_reduce_func(self, dist: ndarray, start: int, n_neighbors: int, return_distance: bool) -> ndarray: ...
    def kneighbors(
        self,
        X: ArrayLike | None = None,
        n_neighbors: int | None = None,
        return_distance: bool = True,
    ) -> tuple[np.ndarray, np.ndarray]: ...
    def kneighbors_graph(
        self,
        X: ArrayLike | None = None,
        n_neighbors: int | None = None,
        mode: Literal["connectivity", "distance"] = "connectivity",
    ) -> NDArray: ...

def _tree_query_radius_parallel_helper(tree: KDTree, *args, **kwargs) -> ndarray: ...

class RadiusNeighborsMixin:
    def _radius_neighbors_reduce_func(self, dist, start, radius, return_distance): ...
    def radius_neighbors(
        self,
        X: ArrayLike | None = None,
        radius: float | None = None,
        return_distance: bool = True,
        sort_results: bool = False,
    ) -> tuple[NDArray, NDArray]: ...
    def radius_neighbors_graph(
        self,
        X: ArrayLike | None = None,
        radius: float | None = None,
        mode: Literal["connectivity", "distance"] = "connectivity",
        sort_results: bool = False,
    ) -> NDArray: ...
