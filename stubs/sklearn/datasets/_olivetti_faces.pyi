from os import makedirs as makedirs, remove as remove
from os.path import exists as exists

import joblib
import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from scipy.io import loadmat as loadmat

from .._typing import Int
from ..utils import check_random_state as check_random_state
from ..utils._bunch import Bunch
from . import get_data_home as get_data_home
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr

# The original data can be found at:
# https://cs.nyu.edu/~roweis/data/olivettifaces.mat
FACES = ...

def fetch_olivetti_faces(
    *,
    data_home: None | str = None,
    shuffle: bool = False,
    random_state: RandomState | None | Int = 0,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]: ...
