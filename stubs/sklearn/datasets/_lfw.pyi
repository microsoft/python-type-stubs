import logging
from os import listdir as listdir, makedirs as makedirs, remove as remove
from os.path import exists as exists, isdir as isdir, join as join
from typing import Literal

import numpy as np
from joblib import Memory as Memory

from .._typing import Float, Int
from ..utils._bunch import Bunch
from ._base import RemoteFileMetadata as RemoteFileMetadata, get_data_home as get_data_home, load_descr as load_descr

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
) -> Bunch | tuple[Bunch, tuple]: ...
def fetch_lfw_pairs(
    *,
    subset: Literal["train", "test", "10_folds"] = "train",
    data_home: None | str = None,
    funneled: bool = True,
    resize: Float = 0.5,
    color: bool = False,
    slice_: tuple[slice, ...] = ...,
    download_if_missing: bool = True,
) -> Bunch: ...
