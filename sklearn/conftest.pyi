from typing import Sequence
from threadpoolctl import threadpool_limits as threadpool_limits
from .utils.fixes import parse_version as parse_version
from _pytest.doctest import DoctestItem as DoctestItem
from os import environ as environ
from .tests import random_seed as random_seed
from ._min_dependencies import PYTEST_MIN_VERSION as PYTEST_MIN_VERSION
from functools import wraps as wraps
from .datasets import (
    fetch_20newsgroups as fetch_20newsgroups,
    fetch_20newsgroups_vectorized as fetch_20newsgroups_vectorized,
    fetch_california_housing as fetch_california_housing,
    fetch_covtype as fetch_covtype,
    fetch_kddcup99 as fetch_kddcup99,
    fetch_olivetti_faces as fetch_olivetti_faces,
    fetch_rcv1 as fetch_rcv1,
)
import platform
import sys

import pytest
import numpy as np

dataset_fetchers: dict = ...

_SKIP32_MARK = ...


# Global fixtures
def global_dtype(request):
    ...


# Adds fixtures for fetching data
fetch_20newsgroups_fxt = ...
fetch_20newsgroups_vectorized_fxt = ...
fetch_california_housing_fxt = ...
fetch_covtype_fxt = ...
fetch_kddcup99_fxt = ...
fetch_olivetti_faces_fxt = ...
fetch_rcv1_fxt = ...


def pytest_collection_modifyitems(config, items: Sequence):
    ...


def pyplot():
    ...


def pytest_runtest_setup(item):
    ...


def pytest_configure(config):
    ...
