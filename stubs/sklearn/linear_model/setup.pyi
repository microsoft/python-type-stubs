from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from .._build_utils import gen_from_templates
import os
import numpy


def configuration(parent_package: str = "", top_path=None):
    ...
