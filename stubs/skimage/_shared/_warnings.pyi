from contextlib import contextmanager
import sys
import warnings
import re
import functools
import os

__all__ = ["all_warnings", "expected_warnings", "warn"]

# A version of `warnings.warn` with a default stacklevel of 2.
# functool is used so as not to increase the call stack accidentally
warn = ...

@contextmanager
def all_warnings(): ...
@contextmanager
def expected_warnings(matching): ...
