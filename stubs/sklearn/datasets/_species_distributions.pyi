import logging
from io import BytesIO as BytesIO
from os import makedirs as makedirs, remove as remove
from os.path import exists as exists

import joblib
import numpy as np
from numpy import ndarray

from ..utils._bunch import Bunch
from . import get_data_home as get_data_home
from ._base import RemoteFileMetadata as RemoteFileMetadata

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/samples.zip
SAMPLES = ...

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/coverages.zip
COVERAGES = ...

DATA_ARCHIVE_NAME: str = ...

logger = ...

def construct_grids(batch) -> ndarray: ...
def fetch_species_distributions(*, data_home: None | str = None, download_if_missing: bool = True) -> Bunch: ...
