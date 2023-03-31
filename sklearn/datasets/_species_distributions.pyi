from os import makedirs as makedirs, remove as remove
from os.path import exists as exists
from ._base import RemoteFileMetadata as RemoteFileMetadata
from numpy import ndarray
from io import BytesIO as BytesIO
from ..utils._bunch import Bunch
from . import get_data_home as get_data_home

import logging
import numpy as np

import joblib

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/samples.zip
SAMPLES = ...

# The original data can be found at:
# https://biodiversityinformatics.amnh.org/open_source/maxent/coverages.zip
COVERAGES = ...

DATA_ARCHIVE_NAME: str = ...


logger = ...


def construct_grids(batch) -> ndarray:
    ...


def fetch_species_distributions(
    *, data_home: None | str = None, download_if_missing: bool = True
) -> Bunch:
    ...
