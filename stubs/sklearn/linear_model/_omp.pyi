from math import sqrt as sqrt
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Iterable, Literal, TypeVar

from numpy import ndarray
from scipy import linalg as linalg
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import MultiOutputMixin, RegressorMixin
from ..model_selection import BaseCrossValidator, check_cv as check_cv
from ..utils import as_float_array as as_float_array, check_array as check_array
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ._base import LinearModel

OrthogonalMatchingPursuitCV_Self = TypeVar("OrthogonalMatchingPursuitCV_Self", bound=OrthogonalMatchingPursuitCV)
OrthogonalMatchingPursuit_Self = TypeVar("OrthogonalMatchingPursuit_Self", bound=OrthogonalMatchingPursuit)

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
) -> ndarray | tuple[ndarray, int] | tuple[ndarray, ndarray | int]: ...
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
) -> ndarray | tuple[ndarray, ndarray | int]: ...

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
        precompute: Literal["auto"] | bool = "auto",
    ) -> None: ...
    def fit(self: OrthogonalMatchingPursuit_Self, X: MatrixLike, y: MatrixLike | ArrayLike) -> OrthogonalMatchingPursuit_Self: ...

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
        cv: int | BaseCrossValidator | Iterable | None = None,
        n_jobs: None | Int = None,
        verbose: int | bool = False,
    ) -> None: ...
    def fit(self: OrthogonalMatchingPursuitCV_Self, X: MatrixLike, y: ArrayLike) -> OrthogonalMatchingPursuitCV_Self: ...
