from tensorflow import SparseTensorCompatible, Tensor, TensorCompatible, TensorShape
from tensorflow.dtypes import DType

class SparseTensor:
    indices: Tensor
    values: Tensor
    dense_shape: Tensor
    shape: TensorShape
    dtype: DType
    name: str
    def __init__(self, indices: TensorCompatible, values: TensorCompatible, dense_shape: TensorCompatible) -> None: ...
    def get_shape(self) -> TensorShape: ...
    # Many arithmetic operations are not directly supported. Some have alternatives like tf.sparse.add instead of +.
    def __div__(self, y: SparseTensorCompatible) -> SparseTensor: ...
    def __truediv__(self, y: SparseTensorCompatible) -> SparseTensor: ...
    def __mul__(self, y: SparseTensorCompatible) -> SparseTensor: ...
    def __rmul__(self, y: SparseTensorCompatible) -> SparseTensor: ...

def to_dense(
    sp_input: SparseTensor,
    default_value: SparseTensorCompatible | None = None,
    validate_indices: bool = True,
    name: str | None = None,
) -> Tensor: ...
def from_dense(tensor: Tensor, name: str | None = None) -> SparseTensor: ...
def slice(
    sp_input: SparseTensor,
    start: list[int] | tuple[int, ...] | Tensor,
    size: TensorCompatible,
    name: str | None = None,
) -> SparseTensor: ...
