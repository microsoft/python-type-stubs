from ..utils._bunch import Bunch
from pandas.core.frame import DataFrame
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from os.path import exists as exists
from numpy import ndarray
from . import get_data_home as get_data_home
from os import makedirs as makedirs, remove as remove
from pandas.core.series import Series
import tarfile

import numpy as np
import logging

import joblib


# The original data can be found at:
# https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz
ARCHIVE = ...

logger = ...


def fetch_california_housing(
    *,
    data_home: str | None = None,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    as_frame: bool = False
) -> tuple[DataFrame, Series] | tuple[Bunch, tuple] | Bunch | tuple[ndarray, ndarray]:
    ...
