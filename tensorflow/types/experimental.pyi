from typing import Generic, TypeVar
from typing_extensions import ParamSpec

import tensorflow as tf

P = ParamSpec("P")
R = TypeVar("R", covariant=True)

class Callable(Generic[P, R]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...

# This is a real tensorflow class, but it's undocumented. ConcreteFunction
# heavily wraps this class.
class _FuncGraph(tf.Graph):
    name: str
    inputs: list[tf.Tensor]
    outputs: list[tf.Tensor]
    control_outputs: list[tf.Operation]
    structured_input_signature: tuple[tuple[tf.TensorSpec, ...], dict[str, tf.TensorSpec]]
    seed: int | None

class GenericFunction(Callable[P, R]):
    def get_concrete_function(self, *args: P.args, **kwargs: P.kwargs) -> ConcreteFunction[P, R]: ...

class ConcreteFunction(Callable[P, R]):
    @property
    def structured_input_signature(self) -> tuple[tuple[tf.TensorSpec, ...], dict[str, tf.TensorSpec]]: ...
    @property
    def graph(self) -> _FuncGraph: ...
    @property
    def inputs(self) -> list[tf.Tensor]: ...
    @property
    def outputs(self) -> list[tf.Tensor]: ...
