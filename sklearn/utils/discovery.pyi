from typing import Literal, Sequence
from ._testing import ignore_warnings as ignore_warnings
from operator import itemgetter as itemgetter
from numpy import ndarray
from ..base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    TransformerMixin as TransformerMixin,
    ClusterMixin as ClusterMixin,
)
from pathlib import Path as Path
from importlib import import_module as import_module
from . import IS_PYPY as IS_PYPY
import pkgutil
import inspect

_MODULE_TO_IGNORE: set = ...


def all_estimators(
    type_filter: None
    | Sequence[Literal["classifier", "regressor", "cluster", "transformer"]]
    | Literal["classifier", "regressor", "cluster", "transformer"] = None
) -> ndarray:
    ...


def all_displays() -> ndarray:
    ...


def all_functions() -> ndarray:
    ...
