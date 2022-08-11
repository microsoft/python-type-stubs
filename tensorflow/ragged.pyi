from typing import Any, Sequence

from tensorflow import RaggedTensor, ScalarTensorCompatible, TensorCompatible

def stack(
    values: Sequence[TensorCompatible | RaggedTensor], axis: ScalarTensorCompatible = 0, name: str | None = None
) -> RaggedTensor: ...
def __getattr__(name: str) -> Any: ...
