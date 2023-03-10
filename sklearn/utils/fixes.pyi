from typing import Literal, Mapping
from scipy.linalg import eigh as _eigh
from ..externals._packaging.version import parse as parse_version
from ..externals._lobpcg import lobpcg as lobpcg
from importlib import resources as resources
from numpy import percentile as percentile
from .deprecation import deprecated
from scipy.optimize.linesearch import (
    line_search_wolfe2 as line_search_wolfe2,
    line_search_wolfe1 as line_search_wolfe1,
)
from threadpoolctl import _ThreadpoolLimiter
from .parallel import delayed
import sys

import sklearn
import numpy as np
import scipy
import scipy.stats
import threadpoolctl


np_version = ...
sp_version = ...


class loguniform(scipy.stats.reciprocal):
    pass


def threadpool_limits(
    limits: int | str | Mapping | None = None,
    user_api: Literal["blas", "openmp"] | None = None,
) -> _ThreadpoolLimiter:
    ...


threadpool_limits.__doc__ = ...


def threadpool_info() -> list[dict[str, int | str] | dict[str, str | None | int]]:
    ...


threadpool_info.__doc__ = ...


@deprecated(
    "The function `delayed` has been moved from `sklearn.utils.fixes` to "
    "`sklearn.utils.parallel`. This import path will be removed in 1.5."
)
def delayed(function):
    ...
