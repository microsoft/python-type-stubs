from sklearn.utils import Bunch
import gzip
import json
import os
import shutil
import hashlib
from os.path import join
import time
from warnings import warn
from contextlib import closing
from functools import wraps
from typing import Callable, Optional, Dict, Tuple, List, Any, Union
from tempfile import TemporaryDirectory
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

import numpy as np

from ..externals import _arff
from . import get_data_home
from ._arff_parser import _liac_arff_parser
from ..utils import Bunch

__all__ = ["fetch_openml"]

_OPENML_PREFIX: str = ...
_SEARCH_NAME: str = ...
_DATA_INFO: str = ...
_DATA_FEATURES: str = ...
_DATA_QUALITIES: str = ...
_DATA_FILE: str = ...

OpenmlQualitiesType = ...
OpenmlFeaturesType = ...

def _get_local_path(openml_path: str, data_home: str) -> str: ...
def _retry_with_clean_cache(openml_path: str, data_home: Optional[str]) -> Callable: ...
def _retry_on_network_error(n_retries: int = 3, delay: float = 1.0, url: str = "") -> Callable: ...
def _open_openml_url(openml_path: str, data_home: Optional[str], n_retries: int = 3, delay: float = 1.0): ...

class OpenMLError(ValueError):
    pass

def _get_json_content_from_openml_api(
    url: str,
    error_message: Optional[str],
    data_home: Optional[str],
    n_retries: int = 3,
    delay: float = 1.0,
) -> Dict: ...
def _get_data_info_by_name(
    name: str,
    version: Union[int, str],
    data_home: Optional[str],
    n_retries: int = 3,
    delay: float = 1.0,
): ...
def _get_data_description_by_id(
    data_id: int,
    data_home: Optional[str],
    n_retries: int = 3,
    delay: float = 1.0,
) -> Dict[str, Any]: ...
def _get_data_features(
    data_id: int,
    data_home: Optional[str],
    n_retries: int = 3,
    delay: float = 1.0,
) -> OpenmlFeaturesType: ...
def _get_data_qualities(
    data_id: int,
    data_home: Optional[str],
    n_retries: int = 3,
    delay: float = 1.0,
) -> OpenmlQualitiesType: ...
def _get_num_samples(data_qualities: OpenmlQualitiesType) -> int: ...
def _load_arff_response(
    url: str,
    data_home: Optional[str],
    output_arrays_type: str,
    features_dict: Dict,
    data_columns: List,
    target_columns: List,
    col_slice_x: List,
    col_slice_y: List,
    shape: Tuple,
    md5_checksum: str,
    n_retries: int = 3,
    delay: float = 1.0,
) -> Tuple: ...
def _download_data_to_bunch(
    url: str,
    sparse: bool,
    data_home: Optional[str],
    *,
    as_frame: bool,
    features_list: List,
    data_columns: List[int],
    target_columns: List,
    shape: Optional[Tuple[int, int]],
    md5_checksum: str,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
def _verify_target_data_type(features_dict, target_columns): ...
def _valid_data_column_names(features_list, target_columns): ...
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
) -> tuple[Bunch, tuple]: ...
