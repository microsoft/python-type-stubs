from sklearn.utils import Bunch

# Author: Lars Buitinck
#         Peter Prettenhofer <peter.prettenhofer@gmail.com>
# License: BSD 3 clause

from gzip import GzipFile
import logging
from os.path import exists, join
import os
from tempfile import TemporaryDirectory

import numpy as np
import joblib

from . import get_data_home
from ._base import _convert_data_dataframe
from ._base import _fetch_remote
from ._base import RemoteFileMetadata
from ._base import load_descr
from ..utils import Bunch
from ._base import _pkl_filepath
from ..utils import check_random_state

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
    random_state: int | RandomState | None = None,
    shuffle: bool = False,
    return_X_y: bool = False,
    as_frame: bool = False,
) -> tuple[Bunch, tuple]: ...
