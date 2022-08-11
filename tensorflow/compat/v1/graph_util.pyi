from typing import Iterable

from tensorflow.compat.v1 import GraphDef, Session

def extract_sub_graph(graph_def: GraphDef, dest_nodes: Iterable[str]) -> GraphDef: ...
def convert_variables_to_constants(
    sess: Session,
    input_graph_def: GraphDef,
    output_node_names: Iterable[str],
    variable_names_whitelist: Iterable[str] | None = None,
    variable_names_blacklist: Iterable[str] | None = None,
) -> GraphDef: ...
