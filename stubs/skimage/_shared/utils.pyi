from collections.abc import Iterable
from numpy.typing import ArrayLike, NDArray
from typing import Any, Mapping, Literal
import inspect
import functools
import sys
import warnings
from collections.abc import Iterable

import numpy as np
import scipy
from numpy.lib import NumpyVersion

from ._warnings import all_warnings, warn

__all__ = [
    "deprecated",
    "get_bound_method_class",
    "all_warnings",
    "safe_as_int",
    "check_shape_equality",
    "check_nD",
    "warn",
    "reshape_nd",
    "identity",
    "slice_at_axis",
]

class skimage_deprecation(Warning):
    pass

def _get_stack_rank(func): ...
def _is_wrapped(func): ...
def _get_stack_length(func): ...

class _DecoratorBaseClass:

    _stack_length: dict = ...

    def get_stack_length(self, func): ...

class change_default_value(_DecoratorBaseClass):
    def __init__(
        self,
        arg_name: str,
        *,
        new_value: Any,
        changed_version: str,
        warning_msg: str | None = None
    ): ...
    def __call__(self, func): ...

class remove_arg(_DecoratorBaseClass):
    def __init__(
        self, arg_name: str, *, changed_version: str, help_msg: str | None = None
    ): ...
    def __call__(self, func): ...

def docstring_add_deprecated(
    func, kwarg_mapping: Mapping, deprecated_version: str
) -> str: ...

class deprecate_kwarg(_DecoratorBaseClass):
    def __init__(
        self,
        kwarg_mapping: Mapping,
        deprecated_version: str,
        warning_msg: str | None = None,
        removed_version: str | None = None,
    ): ...
    def __call__(self, func): ...

class deprecate_multichannel_kwarg(deprecate_kwarg):
    def __init__(self, removed_version: str = "1.0", multichannel_position=None): ...
    def __call__(self, func): ...

class channel_as_last_axis:
    def __init__(
        self,
        channel_arg_positions: tuple[int, ...] = ...,
        channel_kwarg_names: tuple[str, ...] = ...,
        multichannel_output: bool = True,
    ): ...
    def __call__(self, func): ...

class deprecated:
    def __init__(
        self,
        alt_func: str | None = None,
        behavior: Literal["warn", "raise"] = "warn",
        removed_version: str | None = None,
    ): ...
    def __call__(self, func): ...

def get_bound_method_class(m): ...
def safe_as_int(val, atol: float = 1e-3): ...
def check_shape_equality(im1, im2): ...
def slice_at_axis(sl, axis: int): ...
def reshape_nd(arr, ndim: int, dim: int): ...
def check_nD(array: ArrayLike, ndim: int | Iterable[int], arg_name: str = "image"): ...
def convert_to_float(image: NDArray, preserve_range: bool) -> NDArray: ...
def _validate_interpolation_order(image_dtype, order): ...
def _to_np_mode(mode): ...
def _to_ndimage_mode(mode): ...
def _fix_ndimage_mode(mode): ...

new_float_type: dict = ...

def _supported_float_type(input_dtype, allow_complex=False): ...
def identity(image, *args, **kwargs): ...
