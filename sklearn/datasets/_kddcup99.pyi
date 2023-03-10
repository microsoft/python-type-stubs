from typing import Literal
from ..utils._bunch import Bunch
from numpy.random import RandomState
from .._typing import Int
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from os.path import exists as exists, join as join
from . import get_data_home as get_data_home
from ..utils import check_random_state as check_random_state, shuffle as shuffle_method
from gzip import GzipFile as GzipFile

import errno
import logging
import os

import numpy as np
import joblib


# The original data can be found at:
# https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/kddcup.data.gz
ARCHIVE = ...

# The original data can be found at:
# https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/kddcup.data_10_percent.gz
ARCHIVE_10_PERCENT = ...

logger = ...


def fetch_kddcup99(
    *,
    subset: None | Literal["SA", "SF", "http", "smtp"] = None,
    data_home: str | None = None,
    shuffle: bool = False,
    random_state: RandomState | None | Int = None,
    percent10: bool = True,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    as_frame: bool = False,
) -> Bunch | tuple[Bunch, tuple]:
    ...
