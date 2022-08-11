from typing import Any, Callable, Generic, Iterable, Sequence, TypeVar, final, overload
from typing_extensions import Self

from abc import ABC, abstractmethod

import numpy as np

import tensorflow as tf
from tensorflow import DTypeLike, Tensor, Variable
from tensorflow.keras.activations import ActivationT
from tensorflow.keras.constraints import ConstraintT
from tensorflow.keras.initializers import InitializerT
from tensorflow.keras.regularizers import RegularizerT

from bento.utils.tensor_types import ContainerInputSpec, TensorCompatible

_InputT = TypeVar("_InputT", contravariant=True)
_OutputT = TypeVar("_OutputT", covariant=True)

class InputSpec:
    dtype: str | None
    shape: tuple[int | None, ...]
    ndim: int | None
    max_ndim: int | None
    min_ndim: int | None
    axes: dict[int, int | None] | None
    def __init__(
        self,
        dtype: tf.DTypeLike | None = None,
        shape: Iterable[int | None] | None = None,
        ndim: int | None = None,
        max_ndim: int | None = None,
        min_ndim: int | None = None,
        axes: dict[int, int | None] | None = None,
        allow_last_axis_squeeze: bool = False,
    ): ...

class Layer(Generic[_InputT, _OutputT], tf.Module, ABC):
    input_spec: ContainerInputSpec
    trainable: bool
    def __init__(
        self, trainable: bool = True, name: str | None = None, dtype: DTypeLike | None = None, dynamic: bool = False
    ) -> None: ...
    @final
    def __call__(self, inputs: _InputT, *, training: bool = False) -> _OutputT: ...
    @overload
    def build(self: Layer[tf.Tensor, object], input_shape: tf.TensorShape) -> None: ...
    @overload
    def build(self, input_shape: Any) -> None: ...
    # Real type here in _InputShapeT and _OutputShapeT. If Higher order kinds
    # existed we could derive these from the input and output types. Without them
    # we would need to make this class have more generic arguments. Overloads at least
    # handle one common case.
    @overload
    @abstractmethod
    def compute_output_shape(self, input_shape: Any) -> Any: ...
    @overload
    @abstractmethod
    def compute_output_shape(self: Layer[tf.Tensor, tf.Tensor], input_shape: tf.TensorShape) -> tf.TensorShape: ...
    def add_weight(
        self,
        name: str | None = None,
        shape: Iterable[int | None] | None = None,
        dtype: tf.DTypeLike | None = None,
        initializer: InitializerT | None = None,
        regularizer: tf.keras.regularizers.Regularizer | Callable[[tf.Tensor], tf.Tensor] | None = None,
        constraint: tf.keras.constraints.Constraint | Callable[[tf.Tensor], tf.Tensor] | None = None,
        trainable: bool | None = None,
    ) -> tf.Variable: ...
    @abstractmethod
    def call(self, inputs: _InputT) -> _OutputT: ...
    def count_params(self) -> int: ...
    @property
    def trainable_variables(self) -> list[Variable]: ...
    @property
    def non_trainable_variables(self) -> list[Variable]: ...
    @property
    def trainable_weights(self) -> list[Variable]: ...
    @property
    def non_trainable_weights(self) -> list[Variable]: ...
    @property
    def losses(self) -> list[Tensor]: ...
    built: bool
    def get_weights(self) -> list[np.ndarray[Any, np.dtype[np.float32]]]: ...
    def set_weights(self, weights: list[np.ndarray[Any, np.dtype[np.float32]]]) -> None: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class Dense(Layer[tf.Tensor, tf.Tensor]):
    input_spec: InputSpec
    def __init__(
        self,
        units: int,
        activation: ActivationT = None,
        use_bias: bool = True,
        kernel_initializer: InitializerT = "glorot_uniform",
        bias_initializer: InitializerT = "zeros",
        kernel_regularizer: RegularizerT = None,
        bias_regularizer: RegularizerT = None,
        activity_regularizer: RegularizerT = None,
        kernel_constraint: ConstraintT = None,
        bias_constraint: ConstraintT = None,
        name: str | None = None,
    ) -> None: ...
    def compute_output_shape(self, input_shape: tf.TensorShape) -> tf.TensorShape: ...
    def call(self, inputs: tf.Tensor) -> tf.Tensor: ...

class ReLU(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        max_value: float | None = None,
        negative_slope: float | None = 0.0,
        threshold: float | None = 0.0,
        name: str | None = None,
    ) -> None: ...
    def compute_output_shape(self, input_shape: tf.TensorShape) -> tf.TensorShape: ...
    def call(self, inputs: tf.Tensor) -> tf.Tensor: ...

class Dropout(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        rate: float,
        noise_shape: TensorCompatible | Sequence[int | None] | None = None,
        seed: int | None = None,
        name: str | None = None,
    ) -> None: ...
    def compute_output_shape(self, input_shape: tf.TensorShape) -> tf.TensorShape: ...
    def call(self, inputs: tf.Tensor) -> tf.Tensor: ...

def __getattr__(name: str) -> Any: ...
