from typing import Literal, Sequence
from ..utils._bunch import Bunch
from numpy.random import RandomState
from .._typing import Int
from PIL import Image as Image
from urllib.request import urlretrieve as urlretrieve
from ..preprocessing import scale as scale
from pandas.core.frame import DataFrame
from importlib import resources as resources
from collections import namedtuple as namedtuple
from os.path import (
    expanduser as expanduser,
    isdir as isdir,
    join as join,
    splitext as splitext,
)
from os import environ as environ, listdir as listdir, makedirs as makedirs
from ..utils import (
    check_random_state as check_random_state,
    check_pandas_support as check_pandas_support,
)
from numpy import ndarray
from pathlib import Path as Path
from pandas.core.series import Series

# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#               2010 Fabian Pedregosa <fabian.pedregosa@inria.fr>
#               2010 Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause
import csv
import hashlib
import gzip
import shutil
import os

import numpy as np

DATA_MODULE: str = ...
DESCR_MODULE: str = ...
IMAGES_MODULE: str = ...

RemoteFileMetadata = ...


def get_data_home(data_home: str | None = None) -> str:
    ...


def clear_data_home(data_home: str | None = None):
    ...


def load_files(
    container_path: str,
    *,
    description: str | None = None,
    categories: Sequence[str] | None = None,
    load_content: bool = True,
    shuffle: bool = True,
    encoding: str | None = None,
    decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
    random_state: RandomState | None | Int = 0,
    allowed_extensions: Sequence[str] | None = None,
) -> Bunch:
    ...


def load_csv_data(
    data_file_name: str,
    *,
    data_module: str = ...,
    descr_file_name: str | None = None,
    descr_module: str = ...,
) -> tuple[ndarray, ndarray, ndarray, str]:
    ...


def load_gzip_compressed_csv_data(
    data_file_name: str,
    *,
    data_module: str = ...,
    descr_file_name: str | None = None,
    descr_module: str = ...,
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[ndarray, str] | ndarray:
    ...


def load_descr(descr_file_name: str, *, descr_module: str = ...) -> str:
    ...


def load_wine(
    *, return_X_y: bool = False, as_frame: bool = False
) -> tuple[DataFrame, Series] | tuple[Bunch, tuple] | Bunch | tuple[ndarray, ndarray]:
    ...


def load_iris(
    *, return_X_y: bool = False, as_frame: bool = False
) -> tuple[DataFrame, Series] | tuple[Bunch, tuple] | Bunch | tuple[ndarray, ndarray]:
    ...


def load_breast_cancer(
    *, return_X_y: bool = False, as_frame: bool = False
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]:
    ...


def load_digits(
    *, n_class: Int = 10, return_X_y: bool = False, as_frame: bool = False
) -> Bunch | tuple[Bunch, tuple] | tuple[ndarray, ndarray]:
    ...


def load_diabetes(
    *, return_X_y: bool = False, as_frame: bool = False, scaled: bool = True
) -> tuple[DataFrame, Series] | tuple[Bunch, tuple] | Bunch | tuple[ndarray, ndarray]:
    ...


def load_linnerud(
    *, return_X_y: bool = False, as_frame: bool = False
) -> tuple[Bunch, tuple]:
    ...


def load_sample_images() -> Bunch:
    ...


def load_sample_image(image_name: str) -> ndarray:
    ...
