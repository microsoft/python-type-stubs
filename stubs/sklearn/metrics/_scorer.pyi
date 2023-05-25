from typing import Any, Callable
from traceback import format_exc as format_exc
from collections import Counter as Counter
from ..base import BaseEstimator
from numpy import ndarray
from ..utils.multiclass import type_of_target as type_of_target
from functools import partial as partial
from .cluster import (
    adjusted_rand_score as adjusted_rand_score,
    rand_score as rand_score,
    homogeneity_score as homogeneity_score,
    completeness_score as completeness_score,
    v_measure_score as v_measure_score,
    mutual_info_score as mutual_info_score,
    adjusted_mutual_info_score as adjusted_mutual_info_score,
    normalized_mutual_info_score as normalized_mutual_info_score,
    fowlkes_mallows_score as fowlkes_mallows_score,
)
from ..base import is_regressor as is_regressor
from .._typing import Float, MatrixLike, ArrayLike
from collections.abc import Iterable as Iterable
from . import (
    r2_score as r2_score,
    median_absolute_error as median_absolute_error,
    max_error as max_error,
    mean_absolute_error as mean_absolute_error,
    mean_squared_error as mean_squared_error,
    mean_squared_log_error as mean_squared_log_error,
    mean_poisson_deviance as mean_poisson_deviance,
    mean_gamma_deviance as mean_gamma_deviance,
    accuracy_score as accuracy_score,
    top_k_accuracy_score as top_k_accuracy_score,
    f1_score as f1_score,
    roc_auc_score as roc_auc_score,
    average_precision_score as average_precision_score,
    precision_score as precision_score,
    recall_score as recall_score,
    log_loss as log_loss,
    balanced_accuracy_score as balanced_accuracy_score,
    explained_variance_score as explained_variance_score,
    brier_score_loss as brier_score_loss,
    jaccard_score as jaccard_score,
    mean_absolute_percentage_error as mean_absolute_percentage_error,
    matthews_corrcoef as matthews_corrcoef,
    class_likelihood_ratios as class_likelihood_ratios,
)

import numpy as np
import copy
import warnings


class _MultimetricScorer:
    def __init__(self, *, scorers: dict, raise_exc: bool = True) -> None:
        ...

    def __call__(self, estimator, *args, **kwargs) -> dict[str, Float]:
        ...


class _BaseScorer:
    def __init__(self, score_func: Callable, sign: int, kwargs) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __call__(
        self,
        estimator: Any,
        X: MatrixLike | ArrayLike,
        y_true: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...


class _PredictScorer(_BaseScorer):
    ...


class _ProbaScorer(_BaseScorer):
    ...


class _ThresholdScorer(_BaseScorer):
    ...


def get_scorer(scoring: _PredictScorer | None | str | Callable) -> Callable:
    ...


def check_scoring(
    estimator: BaseEstimator,
    scoring: _PredictScorer | None | str | Callable = None,
    *,
    allow_none: bool = False,
) -> Callable:
    ...


def make_scorer(
    score_func: Callable,
    *,
    greater_is_better: bool = True,
    needs_proba: bool = False,
    needs_threshold: bool = False,
    **kwargs,
) -> Callable:
    ...


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


def positive_likelihood_ratio(y_true, y_pred):
    ...


def negative_likelihood_ratio(y_true, y_pred):
    ...


positive_likelihood_ratio_scorer = ...
neg_negative_likelihood_ratio_scorer = ...

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
    def __getitem__(self, item):
        ...


_SCORERS = ...


def get_scorer_names() -> list[str] | ndarray:
    ...


SCORERS = ...
