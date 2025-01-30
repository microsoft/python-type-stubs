import logging
import tarfile
from os import makedirs as makedirs, remove as remove
from os.path import exists as exists

import joblib
import numpy as np

from ..utils import Bunch
from . import get_data_home as get_data_home
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr

# The original data can be found at:
# https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz
ARCHIVE = ...

logger = ...

def fetch_california_housing(
    *, data_home: None | str = None, download_if_missing: bool = True, return_X_y: bool = False, as_frame: bool = False
) -> tuple[Bunch, tuple]: ...
