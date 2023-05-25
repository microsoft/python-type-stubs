from typing import Literal
from os import listdir as listdir, makedirs as makedirs, remove as remove
from ._base import (
    get_data_home as get_data_home,
    RemoteFileMetadata as RemoteFileMetadata,
    load_descr as load_descr,
)
from os.path import join as join, exists as exists, isdir as isdir
from joblib import Memory as Memory
from ..utils._bunch import Bunch
from .._typing import Float, Int

import logging

import numpy as np

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


def fetch_lfw_people(
    *,
    data_home: None | str = None,
    funneled: bool = True,
    resize: None | Float = 0.5,
    min_faces_per_person: Int = 0,
    color: bool = False,
    slice_: tuple[slice, ...] = ...,
    download_if_missing: bool = True,
    return_X_y: bool = False,
) -> Bunch | tuple[Bunch, tuple]:
    ...


def fetch_lfw_pairs(
    *,
    subset: Literal["train", "test", "10_folds", "train"] = "train",
    data_home: None | str = None,
    funneled: bool = True,
    resize: Float = 0.5,
    color: bool = False,
    slice_: tuple[slice, ...] = ...,
    download_if_missing: bool = True,
) -> Bunch:
    ...
