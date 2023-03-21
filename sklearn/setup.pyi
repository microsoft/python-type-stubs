from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from ._build_utils import cythonize_extensions
import sys
import os


def configuration(parent_package: str = "", top_path=None):
    ...
