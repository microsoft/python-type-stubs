import warnings
from abc import ABCMeta, abstractmethod as abstractmethod
from operator import attrgetter as attrgetter

import numpy as np
from numpy import ndarray
from scipy.sparse import csc_matrix as csc_matrix, issparse as issparse
from scipy.sparse._csr import csr_matrix

from .._typing import ArrayLike, MatrixLike
from ..base import TransformerMixin
from ..utils import check_array as check_array, safe_mask as safe_mask, safe_sqr as safe_sqr

# Authors: G. Varoquaux, A. Gramfort, L. Buitinck, J. Nothman
# License: BSD 3 clause

class SelectorMixin(TransformerMixin, metaclass=ABCMeta):
    def get_support(self, indices: bool = False) -> ndarray: ...
    def transform(self, X: MatrixLike) -> csr_matrix | ndarray: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
