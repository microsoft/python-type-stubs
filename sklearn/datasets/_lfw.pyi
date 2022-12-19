from typing import Tuple, Literal
from sklearn.utils import Bunch

# Copyright (c) 2011 Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause

from os import listdir, makedirs, remove
from os.path import join, exists, isdir

import logging

import numpy as np
from joblib import Memory

from ._base import (
    get_data_home,
    _fetch_remote,
    RemoteFileMetadata,
    load_descr,
)
from ..utils import Bunch
import sklearn.utils._bunch

logger = ...

# The original data can be found in:
# http://vis-www.cs.umass.edu/lfw/lfw.tgz
ARCHIVE = ...

# The original funneled data can be found in:
# http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz
FUNNELED_ARCHIVE = ...

# The original target data can be found in:
# http://vis-www.cs.umass.edu/lfw/pairsDevTrain.txt',
# http://vis-www.cs.umass.edu/lfw/pairsDevTest.txt',
# http://vis-www.cs.umass.edu/lfw/pairs.txt',
TARGETS = ...

#
# Common private utilities for data fetching from the original LFW website
# local disk caching, and image decoding.
#

def _check_fetch_lfw(data_home: None = None, funneled: bool = True, download_if_missing: bool = True) -> Tuple[str, str]: ...
def _load_imgs(file_paths, slice_, color, resize): ...

#
# Task #1:  Face Identification on picture with names
#

def _fetch_lfw_people(data_folder_path, slice_=None, color=False, resize=None, min_faces_per_person=0): ...
def fetch_lfw_people(
    *,
    data_home: str | None = None,
    funneled: bool = True,
    resize: float = 0.5,
    min_faces_per_person: int = 0,
    color: bool = False,
    slice_: tuple[slice, ...] = ...,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> tuple[Bunch, tuple]: ...

#
# Task #2:  Face Verification on pairs of face pictures
#

def _fetch_lfw_pairs(index_file_path, data_folder_path, slice_=None, color=False, resize=None): ...
def fetch_lfw_pairs(
    *,
    subset: Literal["train", "test", "10_folds"] = "train",
    data_home: str | None = None,
    funneled: bool = True,
    resize: float = 0.5,
    color: bool = False,
    slice_: tuple[slice, ...] = ...,
    download_if_missing: bool = True,
) -> Bunch: ...
