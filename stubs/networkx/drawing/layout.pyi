from typing import Mapping
from numpy.typing import ArrayLike
from ..classes.graph import Graph
from ..utils import np_random_state

__all__ = [
    "bipartite_layout",
    "circular_layout",
    "kamada_kawai_layout",
    "random_layout",
    "rescale_layout",
    "rescale_layout_dict",
    "shell_layout",
    "spring_layout",
    "spectral_layout",
    "planar_layout",
    "fruchterman_reingold_layout",
    "spiral_layout",
    "multipartite_layout",
]

@np_random_state(3)
def random_layout(
    G: Graph, center: ArrayLike | None = None, dim: int = 2, seed=None
) -> Mapping: ...
def circular_layout(
    G: Graph, scale=1, center: ArrayLike | None = None, dim: int = 2
) -> Mapping: ...
def shell_layout(
    G: Graph,
    nlist=None,
    rotate=None,
    scale=1,
    center: ArrayLike | None = None,
    dim: int = 2,
) -> Mapping: ...
def bipartite_layout(
    G: Graph,
    nodes,
    align="vertical",
    scale=1,
    center: ArrayLike | None = None,
    aspect_ratio=...,
) -> Mapping: ...
@np_random_state(10)
def spring_layout(
    G: Graph,
    k=None,
    pos=None,
    fixed=None,
    iterations=50,
    threshold=1e-4,
    weight="weight",
    scale=1,
    center: ArrayLike | None = None,
    dim: int = 2,
    seed=None,
) -> Mapping: ...

fruchterman_reingold_layout = ...

def kamada_kawai_layout(
    G: Graph,
    dist=None,
    pos=None,
    weight="weight",
    scale=1,
    center: ArrayLike | None = None,
    dim: int = 2,
) -> Mapping: ...
def spectral_layout(
    G: Graph, weight="weight", scale=1, center: ArrayLike | None = None, dim: int = 2
) -> Mapping: ...
def planar_layout(
    G: Graph, scale=1, center: ArrayLike | None = None, dim: int = 2
) -> Mapping: ...
def spiral_layout(
    G: Graph,
    scale=1,
    center: ArrayLike | None = None,
    dim: int = 2,
    resolution: float = 0.35,
    equidistant: bool = False,
) -> Mapping: ...
def multipartite_layout(
    G: Graph,
    subset_key="subset",
    align="vertical",
    scale=1,
    center: ArrayLike | None = None,
) -> Mapping: ...
def rescale_layout(pos, scale=1): ...
def rescale_layout_dict(pos, scale=1): ...
