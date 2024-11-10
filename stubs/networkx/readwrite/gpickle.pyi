__all__ = ["read_gpickle", "write_gpickle"]


from ..classes.graph import Graph

def write_gpickle(G: Graph, path, protocol=...): ...
def read_gpickle(path): ...
