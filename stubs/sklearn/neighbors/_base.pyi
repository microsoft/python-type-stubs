# Authors: Jake Vanderplas <vanderplas@astro.washington.edu>
#          Fabian Pedregosa <fabian.pedregosa@inria.fr>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Sparseness support by Lars Buitinck
#          Multi-output support by Arnaud Joly <a.joly@ulg.ac.be>
#
# License: BSD 3 clause (C) INRIA, University of Amsterdam
import itertools
import numbers
import warnings
from abc import ABCMeta, abstractmethod
from functools import partial as partial
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Literal

import numpy as np
from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from scipy.sparse import csr_matrix as csr_matrix, issparse as issparse, spmatrix

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, MultiOutputMixin, is_classifier as is_classifier
from ..exceptions import DataConversionWarning as DataConversionWarning, EfficiencyWarning as EfficiencyWarning
from ..metrics import pairwise_distances_chunked as pairwise_distances_chunked
from ..metrics._pairwise_distances_reduction import ArgKmin as ArgKmin, RadiusNeighbors as RadiusNeighbors
from ..metrics.pairwise import PAIRWISE_DISTANCE_FUNCTIONS as PAIRWISE_DISTANCE_FUNCTIONS
from ..utils import check_array as check_array, gen_even_slices as gen_even_slices
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.fixes import parse_version as parse_version, sp_version as sp_version
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted, check_non_negative as check_non_negative
from ._ball_tree import BallTree as BallTree
from ._kd_tree import KDTree as KDTree

VALID_METRICS = ...

VALID_METRICS_SPARSE = ...

def sort_graph_by_row_values(graph: MatrixLike, copy: bool = False, warn_when_not_sorted: bool = True) -> spmatrix: ...

class NeighborsBase(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        n_neighbors: None | int = None,
        radius: None | Float = None,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: None | int = 2,
        metric_params=None,
        n_jobs: None | int = None,
    ) -> None: ...

class KNeighborsMixin:
    def kneighbors(
        self,
        X: None | MatrixLike = None,
        n_neighbors: None | Int = None,
        return_distance: bool = True,
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def kneighbors_graph(
        self,
        X: None | MatrixLike = None,
        n_neighbors: None | Int = None,
        mode: Literal["connectivity", "connectivity", "distance"] = "connectivity",
    ) -> spmatrix: ...

class RadiusNeighborsMixin:
    def radius_neighbors(
        self,
        X: None | MatrixLike | list[ndarray] = None,
        radius: None | Float = None,
        return_distance: bool = True,
        sort_results: bool = False,
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def radius_neighbors_graph(
        self,
        X: None | MatrixLike | ArrayLike = None,
        radius: None | Float = None,
        mode: Literal["connectivity", "distance", "connectivity"] = "connectivity",
        sort_results: bool = False,
    ): ...
