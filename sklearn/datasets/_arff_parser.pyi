import itertools
from collections import OrderedDict
from collections.abc import Generator
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse

from ..externals._arff import ArffSparseDataType, ArffContainerType
from ..utils import (
    _chunk_generator,
    check_pandas_support,
    get_chunk_n_rows,
    is_scalar_nan,
)

def _split_sparse_columns(arff_data: ArffSparseDataType, include_columns: List) -> ArffSparseDataType: ...
def _sparse_data_to_array(arff_data: ArffSparseDataType, include_columns: List) -> np.ndarray: ...
def _feature_to_dtype(feature: Dict[str, str]): ...
def _convert_arff_data(
    arff: ArffContainerType,
    col_slice_x: List[int],
    col_slice_y: List[int],
    shape: Optional[Tuple] = None,
) -> Tuple: ...
def _convert_arff_data_dataframe(arff: ArffContainerType, columns: List, features_dict: Dict[str, Any]) -> Tuple: ...
def _liac_arff_parser(
    arff_container,
    output_arrays_type,
    features_dict,
    data_columns,
    target_columns,
    col_slice_x=None,
    col_slice_y=None,
    shape=None,
): ...
