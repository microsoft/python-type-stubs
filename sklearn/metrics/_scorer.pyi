from typing import Dict, List, Optional, Union, Mapping, Any, Callable
from numpy.typing import ArrayLike, NDArray

# Authors: Andreas Mueller <amueller@ais.uni-bonn.de>
#          Lars Buitinck
#          Arnaud Joly <arnaud.v.joly@gmail.com>
# License: Simplified BSD

from collections.abc import Iterable
from functools import partial
from collections import Counter

import numpy as np
import copy
import warnings

from . import (
    r2_score,
    median_absolute_error,
    max_error,
    mean_absolute_error,
    mean_squared_error,
    mean_squared_log_error,
    mean_poisson_deviance,
    mean_gamma_deviance,
    accuracy_score,
    top_k_accuracy_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    precision_score,
    recall_score,
    log_loss,
    balanced_accuracy_score,
    explained_variance_score,
    brier_score_loss,
    jaccard_score,
    mean_absolute_percentage_error,
    matthews_corrcoef,
)

from .cluster import adjusted_rand_score
from .cluster import rand_score
from .cluster import homogeneity_score
from .cluster import completeness_score
from .cluster import v_measure_score
from .cluster import mutual_info_score
from .cluster import adjusted_mutual_info_score
from .cluster import normalized_mutual_info_score
from .cluster import fowlkes_mallows_score

from ..utils.multiclass import type_of_target
from ..base import is_regressor
from numpy import float64, ndarray
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.svm._classes import SVC

def _cached_call(
    cache: Optional[Dict[str, ndarray]],
    estimator: BaseEstimator,
    method: str,
    *args,
    **kwargs,
) -> ndarray: ...

class _MultimetricScorer:
    def __init__(self, **scorers: Mapping) -> None: ...
    def __call__(self, estimator: BaseEstimator, *args, **kwargs) -> Dict[str, float64]: ...
    def _use_cache(self, estimator: BaseEstimator) -> bool: ...

class _BaseScorer:
    def __init__(
        self,
        score_func: Callable,
        sign: int,
        kwargs: Dict[str, Optional[Union[str, float, bool]]],
    ) -> None: ...
    @staticmethod
    def _check_pos_label(pos_label, classes): ...
    def _select_proba_binary(self, y_pred, classes): ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        estimator: Union[Pipeline, SVC],
        X: NDArray | ArrayLike,
        y_true: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> float: ...
    def _factory_args(self) -> str: ...

class _PredictScorer(_BaseScorer):
    def _score(
        self,
        method_caller: partial,
        estimator: BaseEstimator,
        X: ndarray,
        y_true: ndarray,
        sample_weight: None = None,
    ) -> float64: ...

class _ProbaScorer(_BaseScorer):
    def _score(self, method_caller, clf, X, y, sample_weight=None): ...
    def _factory_args(self): ...

class _ThresholdScorer(_BaseScorer):
    def _score(
        self,
        method_caller: partial,
        clf: SVC,
        X: ndarray,
        y: ndarray,
        sample_weight: None = None,
    ) -> float64: ...
    def _factory_args(self): ...

def get_scorer(scoring: str | Callable) -> Callable: ...
def _passthrough_scorer(estimator: BaseEstimator, *args, **kwargs) -> float64: ...
def check_scoring(
    estimator: Estimator,
    scoring: str | Callable | None = None,
    *,
    allow_none: bool = False,
) -> Callable: ...
def _check_multimetric_scoring(
    estimator: BaseEstimator,
    scoring: Union[
        Dict[str, _PredictScorer],
        List[str],
        Dict[str, Callable],
        Dict[str, Union[str, _PredictScorer]],
    ],
) -> Dict[str, Union[_PredictScorer, Callable, _ThresholdScorer]]: ...
def make_scorer(
    score_func: Callable,
    *,
    greater_is_better: bool = True,
    needs_proba: bool = False,
    needs_threshold: bool = False,
    **kwargs,
) -> Callable: ...

# Standard regression scores
explained_variance_scorer = ...
r2_scorer = ...
max_error_scorer = ...
neg_mean_squared_error_scorer = ...
neg_mean_squared_log_error_scorer = ...
neg_mean_absolute_error_scorer = ...
neg_mean_absolute_percentage_error_scorer = ...
neg_median_absolute_error_scorer = ...
neg_root_mean_squared_error_scorer = ...
neg_mean_poisson_deviance_scorer = ...

neg_mean_gamma_deviance_scorer = ...

# Standard Classification Scores
accuracy_scorer = ...
balanced_accuracy_scorer = ...
matthews_corrcoef_scorer = ...

# Score functions that need decision values
top_k_accuracy_scorer = ...
roc_auc_scorer = ...
average_precision_scorer = ...
roc_auc_ovo_scorer = ...
roc_auc_ovo_weighted_scorer = ...
roc_auc_ovr_scorer = ...
roc_auc_ovr_weighted_scorer = ...

# Score function for probabilistic classification
neg_log_loss_scorer = ...
neg_brier_score_scorer = ...
brier_score_loss_scorer = ...

# Clustering scores
adjusted_rand_scorer = ...
rand_scorer = ...
homogeneity_scorer = ...
completeness_scorer = ...
v_measure_scorer = ...
mutual_info_scorer = ...
adjusted_mutual_info_scorer = ...
normalized_mutual_info_scorer = ...
fowlkes_mallows_scorer = ...

# TODO(1.3) Remove
class _DeprecatedScorers(dict):
    def __getitem__(self, item): ...

_SCORERS = ...

def get_scorer_names() -> ArrayLike: ...

SCORERS = ...
