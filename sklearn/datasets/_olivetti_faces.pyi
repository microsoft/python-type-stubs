from sklearn.utils import Bunch

# Copyright (c) 2011 David Warde-Farley <wardefar at iro dot umontreal dot ca>
# License: BSD 3 clause

from os.path import exists
from os import makedirs, remove

import numpy as np
from scipy.io import loadmat
import joblib

from . import get_data_home
from ._base import _fetch_remote
from ._base import RemoteFileMetadata
from ._base import _pkl_filepath
from ._base import load_descr
from ..utils import check_random_state, Bunch

# The original data can be found at:
# https://cs.nyu.edu/~roweis/data/olivettifaces.mat
FACES = ...

def fetch_olivetti_faces(
    *,
    data_home: str | None = None,
    shuffle: bool = False,
    random_state: int | RandomState | None = 0,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> tuple[Bunch, tuple]: ...
