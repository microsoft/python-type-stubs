# author: Andy Mueller, Gael Varoquaux
# license: BSD

import os as os
import sklearn as sklearn
import contextlib as contextlib

from distutils.version import LooseVersion as LooseVersion

from .pre_build_helpers import basic_check_build as basic_check_build
from .openmp_helpers import check_openmp_support as check_openmp_support
from .._min_dependencies import CYTHON_MIN_VERSION as CYTHON_MIN_VERSION

DEFAULT_ROOT: str = ...

def _check_cython_version(): ...
def cythonize_extensions(top_path, config): ...
def gen_from_templates(templates): ...
