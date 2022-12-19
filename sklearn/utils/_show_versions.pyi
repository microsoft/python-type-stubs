# License: BSD 3 clause

import platform
import sys
from ..utils.fixes import threadpool_info
from .. import __version__

from ._openmp_helpers import _openmp_parallelism_enabled

def _get_sys_info(): ...
def _get_deps_info(): ...
def show_versions(): ...
