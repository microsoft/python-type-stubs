from typing import Dict, Optional, Tuple, Union, Callable

# Author: Joel Nothman
#         Andreas Mueller
# License: BSD
from typing import List, Any
from types import MethodType
import warnings
from functools import wraps

from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import update_wrapper
import numpy as np
from contextlib import suppress

from ..utils import _safe_indexing
from ..utils._tags import _safe_tags
from ..base import BaseEstimator
from numpy import ndarray
from pandas.core.series import Series
from sklearn.base import BaseEstimator
from sklearn.decomposition._nmf import NMF
from sklearn.decomposition._pca import PCA
from sklearn.feature_selection._univariate_selection import SelectKBest
from sklearn.pipeline import FeatureUnion, Pipeline

__all__ = ["available_if", "if_delegate_has_method"]

class _BaseComposition(BaseEstimator, metaclass=ABCMeta):

    steps: List[Any] = ...

    @abstractmethod
    def __init__(self): ...
    def _get_params(self, attr: str, deep: bool = True) -> Dict[str, Any]: ...
    def _set_params(self, attr: str, **params) -> Union[Pipeline, FeatureUnion]: ...
    def _replace_estimator(self, attr: str, name: str, new_val: Union[NMF, PCA, SelectKBest]) -> None: ...
    def _validate_names(
        self,
        names: Union[Tuple[str, str], Tuple[str, str, str, str], Tuple[str, str, str]],
    ) -> None: ...

class _AvailableIfDescriptor:
    def __init__(self, fn: Callable, check: Callable, attribute_name: str) -> None: ...
    def __get__(self, obj: BaseEstimator, owner: Optional[Any] = None) -> Callable: ...

def available_if(check: Callable) -> Callable: ...

# TODO(1.3) remove
class _IffHasAttrDescriptor(_AvailableIfDescriptor):
    def __init__(self, fn, delegate_names, attribute_name): ...
    def _check(self, obj): ...

# TODO(1.3) remove
def if_delegate_has_method(delegate: str | Sequence[str] | tuple[str, ...]): ...
def _safe_split(
    estimator: BaseEstimator,
    X: ndarray,
    y: Optional[Union[ndarray, Series]],
    indices: ndarray,
    train_indices: Optional[ndarray] = None,
) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, Series], Tuple[ndarray, None]]: ...
