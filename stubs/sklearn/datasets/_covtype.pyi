import logging
import os
from gzip import GzipFile as GzipFile
from os.path import exists as exists, join as join
from tempfile import TemporaryDirectory as TemporaryDirectory

import joblib
import numpy as np
from numpy import ndarray
from numpy.random import RandomState

from .._typing import Int
from ..utils import check_random_state as check_random_state
from ..utils._bunch import Bunch
from . import get_data_home as get_data_home
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr

# The original data can be found in:
# https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz
ARCHIVE = ...

logger = ...

# Column names reference:
# https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.info
FEATURE_NAMES: list = ...
TARGET_NAMES: list = ...

def fetch_covtype(
    *,
    data_home: None | str = None,
    download_if_missing: bool = True,
    random_state: RandomState | None | Int = None,
    shuffle: bool = False,
    return_X_y: bool = False,
    as_frame: bool = False,
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]: ...
