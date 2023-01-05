from typing import Optional, Literal
from sklearn.utils import Bunch

import errno
from gzip import GzipFile
import logging
import os
from os.path import exists, join

import numpy as np
import joblib

from ._base import _fetch_remote
from ._base import _convert_data_dataframe
from . import get_data_home
from ._base import RemoteFileMetadata
from ._base import load_descr
from ..utils import Bunch
from ..utils import check_random_state
from ..utils import shuffle as shuffle_method
import sklearn.utils._bunch

# The original data can be found at:
# https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/kddcup.data.gz
ARCHIVE = ...

# The original data can be found at:
# https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/kddcup.data_10_percent.gz
ARCHIVE_10_PERCENT = ...

logger = ...

def fetch_kddcup99(
    *,
    subset: Literal["SA", "SF", "http", "smtp"] | None = None,
    data_home: str | None = None,
    shuffle: bool = False,
    random_state: int | RandomState | None = None,
    percent10: bool = True,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    as_frame: bool = False,
) -> tuple[Bunch, tuple]: ...
def _fetch_brute_kddcup99(
    data_home: Optional[str] = None,
    download_if_missing: bool = True,
    percent10: bool = True,
) -> sklearn.utils._bunch.Bunch: ...
def _mkdirp(d): ...
