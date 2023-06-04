from typing import Any, Callable, Literal, Mapping, Sequence, Type
from abc import ABC, abstractmethod
from numbers import Integral, Real
from scipy.sparse import issparse as issparse, csr_matrix as csr_matrix
from inspect import signature as signature
from .._typing import Float
from collections.abc import Iterable as Iterable
import functools
import math
import operator
import re
import warnings

import numpy as np


class InvalidParameterError(ValueError, TypeError):
    ...


def validate_parameter_constraints(
    parameter_constraints: Mapping | str, params: dict, caller_name: str
) -> None:
    ...


def make_constraint(constraint: Any) -> _Constraint:
    ...


def validate_params(parameter_constraints: dict) -> Callable:
    ...


class _Constraint(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...


class _InstancesOf(_Constraint):
    def __init__(self, type) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _NoneConstraint(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _NanConstraint(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _PandasNAConstraint(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class Options(_Constraint):
    def __init__(
        self,
        type: Type[str] | Type[type] | Type[Real],
        options: set | set[float] | set[str] | set[Type[Float] | Type[Float]],
        *,
        deprecated: set | None = None
    ) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class StrOptions(Options):
    def __init__(
        self, options: set[str], *, deprecated: set[str] | None = None
    ) -> None:
        ...


class Interval(_Constraint):
    def __init__(
        self,
        type: Real | Type[Integral] | Type[Real] | Integral,
        left: float | None | int,
        right: float | None | int,
        *,
        closed: Literal["left", "right", "both", "neither"]
    ) -> None:
        ...

    def __contains__(self, val: bool | Float) -> bool:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _ArrayLikes(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _SparseMatrices(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _Callables(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _RandomStates(_Constraint):
    def __init__(self) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _Booleans(_Constraint):
    def __init__(self) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _VerboseHelper(_Constraint):
    def __init__(self) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _MissingValues(_Constraint):
    def __init__(self) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class HasMethods(_Constraint):
    def __init__(self, methods: list[str] | str | Sequence[str]) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _IterablesNotString(_Constraint):
    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class _CVObjects(_Constraint):
    def __init__(self) -> None:
        ...

    def is_satisfied_by(self, val: Any) -> bool:
        ...

    def __str__(self) -> str:
        ...


class Hidden:
    def __init__(self, constraint: _Constraint | str) -> None:
        ...


def generate_invalid_param_val(
    constraint: _Constraint, constraints: None | list[_Constraint] = None
) -> Any:
    ...


def generate_valid_param(constraint: _Constraint) -> Any:
    ...
