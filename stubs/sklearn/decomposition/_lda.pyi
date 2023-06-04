from typing import Any, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from scipy.special import gammaln as gammaln, logsumexp as logsumexp
from numpy import ndarray
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from joblib import effective_n_jobs as effective_n_jobs
from numbers import Integral as Integral, Real as Real
from ._online_lda_fast import mean_change as cy_mean_change
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import Int, Float, MatrixLike, ArrayLike
from ..utils import (
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from ..utils.validation import (
    check_non_negative as check_non_negative,
    check_is_fitted as check_is_fitted,
)

LatentDirichletAllocation_Self = TypeVar(
    "LatentDirichletAllocation_Self", bound="LatentDirichletAllocation"
)


import numpy as np
import scipy.sparse as sp

EPS = ...


class LatentDirichletAllocation(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):
    topic_word_prior_: float = ...
    random_state_: RandomState = ...
    doc_topic_prior_: float = ...
    bound_: float = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_batch_iter_: int = ...
    exp_dirichlet_component_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def partial_fit(
        self: LatentDirichletAllocation_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> LatentDirichletAllocation_Self:
        ...

    def fit(
        self: LatentDirichletAllocation_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> LatentDirichletAllocation_Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score(self, X: MatrixLike | ArrayLike, y: Any = None) -> float:
        ...

    def perplexity(
        self, X: MatrixLike | ArrayLike, sub_sampling: bool = False
    ) -> float:
        ...
