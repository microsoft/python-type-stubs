import glob
import os
import subprocess
import sys
import tempfile
import textwrap

def compile_test_program(code, extra_preargs: list = [], extra_postargs: list = []): ...
def basic_check_build(): ...
