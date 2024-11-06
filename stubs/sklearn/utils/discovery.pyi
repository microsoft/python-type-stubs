import inspect
import pkgutil
from importlib import import_module as import_module
from operator import itemgetter as itemgetter
from pathlib import Path as Path
from typing import Literal, Sequence

from numpy import ndarray

from ..base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    ClusterMixin as ClusterMixin,
    RegressorMixin as RegressorMixin,
    TransformerMixin as TransformerMixin,
)
from . import IS_PYPY as IS_PYPY
from ._testing import ignore_warnings as ignore_warnings

_MODULE_TO_IGNORE: set = ...

def all_estimators(
    type_filter: (
        None
        | Sequence[Literal["classifier", "regressor", "cluster", "transformer"]]
        | Literal["classifier", "regressor", "cluster", "transformer"]
    ) = None,
) -> ndarray: ...
def all_displays() -> ndarray: ...
def all_functions() -> ndarray: ...
