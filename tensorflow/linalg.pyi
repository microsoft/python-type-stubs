from typing import overload

from builtins import bool as _bool

from tensorflow import RaggedTensor, Tensor, TensorCompatible

from bento.utils.tensor_types import DTypeLike

@overload
def matmul(
    a: TensorCompatible,
    b: TensorCompatible,
    transpose_a: _bool = False,
    transpose_b: _bool = False,
    adjoint_a: _bool = False,
    adjoint_b: _bool = False,
    a_is_sparse: _bool = False,
    b_is_sparse: _bool = False,
    output_type: DTypeLike | None = None,
    name: str | None = None,
) -> Tensor: ...
@overload
def matmul(
    a: RaggedTensor,
    b: RaggedTensor,
    transpose_a: _bool = False,
    transpose_b: _bool = False,
    adjoint_a: _bool = False,
    adjoint_b: _bool = False,
    a_is_sparse: _bool = False,
    b_is_sparse: _bool = False,
    output_type: DTypeLike | None = None,
    name: str | None = None,
) -> RaggedTensor: ...
