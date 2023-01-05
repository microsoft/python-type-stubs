from numpy import ndarray
from typing import Callable, List, Optional, Tuple, Union, Any, Sequence, Literal, Generator, Iterable
from numpy.typing import ArrayLike, NDArray

# Authors: Guillaume Lemaitre <g.lemaitre58@gmail.com>
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod
from copy import deepcopy

import numpy as np
from numpy.random import RandomState
import scipy.sparse as sparse

from ..base import BaseEstimator, clone
from ..base import ClassifierMixin, RegressorMixin, TransformerMixin
from ..base import is_classifier, is_regressor
from ..exceptions import NotFittedError
from ..utils._estimator_html_repr import _VisualBlock

from ._base import _fit_single_estimator
from ._base import _BaseHeterogeneousEnsemble

from ..linear_model import LogisticRegression
from ..linear_model import RidgeCV

from ..model_selection import cross_val_predict
from ..model_selection import check_cv

from ..preprocessing import LabelEncoder

from ..utils import Bunch
from ..utils.metaestimators import available_if
from ..utils.multiclass import check_classification_targets
from ..utils.validation import check_is_fitted
from ..utils.validation import check_scalar
from ..utils.validation import column_or_1d
from ..utils.fixes import delayed
from ..utils.validation import _check_feature_names_in
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.pipeline import Pipeline

def _estimator_has(attr: str) -> Callable: ...

class _BaseStacking(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimators: List[Union[Tuple[str, RandomForestClassifier], Tuple[str, Pipeline]]],
        final_estimator: Optional[LogisticRegression] = None,
        *,
        cv=None,
        stack_method="auto",
        n_jobs=None,
        verbose=0,
        passthrough=False,
    ) -> None: ...
    def _clone_final_estimator(self, default: LogisticRegression) -> None: ...
    def _concatenate_predictions(self, X: ndarray, predictions: List[ndarray]) -> ndarray: ...
    @staticmethod
    def _method_name(name: str, estimator: Union[Pipeline, RandomForestClassifier], method: str) -> str: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "StackingClassifier": ...
    @property
    def n_features_in_(self): ...
    def _transform(self, X: ndarray) -> ndarray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    @available_if(_estimator_has("predict"))
    def predict(self, X: NDArray | ArrayLike, **predict_params) -> np.ndarray: ...
    def _sk_visual_block_(self, final_estimator): ...

class StackingClassifier(ClassifierMixin, _BaseStacking):
    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]],
        final_estimator: BaseEstimator | None = None,
        *,
        cv: int | Generator | Iterable | Literal["prefit"] | None = None,
        stack_method: Literal["auto", "predict_proba", "decision_function", "predict"] = "auto",
        n_jobs: int | None = None,
        passthrough: bool = False,
        verbose: int = 0,
    ) -> None: ...
    def _validate_final_estimator(self) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "StackingClassifier": ...
    @available_if(_estimator_has("predict"))
    def predict(self, X: NDArray | ArrayLike, **predict_params) -> np.ndarray: ...
    @available_if(_estimator_has("predict_proba"))
    def predict_proba(self, X: NDArray | ArrayLike) -> NDArray | list[NDArray]: ...
    @available_if(_estimator_has("decision_function"))
    def decision_function(self, X: NDArray | ArrayLike) -> NDArray: ...
    def transform(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def _sk_visual_block_(self): ...

class StackingRegressor(RegressorMixin, _BaseStacking):
    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]],
        final_estimator: BaseEstimator | None = None,
        *,
        cv: int | Generator | Iterable | Literal["prefit"] | None = None,
        n_jobs: int | None = None,
        passthrough: bool = False,
        verbose: int = 0,
    ): ...
    def _validate_final_estimator(self): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def transform(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def _sk_visual_block_(self): ...
