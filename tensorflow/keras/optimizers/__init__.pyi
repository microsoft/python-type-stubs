from __future__ import annotations

from typing import Any, Callable, Iterable
from typing_extensions import Self, TypeAlias

from abc import ABC

import tensorflow as tf
from tensorflow.keras.optimizers import schedules as schedules

_InitializerT = str | Callable[[], tf.Tensor] | dict[str, Any]
_ShapeT: TypeAlias = tf.TensorShape | Iterable[int | None]
_DtypeT: TypeAlias = tf.DType | str | None
_GradientsT: TypeAlias = tf.Tensor | tf.IndexedSlices

class Optimizer(ABC):
    @property
    def name(self) -> str: ...
    def __init__(self, *args: object, **kwargs: object) -> None: ...
    def add_slot(
        self,
        var: tf.Variable,
        slot_name: str,
        initializer: _InitializerT = "zeros",
        shape: tf.TensorShape | None = None,
    ) -> tf.Variable: ...
    def add_weight(
        self,
        name: str,
        shape: _ShapeT,
        dtype: _DtypeT = None,
        trainable: None | bool = None,
        synchronization: tf.VariableSynchronization = tf.VariableSynchronization.AUTO,
        aggregation: tf.VariableAggregation = tf.VariableAggregation.NONE,
    ) -> tf.Variable: ...
    def apply_gradients(
        self,
        grads_and_vars: Iterable[tuple[_GradientsT, tf.Variable]],
        name: str | None = None,
        experimental_aggregate_gradients: bool = True,
    ) -> tf.Operation: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any], custom_objects: dict[str, type] | None = None) -> Self: ...
    def get_config(self) -> dict[str, Any]: ...
    def get_slot(self, var: tf.Variable, slot_name: str) -> tf.Variable: ...
    def get_slot_names(self) -> list[str]: ...
    def get_gradients(self, loss: tf.Tensor, params: list[tf.Variable]) -> list[tf.Tensor]: ...
    def minimize(
        self,
        loss: tf.Tensor | Callable[[], tf.Tensor],
        var_list: list[tf.Variable]
        | tuple[tf.Variable, ...]
        | Callable[[], list[tf.Variable] | tuple[tf.Variable, ...]],
        grad_loss: tf.Tensor | None = None,
        name: str | None = None,
        tape: tf.GradientTape | None = None,
    ) -> tf.Operation: ...
    def variables(self) -> list[tf.Variable]: ...

class Adam(Optimizer):
    def __init__(
        self,
        learning_rate: float = 0.001,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-07,
        amsgrad: bool = False,
        name: str | None = "Adam",
    ) -> None: ...

class Adagrad(Optimizer): ...
