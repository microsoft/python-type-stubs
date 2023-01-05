import os
import sys
import glob
import tempfile
import textwrap
import setuptools  # noqa
import subprocess
import warnings

from distutils.dist import Distribution
from distutils.sysconfig import customize_compiler

def _get_compiler(): ...
def compile_test_program(code, extra_preargs=[], extra_postargs=[]): ...
def basic_check_build(): ...
