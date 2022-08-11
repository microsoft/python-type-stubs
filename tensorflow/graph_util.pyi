from typing import Mapping, overload

from tensorflow import Operation, Tensor
from tensorflow.compat.v1 import GraphDef

@overload
def import_graph_def(
    graph_def: GraphDef,
    input_map: Mapping[str, Tensor] | None,
    return_elements: list[str],
    name: str | None = None,
) -> list[Operation | Tensor]: ...
@overload
def import_graph_def(
    graph_def: GraphDef,
    *,
    return_elements: list[str],
    name: str | None = None,
) -> list[Operation | Tensor]: ...
@overload
def import_graph_def(
    graph_def: GraphDef,
    input_map: Mapping[str, Tensor] | None = None,
    return_elements: None = None,
    name: str | None = None,
) -> None: ...
