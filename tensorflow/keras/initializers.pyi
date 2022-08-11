# TODO: Fill in remaining initializers
from typing import Any, overload
from typing_extensions import Self

import numpy as np

from tensorflow import DTypeLike, ShapeLike, Tensor, TensorCompatible

from bento.arguments import Config

class Initializer:
    def __call__(self, shape: ShapeLike, dtype: DTypeLike | None = None) -> Tensor: ...
    def get_config(self) -> dict[str, Config]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Config]) -> Self: ...

class Constant(Initializer):
    def __init__(self, value: TensorCompatible) -> None: ...

class GlorotNormal(Initializer):
    def __init__(self, seed: int | None = None) -> None: ...

class GlorotUniform(Initializer):
    def __init__(self, seed: int | None = None) -> None: ...

class TruncatedNormal(Initializer):
    def __init__(self, mean: TensorCompatible = 0.0, stddev: TensorCompatible = 0.05, seed: int | None = None): ...

class Zeros(Initializer):
    def __init__(self) -> None: ...

constant = Constant
glorot_normal = GlorotNormal
glorot_uniform = GlorotUniform
truncated_normal = TruncatedNormal
zeros = Zeros

InitializerT = str | Initializer | dict[str, Any] | None

@overload
def get(identifier: None) -> None: ...
@overload
def get(identifier: str | Initializer | dict[str, Any]) -> Initializer: ...
def __getattr__(name: str) -> Any: ...
