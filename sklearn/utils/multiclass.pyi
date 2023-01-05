from numpy import ndarray
from numpy.typing import NDArray, ArrayLike

# Author: Arnaud Joly, Joel Nothman, Hamzeh Alsalhi
#
# License: BSD 3 clause
from collections.abc import Sequence
from itertools import chain
import warnings

from scipy.sparse import issparse
from scipy.sparse import dok_matrix
from scipy.sparse import lil_matrix

import numpy as np

from .validation import check_array, _assert_all_finite
from pandas.core.series import Series
from sklearn.linear_model._passive_aggressive import PassiveAggressiveClassifier
from sklearn.linear_model._perceptron import Perceptron
from sklearn.linear_model._stochastic_gradient import SGDClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from typing import List, Optional, Tuple, Union

def _unique_multiclass(y: ndarray) -> ndarray: ...
def _unique_indicator(y: ndarray) -> ndarray: ...

_FN_UNIQUE_LABELS: dict = ...

def unique_labels(*ys) -> np.ndarray: ...
def _is_integral_float(y): ...
def is_multilabel(y: NDArray) -> bool: ...
def check_classification_targets(y: ArrayLike) -> None: ...
def type_of_target(y: ArrayLike, input_name: str = "") -> str: ...
def _check_partial_fit_first_call(
    clf: Union[
        GaussianNB,
        Perceptron,
        PassiveAggressiveClassifier,
        MultinomialNB,
        SGDClassifier,
    ],
    classes: Optional[ndarray] = None,
) -> bool: ...
def class_distribution(
    y: NDArray | ArrayLike, sample_weight: ArrayLike | None = None
) -> tuple[list[NDArray], list[int], list[NDArray]]: ...
def _ovr_decision_function(predictions: ndarray, confidences: ndarray, n_classes: int) -> ndarray: ...
