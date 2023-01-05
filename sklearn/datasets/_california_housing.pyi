from sklearn.utils import Bunch

# Authors: Peter Prettenhofer
# License: BSD 3 clause

from os.path import exists
from os import makedirs, remove
import tarfile

import numpy as np
import logging

import joblib

from . import get_data_home
from ._base import _convert_data_dataframe
from ._base import _fetch_remote
from ._base import _pkl_filepath
from ._base import RemoteFileMetadata
from ._base import load_descr
from ..utils import Bunch

# The original data can be found at:
# https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz
ARCHIVE = ...

logger = ...

def fetch_california_housing(
    *, data_home: str | None = None, download_if_missing: bool = True, return_X_y: bool = False, as_frame: bool = False
) -> tuple[Bunch, tuple]: ...
