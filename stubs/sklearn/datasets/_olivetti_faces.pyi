from numpy.random import RandomState
from os import makedirs as makedirs, remove as remove
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from os.path import exists as exists
from numpy import ndarray
from ..utils._bunch import Bunch
from scipy.io import loadmat as loadmat
from .._typing import Int
from ..utils import check_random_state as check_random_state
from . import get_data_home as get_data_home

import numpy as np
import joblib

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
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]:
    ...
