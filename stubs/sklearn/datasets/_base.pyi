# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#               2010 Fabian Pedregosa <fabian.pedregosa@inria.fr>
#               2010 Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause
import csv
import gzip
import hashlib
import os
import shutil
from collections import namedtuple as namedtuple
from importlib import resources as resources
from os import environ as environ, listdir as listdir, makedirs as makedirs
from os.path import expanduser as expanduser, isdir as isdir, join as join, splitext as splitext
from pathlib import Path as Path
from typing import Literal, Sequence
from urllib.request import urlretrieve as urlretrieve

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from PIL import Image as Image

from .._typing import Int
from ..preprocessing import scale as scale
from ..utils import check_pandas_support as check_pandas_support, check_random_state as check_random_state
from ..utils._bunch import Bunch

DATA_MODULE: str = ...
DESCR_MODULE: str = ...
IMAGES_MODULE: str = ...

RemoteFileMetadata = ...

def get_data_home(data_home: None | str = None) -> str: ...
def clear_data_home(data_home: None | str = None): ...
def load_files(
    container_path: str,
    *,
    description: None | str = None,
    categories: None | Sequence[str] = None,
    load_content: bool = True,
    shuffle: bool = True,
    encoding: None | str = None,
    decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
    random_state: RandomState | None | Int = 0,
    allowed_extensions: None | Sequence[str] = None,
) -> Bunch: ...
def load_csv_data(
    data_file_name: str,
    *,
    data_module: str = ...,
    descr_file_name: None | str = None,
    descr_module: str = ...,
) -> tuple[ndarray, ndarray, ndarray, str]: ...
def load_gzip_compressed_csv_data(
    data_file_name: str,
    *,
    data_module: str = ...,
    descr_file_name: None | str = None,
    descr_module: str = ...,
    encoding: str = "utf-8",
    **kwargs,
) -> ndarray | tuple[ndarray, str]: ...
def load_descr(descr_file_name: str, *, descr_module: str = ...) -> str: ...
def load_wine(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_iris(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_breast_cancer(
    *, return_X_y: bool = False, as_frame: bool = False
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]: ...
def load_digits(
    *, n_class: Int = 10, return_X_y: bool = False, as_frame: bool = False
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]: ...
def load_diabetes(*, return_X_y: bool = False, as_frame: bool = False, scaled: bool = True) -> tuple[Bunch, tuple]: ...
def load_linnerud(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_sample_images() -> Bunch: ...
def load_sample_image(image_name: str) -> ndarray: ...
