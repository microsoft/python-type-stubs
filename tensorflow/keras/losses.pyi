from typing import Any, Literal
from typing_extensions import Self, TypeGuard

from abc import ABC, abstractmethod

from tensorflow import Tensor

from bento.utils.tensor_types import TensorCompatible

class Loss(ABC):
    reduction: _ReductionValues
    name: str | None
    def __init__(self, reduction: _ReductionValues = "auto", name: str | None = None): ...
    @abstractmethod
    def call(self, y_true: Tensor, y_pred: Tensor) -> Tensor: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...
    def get_config(self) -> dict[str, Any]: ...
    def __call__(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Tensor: ...

class BinaryCrossentropy(Loss):
    def call(self, y_true: Tensor, y_pred: Tensor) -> Tensor: ...

class MeanSquaredError(Loss):
    def call(self, y_true: Tensor, y_pred: Tensor) -> Tensor: ...

class MeanSquaredLogarithmicError(Loss):
    def call(self, y_true: Tensor, y_pred: Tensor) -> Tensor: ...

class Reduction:
    AUTO = "auto"
    NONE = "none"
    SUM = "sum"
    SUM_OVER_BATCH_SIZE = "sum_over_batch_size"
    @classmethod
    def all(cls) -> tuple[_ReductionValues, ...]: ...
    @classmethod
    def validate(cls, key: object) -> TypeGuard[_ReductionValues]: ...

_ReductionValues = Literal["auto", "none", "sum", "sum_over_batch_size"]
