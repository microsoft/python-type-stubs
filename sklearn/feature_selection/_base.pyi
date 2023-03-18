from operator import attrgetter as attrgetter
from abc import ABCMeta, abstractmethod as abstractmethod
from numpy import ndarray
from ..base import TransformerMixin
from scipy.sparse import issparse as issparse, csc_matrix as csc_matrix
from scipy.sparse._csr import csr_matrix
from .._typing import MatrixLike, ArrayLike
from ..utils import (
    check_array as check_array,
    safe_mask as safe_mask,
    safe_sqr as safe_sqr,
)

# Authors: G. Varoquaux, A. Gramfort, L. Buitinck, J. Nothman
# License: BSD 3 clause

import warnings

import numpy as np


class SelectorMixin(TransformerMixin, metaclass=ABCMeta):
    def get_support(self, indices: bool = False) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> csr_matrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
