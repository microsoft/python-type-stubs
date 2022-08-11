from typing import Any, Mapping, MutableSequence, Sequence, overload
from typing_extensions import Self

from types import TracebackType

from google.protobuf.message import Message

import numpy as np

import tensorflow as tf
from tensorflow.compat.v1 import graph_util as graph_util
from tensorflow.compat.v1 import saved_model as saved_model

from bento.utils.tensor_types import FloatDataSequence

# Would be better to use mypy-protobuf to make this.
class GraphDef(Message):
    node: MutableSequence[NodeDef]
    def __getattr__(self, name: str) -> Any: ...

class MetaGraphDef(Message): ...

class NodeDef(Message):
    name: str
    op: str
    input: MutableSequence[str]
    def __getattr__(self, name: str) -> Any: ...

class RunOptions(Message): ...
class RunMetadata(Message): ...

_GraphElement = tf.Tensor | tf.SparseTensor | tf.Operation | str
_FeedElement = float | str | np.ndarray[Any, Any] | FloatDataSequence
# This is a simplification. Key being invariant in a Mapping makes the real type difficult to write. This
# is enough to cover vast majority of use cases.
_FeedDict = Mapping[str, _FeedElement] | Mapping[tf.Tensor, _FeedElement] | Mapping[tf.SparseTensor, _FeedElement]

class Session:
    graph: tf.Graph
    graph_def: GraphDef
    def __init__(
        self,
        *,
        graph: tf.Graph | None = None,
    ) -> None: ...
    @overload
    def run(
        self,
        fetches: _GraphElement,
        feed_dict: _FeedDict | None = None,
        options: RunOptions | None = None,
        run_metadata: RunMetadata | None = None,
    ) -> np.ndarray[Any, Any]: ...
    @overload
    def run(
        self,
        fetches: Sequence[_GraphElement],
        feed_dict: _FeedDict | None = None,
        options: RunOptions | None = None,
        run_metadata: RunMetadata | None = None,
    ) -> list[np.ndarray[Any, Any]]: ...
    @overload
    def run(
        self,
        fetches: Mapping[str, _GraphElement],
        feed_dict: _FeedDict | None = None,
        options: RunOptions | None = None,
        run_metadata: RunMetadata | None = None,
    ) -> dict[str, np.ndarray[Any, Any]]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

def disable_eager_execution() -> None: ...
def disable_v2_behavior() -> None: ...
def global_variables_initializer() -> tf.Operation: ...
def tables_initializer() -> tf.Operation: ...
def get_default_graph() -> tf.Graph: ...
def __getattr__(name: str) -> Any: ...
