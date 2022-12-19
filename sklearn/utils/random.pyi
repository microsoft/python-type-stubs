# Author: Hamzeh Alsalhi <ha258@cornell.edu>
#
# License: BSD 3 clause
import numpy as np
import scipy.sparse as sp
import array

from . import check_random_state
from ._random import sample_without_replacement

__all__ = ["sample_without_replacement"]

def _random_choice_csc(n_samples, classes, class_probability=None, random_state=None): ...
