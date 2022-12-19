from typing import List, Tuple, Union, Literal
from sklearn.utils import Bunch
from numpy.typing import ArrayLike

# Copyright (c) 2011 Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause

import os
import logging
import tarfile
import pickle
import shutil
import re
import codecs

import numpy as np
import scipy.sparse as sp
from numpy.random import RandomState

from . import get_data_home
from . import load_files
from ._base import _convert_data_dataframe
from ._base import _pkl_filepath
from ._base import _fetch_remote
from ._base import RemoteFileMetadata
from ._base import load_descr
from ..feature_extraction.text import CountVectorizer
from .. import preprocessing
from ..utils import check_random_state, Bunch
import sklearn.utils._bunch
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

logger = ...

# The original data can be found at:
# https://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz
ARCHIVE = ...

CACHE_NAME: str = ...
TRAIN_FOLDER: str = ...
TEST_FOLDER: str = ...

def _download_20newsgroups(target_dir, cache_path): ...
def strip_newsgroup_header(text: str) -> str: ...

_QUOTE_RE = ...

def strip_newsgroup_quoting(text: str) -> str: ...
def strip_newsgroup_footer(text: str) -> str: ...
def fetch_20newsgroups(
    *,
    data_home: str | None = None,
    subset: Literal["train", "test", "all"] = "train",
    categories: ArrayLike | None = None,
    shuffle: bool = True,
    random_state: int | RandomState | None = 42,
    remove: tuple = ...,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> tuple[Bunch, tuple]: ...
def fetch_20newsgroups_vectorized(
    *,
    subset: Literal["train", "test", "all"] = "train",
    remove: tuple = ...,
    data_home: str | None = None,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    normalize: bool = True,
    as_frame: bool = False,
) -> tuple[Bunch, tuple]: ...
