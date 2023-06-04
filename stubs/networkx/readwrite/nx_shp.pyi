import warnings

from ..classes.graph import Graph

__all__ = ["read_shp", "write_shp"]

def read_shp(
    path, simplify: bool = True, geom_attrs: bool = True, strict: bool = True
): ...
def edges_from_line(geom, attrs, simplify=True, geom_attrs=True): ...
def write_shp(G: Graph, outdir): ...
