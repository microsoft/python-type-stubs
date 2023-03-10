from typing import Any, Iterable, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from collections.abc import Iterable
from .._typing import ArrayLike, MatrixLike, Int, Float
from math import sqrt as sqrt
from scipy import linalg as linalg
from ..base import RegressorMixin, MultiOutputMixin
from ..model_selection import check_cv as check_cv
from ._base import LinearModel
from numpy import ndarray
from ..utils import as_float_array as as_float_array, check_array as check_array
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..model_selection import BaseCrossValidator
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs

# Author: Vlad Niculae
#
# License: BSD 3 clause

import warnings
import numpy as np

premature: str = ...


def orthogonal_mp(
    X: ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    n_nonzero_coefs: None | Int = None,
    tol: None | Float = None,
    precompute: bool | str = False,
    copy_X: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
) -> tuple[ndarray, int] | tuple[ndarray, ndarray | int] | ndarray:
    ...


def orthogonal_mp_gram(
    Gram: MatrixLike,
    Xy: MatrixLike | ArrayLike,
    *,
    n_nonzero_coefs: None | Int = None,
    tol: None | Float = None,
    norms_squared: None | ArrayLike = None,
    copy_Gram: bool = True,
    copy_Xy: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
) -> tuple[ndarray, ndarray | int] | ndarray:
    ...


class OrthogonalMatchingPursuit(MultiOutputMixin, RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        n_nonzero_coefs: None | Int = None,
        tol: None | Float = None,
        fit_intercept: bool = True,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] = "auto",
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> Any:
        ...


class OrthogonalMatchingPursuitCV(RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        copy: bool = True,
        fit_intercept: bool = True,
        normalize: bool | str = "deprecated",
        max_iter: None | Int = None,
        cv: Iterable | BaseCrossValidator | int | None = None,
        n_jobs: None | Int = None,
        verbose: bool | int = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...
