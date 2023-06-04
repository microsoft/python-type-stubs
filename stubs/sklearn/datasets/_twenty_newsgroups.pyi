from typing import Literal
from numpy.random import RandomState
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from numpy import ndarray
from .. import preprocessing as preprocessing
from ..utils._bunch import Bunch
from .._typing import ArrayLike, Int
from ..utils import check_random_state as check_random_state
from ..feature_extraction.text import CountVectorizer as CountVectorizer
from . import get_data_home as get_data_home, load_files as load_files

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
import joblib

logger = ...

# The original data can be found at:
# https://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz
ARCHIVE = ...

CACHE_NAME: str = ...
TRAIN_FOLDER: str = ...
TEST_FOLDER: str = ...


def strip_newsgroup_header(text: str) -> str:
    ...


_QUOTE_RE = ...


def strip_newsgroup_quoting(text: str) -> str:
    ...


def strip_newsgroup_footer(text: str) -> str:
    ...


def fetch_20newsgroups(
    *,
    data_home: None | str = None,
    subset: Literal["train", "test", "all", "train"] = "train",
    categories: None | ArrayLike = None,
    shuffle: bool = True,
    random_state: RandomState | None | Int = 42,
    remove: tuple = ...,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> Bunch | tuple[list[str], ndarray] | tuple[Bunch, tuple]:
    ...


def fetch_20newsgroups_vectorized(
    *,
    subset: Literal["train", "test", "all", "train"] = "train",
    remove: tuple = ...,
    data_home: None | str = None,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    normalize: bool = True,
    as_frame: bool = False,
) -> tuple[Bunch, tuple]:
    ...
