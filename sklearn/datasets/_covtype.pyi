from tempfile import TemporaryDirectory as TemporaryDirectory
from ..utils._bunch import Bunch
from numpy.random import RandomState
from .._typing import Int
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from os.path import exists as exists, join as join
from numpy import ndarray
from . import get_data_home as get_data_home
from ..utils import check_random_state as check_random_state
from gzip import GzipFile as GzipFile
import logging
import os

import numpy as np
import joblib


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
    data_home: str | None = None,
    download_if_missing: bool = True,
    random_state: RandomState | None | Int = None,
    shuffle: bool = False,
    return_X_y: bool = False,
    as_frame: bool = False,
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]:
    ...
