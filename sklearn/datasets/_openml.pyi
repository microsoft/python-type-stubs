from typing import List, Optional, Union
from ._arff_parser import load_arff_from_gzip_file as load_arff_from_gzip_file
from tempfile import TemporaryDirectory as TemporaryDirectory
from ..utils._bunch import Bunch
from contextlib import closing as closing
from urllib.request import urlopen as urlopen, Request as Request
from functools import wraps as wraps
from os.path import join as join
from . import get_data_home as get_data_home
from ..utils import check_pandas_support as check_pandas_support
from urllib.error import HTTPError as HTTPError, URLError as URLError
from warnings import warn
import gzip
import hashlib
import json
import os
import shutil
import time

import numpy as np

__all__ = ["fetch_openml"]

_OPENML_PREFIX: str = ...
_SEARCH_NAME: str = ...
_DATA_INFO: str = ...
_DATA_FEATURES: str = ...
_DATA_QUALITIES: str = ...
_DATA_FILE: str = ...

OpenmlQualitiesType = ...
OpenmlFeaturesType = ...


class OpenMLError(ValueError):
    pass


def fetch_openml(
    name: Optional[str] = None,
    *,
    version: Union[str, int] = "active",
    data_id: Optional[int] = None,
    data_home: Optional[str] = None,
    target_column: Optional[Union[str, List]] = "default-target",
    cache: bool = True,
    return_X_y: bool = False,
    as_frame: Union[str, bool] = "auto",
    n_retries: int = 3,
    delay: float = 1.0,
    parser: Optional[str] = "warn",
) -> tuple[Bunch, tuple]:
    ...
