from typing import ClassVar, Iterable, Literal, TypeVar
from ..model_selection import BaseCrossValidator
from scipy import linalg as linalg
from ._base import LinearModel
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from ..model_selection._split import BaseShuffleSplit
from numbers import Integral as Integral, Real as Real
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs
from math import sqrt as sqrt
from ..base import RegressorMixin, MultiOutputMixin
from ..model_selection import check_cv as check_cv
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import ArrayLike, MatrixLike, Int, Float
from ..utils import as_float_array as as_float_array, check_array as check_array

OrthogonalMatchingPursuitCV_Self = TypeVar(
    "OrthogonalMatchingPursuitCV_Self", bound="OrthogonalMatchingPursuitCV"
)
OrthogonalMatchingPursuit_Self = TypeVar(
    "OrthogonalMatchingPursuit_Self", bound="OrthogonalMatchingPursuit"
)


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
    precompute: str | bool = False,
    copy_X: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
) -> ndarray | tuple[ndarray, int] | tuple[ndarray, ndarray | int]:
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
) -> ndarray | tuple[ndarray, ndarray | int]:
    ...


class OrthogonalMatchingPursuit(MultiOutputMixin, RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_nonzero_coefs_: int = ...
    n_iter_: ArrayLike | int = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_nonzero_coefs: None | Int = None,
        tol: None | Float = None,
        fit_intercept: bool = True,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | bool = "auto",
    ) -> None:
        ...

    def fit(
        self: OrthogonalMatchingPursuit_Self, X: MatrixLike, y: MatrixLike | ArrayLike
    ) -> OrthogonalMatchingPursuit_Self:
        ...


class OrthogonalMatchingPursuitCV(RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: ArrayLike | int = ...
    n_nonzero_coefs_: int = ...
    coef_: ndarray = ...
    intercept_: float | ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        copy: bool = True,
        fit_intercept: bool = True,
        normalize: str | bool = "deprecated",
        max_iter: None | Int = None,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        n_jobs: None | Int = None,
        verbose: int | bool = False,
    ) -> None:
        ...

    def fit(
        self: OrthogonalMatchingPursuitCV_Self, X: MatrixLike, y: ArrayLike
    ) -> OrthogonalMatchingPursuitCV_Self:
        ...
