from typing import Optional, Tuple, Union, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Chyi-Kwei Yau
# Author: Matthew D. Hoffman (original onlineldavb implementation)

import numpy as np
import scipy.sparse as sp
from scipy.special import gammaln, logsumexp

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils import check_random_state, gen_batches, gen_even_slices
from ..utils.validation import check_non_negative
from ..utils.validation import check_is_fitted
from ..utils.fixes import delayed

from numpy import float64, ndarray
from numpy.random import RandomState
from scipy.sparse._csr import csr_matrix

EPS = ...

def _update_doc_distribution(
    X: csr_matrix,
    exp_topic_word_distr: ndarray,
    doc_topic_prior: float,
    max_doc_update_iter: int,
    mean_change_tol: float,
    cal_sstats: bool,
    random_state: Optional[RandomState],
) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]: ...

class LatentDirichletAllocation(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int = 10,
        *,
        doc_topic_prior: float | None = None,
        topic_word_prior: float | None = None,
        learning_method: Literal["batch", "online"] = "batch",
        learning_decay: float = 0.7,
        learning_offset: float = 10.0,
        max_iter: int = 10,
        batch_size: int = 128,
        evaluate_every: int = ...,
        total_samples: float | int = 1e6,
        perp_tol: float = 1e-1,
        mean_change_tol: float = 1e-3,
        max_doc_update_iter: int = 100,
        n_jobs: int | None = None,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _check_params(self) -> None: ...
    def _init_latent_vars(self, n_features: int) -> None: ...
    def _e_step(
        self,
        X: csr_matrix,
        cal_sstats: bool,
        random_init: bool,
        parallel=None,
    ) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]: ...
    def _em_step(
        self,
        X: csr_matrix,
        total_samples: int,
        batch_update: bool,
        parallel=None,
    ) -> None: ...
    def _more_tags(self): ...
    def _check_non_neg_array(self, X: csr_matrix, reset_n_features: bool, whom: str) -> csr_matrix: ...
    def partial_fit(self, X: NDArray | ArrayLike, y=None): ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "LatentDirichletAllocation": ...
    def _unnormalized_transform(self, X): ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _approx_bound(self, X: csr_matrix, doc_topic_distr: ndarray, sub_sampling: bool) -> float64: ...
    def score(self, X: NDArray | ArrayLike, y=None) -> float: ...
    def _perplexity_precomp_distr(
        self,
        X: csr_matrix,
        doc_topic_distr: Optional[ndarray] = None,
        sub_sampling: bool = False,
    ) -> float64: ...
    def perplexity(self, X: NDArray | ArrayLike, sub_sampling: bool = False) -> float: ...
    @property
    def _n_features_out(self): ...
