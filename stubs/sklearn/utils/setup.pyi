from os.path import join
from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup
from .._build_utils import gen_from_templates
import os


def configuration(parent_package: str = "", top_path=None):
    ...
