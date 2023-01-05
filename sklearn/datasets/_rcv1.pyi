from typing import Literal
from sklearn.utils import Bunch

# Author: Tom Dupre la Tour
# License: BSD 3 clause

import logging

from os import remove, makedirs
from os.path import exists, join
from gzip import GzipFile

import numpy as np
import scipy.sparse as sp
import joblib

from . import get_data_home
from ._base import _pkl_filepath
from ._base import _fetch_remote
from ._base import RemoteFileMetadata
from ._base import load_descr
from ._svmlight_format_io import load_svmlight_files
from ..utils import shuffle as shuffle_
from ..utils import Bunch

# The original vectorized data can be found at:
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a13-vector-files/lyrl2004_vectors_test_pt0.dat.gz
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a13-vector-files/lyrl2004_vectors_test_pt1.dat.gz
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a13-vector-files/lyrl2004_vectors_test_pt2.dat.gz
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a13-vector-files/lyrl2004_vectors_test_pt3.dat.gz
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a13-vector-files/lyrl2004_vectors_train.dat.gz
# while the original stemmed token files can be found
# in the README, section B.12.i.:
#    http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/lyrl2004_rcv1v2_README.htm
XY_METADATA = ...

# The original data can be found at:
# http://jmlr.csail.mit.edu/papers/volume5/lewis04a/a08-topic-qrels/rcv1-v2.topics.qrels.gz
TOPICS_METADATA = ...

logger = ...

def fetch_rcv1(
    *,
    data_home: str | None = None,
    subset: Literal["train", "test", "all"] = "all",
    download_if_missing: bool = True,
    random_state: int | RandomState | None = None,
    shuffle: bool = False,
    return_X_y: bool = False,
) -> tuple[Bunch, tuple]: ...
def _inverse_permutation(p): ...
def _find_permutation(a, b): ...
