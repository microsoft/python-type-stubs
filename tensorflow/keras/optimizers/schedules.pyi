from typing import Any, Sequence
from typing_extensions import Self

from abc import ABC, abstractmethod

import tensorflow as tf

class LearningRateSchedule(ABC):
    @abstractmethod
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    @abstractmethod
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class PiecewiseConstantDecay(LearningRateSchedule):
    def __init__(
        self,
        boundaries: Sequence[tf.Tensor] | Sequence[float],
        values: Sequence[float] | Sequence[tf.Tensor],
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class InverseTimeDecay(LearningRateSchedule):
    def __init__(
        self,
        initial_learning_rate: float | tf.Tensor,
        decay_steps: int,
        decay_rate: float,
        staircase: bool = False,
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class PolynomialDecay(LearningRateSchedule):
    def __init__(
        self,
        initial_learning_rate: float | tf.Tensor,
        decay_steps: int,
        end_learning_rate: float | tf.Tensor,
        power: float = 1.0,
        cycle: bool = False,
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class CosineDecay(LearningRateSchedule):
    def __init__(
        self,
        initial_learning_rate: float | tf.Tensor,
        decay_steps: int,
        alpha: float | tf.Tensor = 0.0,
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class CosineDecayRestarts(LearningRateSchedule):
    def __init__(
        self,
        initial_learning_rate: float | tf.Tensor,
        decay_steps: int | tf.Tensor,
        t_mul: float | tf.Tensor = 1.0,
        m_mul: float | tf.Tensor = 1.0,
        alpha: float | tf.Tensor = 0.0,
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...

class ExponentialDecay(LearningRateSchedule):
    def __init__(
        self,
        initial_learning_rate: float | tf.Tensor,
        decay_steps: int | tf.Tensor,
        decay_rate: float | tf.Tensor,
        staircase: bool = False,
        name: str | None = None,
    ) -> None: ...
    def __call__(self, step: int | tf.Tensor) -> float | tf.Tensor: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...
