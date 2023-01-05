from numpy import ndarray
from typing import Optional, Any, Literal
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Authors: Rob Zinkov, Mathieu Blondel
# License: BSD 3 clause

from ._stochastic_gradient import BaseSGDClassifier
from ._stochastic_gradient import BaseSGDRegressor
from ._stochastic_gradient import DEFAULT_EPSILON
from scipy.sparse._csr import csr_matrix

class PassiveAggressiveClassifier(BaseSGDClassifier):
    def __init__(
        self,
        *,
        C: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float | None = 1e-3,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        shuffle: bool = True,
        verbose: int = 0,
        loss: str = "hinge",
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        warm_start: bool = False,
        class_weight: dict | Literal["balanced"] | None = None,
        average: bool | int = False,
    ) -> None: ...
    def partial_fit(
        self, X: NDArray | ArrayLike, y: ArrayLike, classes: NDArray | None = None
    ) -> "PassiveAggressiveClassifier": ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        coef_init: NDArray | None = None,
        intercept_init: NDArray | None = None,
    ) -> "PassiveAggressiveClassifier": ...

class PassiveAggressiveRegressor(BaseSGDRegressor):
    def __init__(
        self,
        *,
        C: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float | None = 1e-3,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        shuffle: bool = True,
        verbose: int = 0,
        loss: str = "epsilon_insensitive",
        epsilon: float = ...,
        random_state: int | RandomState | None = None,
        warm_start: bool = False,
        average: bool | int = False,
    ): ...
    def partial_fit(self, X: NDArray | ArrayLike, y: NDArray) -> Any: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray,
        coef_init: NDArray | None = None,
        intercept_init: NDArray | None = None,
    ) -> Any: ...
