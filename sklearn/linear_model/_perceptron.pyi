from typing import Literal
from numpy.random import RandomState

# Author: Mathieu Blondel
# License: BSD 3 clause

from ._stochastic_gradient import BaseSGDClassifier

class Perceptron(BaseSGDClassifier):
    def __init__(
        self,
        *,
        penalty: Literal["l2", "l1", "elasticnet"] | None = None,
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-3,
        shuffle: bool = True,
        verbose: int = 0,
        eta0: float = 1.0,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = 0,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        class_weight: dict | Literal["balanced"] | None = None,
        warm_start: bool = False,
    ) -> None: ...
