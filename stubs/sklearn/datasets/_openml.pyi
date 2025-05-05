import gzip
import hashlib
import json
import os
import shutil
import time
from contextlib import closing as closing
from functools import wraps as wraps
from os.path import join as join
from tempfile import TemporaryDirectory as TemporaryDirectory
from typing import Literal, overload
from urllib.error import HTTPError as HTTPError, URLError as URLError
from urllib.request import Request as Request, urlopen as urlopen
from warnings import warn

import numpy as np

from ..utils import Bunch, check_pandas_support as check_pandas_support
from . import get_data_home as get_data_home
from ._arff_parser import load_arff_from_gzip_file as load_arff_from_gzip_file

__all__ = ["fetch_openml"]

_OPENML_PREFIX: str = ...
_SEARCH_NAME: str = ...
_DATA_INFO: str = ...
_DATA_FEATURES: str = ...
_DATA_QUALITIES: str = ...
_DATA_FILE: str = ...

OpenmlQualitiesType = ...
OpenmlFeaturesType = ...

class OpenMLError(ValueError): ...

@overload
def fetch_openml(
    name: str | None = None,
    *,
    version: str | int = "active",
    data_id: int | None = None,
    data_home: str | None = None,
    target_column: str | list | None = "default-target",
    cache: bool = True,
    return_X_y: Literal[False] = ...,
    as_frame: str | bool = "auto",
    n_retries: int = 3,
    delay: float = 1.0,
    parser: str | None = "warn",
) -> Bunch: ...
@overload
def fetch_openml(
    name: str | None = None,
    *,
    version: str | int = "active",
    data_id: int | None = None,
    data_home: str | None = None,
    target_column: str | list | None = "default-target",
    cache: bool = True,
    return_X_y: Literal[True] = ...,
    as_frame: str | bool = "auto",
    n_retries: int = 3,
    delay: float = 1.0,
    parser: str | None = "warn",
) -> tuple[Bunch, tuple]: ...
