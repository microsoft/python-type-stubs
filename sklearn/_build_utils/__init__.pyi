from .pre_build_helpers import basic_check_build as basic_check_build
from ..externals._packaging.version import parse as parse
from Cython.Build import cythonize as cythonize
from Cython import Tempita as Tempita
from .._min_dependencies import CYTHON_MIN_VERSION as CYTHON_MIN_VERSION
from .openmp_helpers import check_openmp_support as check_openmp_support

# author: Andy Mueller, Gael Varoquaux
# license: BSD


import os as os
import sklearn as sklearn
import contextlib as contextlib


DEFAULT_ROOT: str = ...


def cythonize_extensions(extension):
    ...


def gen_from_templates(templates):
    ...
