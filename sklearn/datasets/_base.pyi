from numpy import ndarray
from typing import List, Optional, Tuple, Union, Literal
from sklearn.utils import Bunch
from numpy.typing import ArrayLike, NDArray

# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#               2010 Fabian Pedregosa <fabian.pedregosa@inria.fr>
#               2010 Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause
import csv
import hashlib
import gzip
import shutil
from collections import namedtuple
import os
from os import environ, listdir, makedirs
from os.path import expanduser, isdir, join, splitext
from importlib import resources
from pathlib import Path

from ..preprocessing import scale
from ..utils import Bunch
from ..utils import check_random_state
from ..utils import check_pandas_support
from ..utils.deprecation import deprecated

import numpy as np

from urllib.request import urlretrieve
import sklearn.utils._bunch
from pandas.core.frame import DataFrame
from pandas.core.series import Series

DATA_MODULE: str = ...
DESCR_MODULE: str = ...
IMAGES_MODULE: str = ...

RemoteFileMetadata = ...

def get_data_home(data_home: str | None = None) -> str: ...
def clear_data_home(data_home: str | None = None): ...
def _convert_data_dataframe(
    caller_name: str,
    data: ndarray,
    target: ndarray,
    feature_names: List[str],
    target_names: List[str],
    sparse_data: bool = False,
) -> Tuple[DataFrame, DataFrame, Series]: ...
def load_files(
    container_path: str,
    *,
    description: str | None = None,
    categories: ArrayLike | None = None,
    load_content: bool = True,
    shuffle: bool = True,
    encoding: str | None = None,
    decode_error: Literal["strict", "ignore", "replace"] = "strict",
    random_state: int | RandomState | None = 0,
    allowed_extensions: ArrayLike | None = None,
) -> Bunch: ...
def load_csv_data(
    data_file_name: str,
    *,
    data_module: str | module = ...,
    descr_file_name: str | None = None,
    descr_module: str | module = ...,
) -> tuple[NDArray, NDArray, NDArray, str]: ...
def load_gzip_compressed_csv_data(
    data_file_name: str,
    *,
    data_module: str | module = ...,
    descr_file_name: str | None = None,
    descr_module: str | module = ...,
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[NDArray, str]: ...
def load_descr(descr_file_name: str, *, descr_module: str | module = ...) -> str: ...
def load_wine(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_iris(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_breast_cancer(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_digits(*, n_class: int = 10, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
def load_diabetes(*, return_X_y: bool = False, as_frame: bool = False, scaled: bool = True) -> tuple[Bunch, tuple]: ...
def load_linnerud(*, return_X_y: bool = False, as_frame: bool = False) -> tuple[Bunch, tuple]: ...
@deprecated(
    r"""`load_boston` is deprecated in 1.0 and will be removed in 1.2.

    The Boston housing prices dataset has an ethical problem. You can refer to
    the documentation of this function for further details.

    The scikit-learn maintainers therefore strongly discourage the use of this
    dataset unless the purpose of the code is to study and educate about
    ethical issues in data science and machine learning.

    In this special case, you can fetch the dataset from the original
    source::

        import pandas as pd
        import numpy as np

        data_url = "http://lib.stat.cmu.edu/datasets/boston"
        raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
        target = raw_df.values[1::2, 2]

    Alternative datasets include the California housing dataset (i.e.
    :func:`~sklearn.datasets.fetch_california_housing`) and the Ames housing
    dataset. You can load the datasets as follows::

        from sklearn.datasets import fetch_california_housing
        housing = fetch_california_housing()

    for the California housing dataset and::

        from sklearn.datasets import fetch_openml
        housing = fetch_openml(name="house_prices", as_frame=True)

    for the Ames housing dataset."""
)
def load_boston(*, return_X_y: bool = False) -> tuple[Bunch, tuple]: ...
def load_sample_images() -> Bunch: ...
def load_sample_image(image_name: Literal["flower.jpg", "flower.jpg"]) -> NDArray: ...
def _pkl_filepath(*args, **kwargs) -> str: ...
def _sha256(path): ...
def _fetch_remote(remote, dirname=None): ...
