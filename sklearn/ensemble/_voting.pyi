from numpy import ndarray
from typing import List, Optional, Tuple, Union, Sequence, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Sebastian Raschka <se.raschka@gmail.com>,
#          Gilles Louppe <g.louppe@gmail.com>,
#          Ramil Nugmanov <stsouko@live.ru>
#          Mohamed Ali Jamaoui <m.ali.jamaoui@gmail.com>
#
# License: BSD 3 clause

from abc import abstractmethod

import numbers
import numpy as np

from ..base import BaseEstimator, ClassifierMixin
from ..base import RegressorMixin
from ..base import TransformerMixin
from ..base import clone
from ._base import _fit_single_estimator
from ._base import _BaseHeterogeneousEnsemble
from ..preprocessing import LabelEncoder
from ..utils import Bunch
from ..utils import check_scalar
from ..utils.metaestimators import available_if
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_feature_names_in
from ..utils.multiclass import check_classification_targets
from ..utils.validation import column_or_1d
from ..exceptions import NotFittedError
from ..utils._estimator_html_repr import _VisualBlock
from ..utils.fixes import delayed
from sklearn.ensemble._forest import RandomForestRegressor
from sklearn.ensemble._gb import GradientBoostingRegressor
from sklearn.linear_model._base import LinearRegression

class _BaseVoting(TransformerMixin, _BaseHeterogeneousEnsemble):
    def _log_message(self, name: str, idx: int, total: int) -> None: ...
    @property
    def _weights_not_none(self) -> Optional[List[int]]: ...
    def _predict(self, X: ndarray) -> ndarray: ...
    @abstractmethod
    def fit(self, X: ndarray, y: ndarray, sample_weight: None = None) -> Union[VotingRegressor, VotingClassifier]: ...
    def fit_transform(self, X: ArrayLike, y: NDArray | None = None, **fit_params) -> NDArray: ...
    @property
    def n_features_in_(self): ...
    def _sk_visual_block_(self): ...
    def _more_tags(self): ...

class VotingClassifier(ClassifierMixin, _BaseVoting):
    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]],
        *,
        voting: Literal["hard", "soft"] = "hard",
        weights: ArrayLike | None = None,
        n_jobs: int | None = None,
        flatten_transform: bool = True,
        verbose: bool = False,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "VotingClassifier": ...
    def predict(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def _collect_probas(self, X: ndarray) -> ndarray: ...
    def _check_voting(self) -> bool: ...
    @available_if(_check_voting)
    def predict_proba(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def transform(self, X: NDArray | ArrayLike): ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

class VotingRegressor(RegressorMixin, _BaseVoting):
    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]],
        *,
        weights: ArrayLike | None = None,
        n_jobs: int | None = None,
        verbose: bool = False,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "VotingRegressor": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def transform(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
