from numpy import ndarray
from sklearn.utils import Bunch

# Authors: Peter Prettenhofer <peter.prettenhofer@gmail.com>
#          Jake Vanderplas <vanderplas@astro.washington.edu>
#
# License: BSD 3 clause

from io import BytesIO
from os import makedirs, remove
from os.path import exists

import logging
import numpy as np

import joblib

from . import get_data_home
from ._base import _fetch_remote
from ._base import RemoteFileMetadata
from ..utils import Bunch
from ._base import _pkl_filepath

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/samples.zip
SAMPLES = ...

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/coverages.zip
COVERAGES = ...

DATA_ARCHIVE_NAME: str = ...

logger = ...

def _load_coverage(F, header_length=6, dtype=np.int16): ...
def _load_csv(F): ...
def construct_grids(batch: Batch) -> NDArray: ...
def fetch_species_distributions(*, data_home: str | None = None, download_if_missing: bool = True) -> Bunch: ...
