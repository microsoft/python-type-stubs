from typing import Callable, Literal, Self, Sequence, Type
from inspect import signature as signature
from scipy.special import kv as kv, gamma
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import ArrayLike, MatrixLike, Float
from ..base import clone as clone
from abc import ABCMeta, abstractmethod
from ..metrics.pairwise import pairwise_kernels as pairwise_kernels
from collections import namedtuple
from numpy import ndarray
from scipy.spatial.distance import (
    pdist as pdist,
    cdist as cdist,
    squareform as squareform,
)
import math

import numpy as np

import warnings


class Hyperparameter(
    namedtuple(
        "Hyperparameter", ("name", "value_type", "bounds", "n_elements", "fixed")
    )
):

    # A raw namedtuple is very memory efficient as it packs the attributes
    # in a struct to get rid of the __dict__ of attributes in particular it
    # does not copy the string for the keys on each instance.
    # By deriving a namedtuple class just to introduce the __init__ method we
    # would also reintroduce the __dict__ on the instance. By telling the
    # Python interpreter that this subclass uses static __slots__ instead of
    # dynamic attributes. Furthermore we don't need any additional slot in the
    # subclass so we set __slots__ to the empty tuple.
    __slots__ = ...

    def __new__(
        cls: Type[Hyperparameter],
        name: str,
        value_type: str,
        bounds: tuple[float, float] | str | tuple[float, int] | ndarray,
        n_elements: int = 1,
        fixed=None,
    ) -> Hyperparameter | Self:
        ...

    # This is mainly a testing utility to check that two hyperparameters
    # are equal.
    def __eq__(self, other) -> bool:
        ...


class Kernel(metaclass=ABCMeta):
    def get_params(self, deep: bool = True) -> dict:
        ...

    def set_params(self, **params) -> Self:
        ...

    def clone_with_theta(self, theta: ArrayLike) -> Product | Sum:
        ...

    @property
    def n_dims(self) -> int:
        ...

    @property
    def hyperparameters(self) -> list[Hyperparameter]:
        ...

    @property
    def theta(self) -> ndarray:
        ...

    @theta.setter
    def theta(self, theta) -> ndarray:
        ...

    @property
    def bounds(self) -> ndarray:
        ...

    def __add__(self, b: Product | WhiteKernel | Sum) -> Sum:
        ...

    def __radd__(self, b):
        ...

    def __mul__(self, b: ExpSineSquared | RBF | Exponentiation) -> Product:
        ...

    def __rmul__(self, b: int | float) -> Product:
        ...

    def __pow__(self, b: int) -> Exponentiation:
        ...

    def __eq__(self, b: str) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __call__(self, X, Y=None, eval_gradient: bool = False):
        ...

    @abstractmethod
    def diag(self, X: ArrayLike) -> ndarray:
        ...

    @abstractmethod
    def is_stationary(self):
        ...

    @property
    def requires_vector_input(self) -> bool:
        ...


class NormalizedKernelMixin:
    def diag(self, X: MatrixLike) -> ndarray:
        ...


class StationaryKernelMixin:
    def is_stationary(self):
        ...


class GenericKernelMixin:
    @property
    def requires_vector_input(self) -> bool:
        ...


class CompoundKernel(Kernel):
    def __init__(self, kernels: Sequence[Kernel]) -> None:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...

    @property
    def theta(self) -> ndarray:
        ...

    @theta.setter
    def theta(self, theta) -> ndarray:
        ...

    @property
    def bounds(self) -> ndarray:
        ...

    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: None | MatrixLike | ArrayLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray]:
        ...

    def __eq__(self, b) -> bool:
        ...

    def is_stationary(self):
        ...

    @property
    def requires_vector_input(self):
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class KernelOperator(Kernel):
    def __init__(self, k1: Product | ConstantKernel | Sum, k2) -> None:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...

    @property
    def hyperparameters(self) -> list[Hyperparameter]:
        ...

    @property
    def theta(self) -> ndarray:
        ...

    @theta.setter
    def theta(self, theta) -> ndarray:
        ...

    @property
    def bounds(self) -> ndarray:
        ...

    def __eq__(self, b) -> bool:
        ...

    def is_stationary(self):
        ...

    @property
    def requires_vector_input(self) -> bool:
        ...


class Sum(KernelOperator):
    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: None | MatrixLike | ArrayLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def __repr__(self) -> str:
        ...


class Product(KernelOperator):
    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: Sequence | None | MatrixLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def __repr__(self) -> str:
        ...


class Exponentiation(Kernel):
    def __init__(self, kernel: DotProduct | Kernel, exponent: Float) -> None:
        ...

    def get_params(self, deep: bool = True) -> dict | dict[str, DotProduct | int]:
        ...

    @property
    def hyperparameters(self) -> list[Hyperparameter]:
        ...

    @property
    def theta(self) -> ndarray:
        ...

    @theta.setter
    def theta(self, theta) -> ndarray:
        ...

    @property
    def bounds(self) -> ndarray:
        ...

    def __eq__(self, b) -> bool:
        ...

    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: Sequence | None | MatrixLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def __repr__(self) -> str:
        ...

    def is_stationary(self):
        ...

    @property
    def requires_vector_input(self) -> bool:
        ...


class ConstantKernel(StationaryKernelMixin, GenericKernelMixin, Kernel):
    def __init__(
        self,
        constant_value: Float = 1.0,
        constant_value_bounds: str | tuple[float, float] = ...,
    ) -> None:
        ...

    @property
    def hyperparameter_constant_value(self) -> Hyperparameter:
        ...

    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: None | MatrixLike | ArrayLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def __repr__(self) -> str:
        ...


class WhiteKernel(StationaryKernelMixin, GenericKernelMixin, Kernel):
    def __init__(
        self,
        noise_level: Float = 1.0,
        noise_level_bounds: str | tuple[float, float] = ...,
    ) -> None:
        ...

    @property
    def hyperparameter_noise_level(self) -> Hyperparameter:
        ...

    def __call__(
        self,
        X: MatrixLike | ArrayLike,
        Y: None | MatrixLike | ArrayLike = None,
        eval_gradient: bool = False,
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def __repr__(self) -> str:
        ...


class RBF(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(
        self,
        length_scale: Float | ArrayLike = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
    ) -> None:
        ...

    @property
    def anisotropic(self) -> bool:
        ...

    @property
    def hyperparameter_length_scale(self) -> Hyperparameter:
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def __repr__(self) -> str:
        ...


class Matern(RBF):
    def __init__(
        self,
        length_scale: Float | ArrayLike = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
        nu: Float = 1.5,
    ) -> None:
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def __repr__(self) -> str:
        ...


class RationalQuadratic(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(
        self,
        length_scale: Float = 1.0,
        alpha: Float = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
        alpha_bounds: str | tuple[float, float] = ...,
    ) -> None:
        ...

    @property
    def hyperparameter_length_scale(self) -> Hyperparameter:
        ...

    @property
    def hyperparameter_alpha(self) -> Hyperparameter:
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def __repr__(self) -> str:
        ...


class ExpSineSquared(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(
        self,
        length_scale: Float = 1.0,
        periodicity: Float = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
        periodicity_bounds: str | tuple[float, float] = ...,
    ) -> None:
        ...

    @property
    def hyperparameter_length_scale(self) -> Hyperparameter:
        ...

    @property
    def hyperparameter_periodicity(self) -> Hyperparameter:
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def __repr__(self) -> str:
        ...


class DotProduct(Kernel):
    def __init__(
        self, sigma_0: Float = 1.0, sigma_0_bounds: str | tuple[float, float] = ...
    ) -> None:
        ...

    @property
    def hyperparameter_sigma_0(self) -> Hyperparameter:
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def diag(self, X: MatrixLike) -> ndarray:
        ...

    def is_stationary(self):
        ...

    def __repr__(self) -> str:
        ...


class PairwiseKernel(Kernel):
    def __init__(
        self,
        gamma: Float = 1.0,
        gamma_bounds: str | tuple[float, float] = ...,
        metric: Literal[
            "linear",
            "additive_chi2",
            "chi2",
            "poly",
            "polynomial",
            "rbf",
            "laplacian",
            "sigmoid",
            "cosine",
            "linear",
        ]
        | Callable = "linear",
        pairwise_kernels_kwargs: dict | None = None,
    ) -> None:
        ...

    @property
    def hyperparameter_gamma(self):
        ...

    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray]:
        ...

    def diag(self, X: MatrixLike) -> ndarray:
        ...

    def is_stationary(self):
        ...

    def __repr__(self) -> str:
        ...
