from typing import Literal, Mapping
from ..utils._param_validation import StrOptions as StrOptions, Interval as Interval
from ._stochastic_gradient import BaseSGDClassifier
from numpy.random import RandomState
from .._typing import Float, Int
from numbers import Real as Real

# Author: Mathieu Blondel
# License: BSD 3 clause


class Perceptron(BaseSGDClassifier):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        penalty: None | Literal["l2", "l1", "elasticnet"] = None,
        alpha: Float = 0.0001,
        l1_ratio: Float = 0.15,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: None | Float = 1e-3,
        shuffle: bool = True,
        verbose: Int = 0,
        eta0: Float = 1.0,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = 0,
        early_stopping: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: Int = 5,
        class_weight: Mapping[str, float] | str | None = None,
        warm_start: bool = False,
    ) -> None:
        ...
