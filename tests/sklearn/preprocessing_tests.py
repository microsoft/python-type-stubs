# pyright: reportUnknownVariableType=false
# pyright: reportMissingTypeStubs=false

from typing import Any, assert_type

from numpy import ndarray
from scipy.sparse._csr import csr_matrix
from scipy.sparse._matrix import spmatrix
from sklearn.preprocessing import normalize

# normalize with matrix
matrix: spmatrix = spmatrix()
result = normalize(matrix)
assert_type(result, csr_matrix)

result = normalize(matrix, return_norm=False)
assert_type(result, csr_matrix)

result = normalize(matrix, return_norm=True)
assert_type(result, tuple[csr_matrix, ndarray[Any, Any]])

# normalize with array
array_like = [1]
result = normalize(array_like)
assert_type(result, ndarray[Any, Any])

result = normalize(array_like, return_norm=False)
assert_type(result, ndarray[Any, Any])

result = normalize(array_like, return_norm=True)
assert_type(result, tuple[ndarray[Any, Any], ndarray[Any, Any]])
