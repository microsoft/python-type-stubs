from typing import Any, Literal, Self
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy.random import RandomState
from scipy.special import gammaln as gammaln, logsumexp as logsumexp
from .._typing import Int, Float, ArrayLike, MatrixLike
from ._online_lda_fast import mean_change as cy_mean_change
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from joblib import effective_n_jobs as effective_n_jobs
from ..utils.validation import (
    check_non_negative as check_non_negative,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from ..utils import (
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel

import numpy as np
import scipy.sparse as sp

EPS = ...


class LatentDirichletAllocation(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Int = 10,
        *,
        doc_topic_prior: None | Float = None,
        topic_word_prior: None | Float = None,
        learning_method: Literal["batch", "online", "batch"] = "batch",
        learning_decay: Float = 0.7,
        learning_offset: Float = 10.0,
        max_iter: Int = 10,
        batch_size: Int = 128,
        evaluate_every: Int = ...,
        total_samples: float | Int = 1e6,
        perp_tol: Float = 1e-1,
        mean_change_tol: Float = 1e-3,
        max_doc_update_iter: Int = 100,
        n_jobs: None | Int = None,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def partial_fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Self:
        ...

    def fit(
        self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> LatentDirichletAllocation | Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score(self, X: MatrixLike | ArrayLike, y: Any = None) -> float:
        ...

    def perplexity(
        self, X: MatrixLike | ArrayLike, sub_sampling: bool = False
    ) -> float:
        ...
