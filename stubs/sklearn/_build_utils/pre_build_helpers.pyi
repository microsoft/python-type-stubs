from setuptools.command.build_ext import (
    customize_compiler as customize_compiler,
    new_compiler as new_compiler,
)

import os
import sys
import glob
import tempfile
import textwrap
import subprocess


def compile_test_program(code, extra_preargs: list = [], extra_postargs: list = []):
    ...


def basic_check_build():
    ...
