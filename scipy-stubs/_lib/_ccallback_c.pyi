# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy._lib._ccallback_c, version: unspecified
import typing
import builtins as _mod_builtins
import ctypes as _mod_ctypes

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
def check_capsule(item) -> typing.Any:
    '\n    check_capsule(item)\n\n    Return True if the given object is a PyCapsule.\n    '
    ...

def get_capsule_signature() -> typing.Any:
    ...

def get_raw_capsule(ptr, name, context) -> typing.Any:
    '\n    get_raw_capsule(ptr, name, context)\n\n    Create a new PyCapsule with given pointer, name, and context.\n\n    Parameters\n    ----------\n    ptr : {PyCapsule, int}\n        Memory address of the pointer.\n    name : str\n        Python string containing the signature.\n    context : {PyCapsule, int}\n        Memory address of the context.\n        If NULL and ptr is a PyCapsule, use the one from the context of ptr.\n\n    '
    ...

idx: int
def plus1_ctypes() -> typing.Any:
    ...

plus1_t = _mod_ctypes.CFunctionType
def plus1b_ctypes() -> typing.Any:
    ...

plus1b_t = _mod_ctypes.CFunctionType
def plus1bc_ctypes() -> typing.Any:
    ...

plus1bc_t = _mod_ctypes.CFunctionType
sig: tuple
sigs: list
def sine_ctypes() -> typing.Any:
    ...

sine_t = _mod_ctypes.CFunctionType
def test_call_cython() -> typing.Any:
    '\n    Implementation of a caller routine in Cython\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

