from ...base import is_classifier
from numpy import bool_, int64, ndarray
from sklearn.base import BaseEstimator
from typing import Callable, Tuple, Union

def _check_classifier_response_method(estimator: BaseEstimator, response_method: str) -> Callable: ...
def _get_response(
    X: ndarray, estimator: BaseEstimator, response_method: str, pos_label: None = None
) -> Union[Tuple[ndarray, int64], Tuple[ndarray, bool_]]: ...
