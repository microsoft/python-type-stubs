from collections.abc import Mapping
from numbers import Number

from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..drawing.layout import (
    circular_layout,
    kamada_kawai_layout,
    planar_layout,
    random_layout,
    shell_layout,
    spectral_layout,
    spring_layout,
)

__all__ = [
    "draw",
    "draw_networkx",
    "draw_networkx_nodes",
    "draw_networkx_edges",
    "draw_networkx_labels",
    "draw_networkx_edge_labels",
    "draw_circular",
    "draw_kamada_kawai",
    "draw_random",
    "draw_spectral",
    "draw_spring",
    "draw_planar",
    "draw_shell",
]

def draw(G: Graph, pos: Mapping | None = None, ax=None, **kwds): ...
def draw_networkx(G: Graph, pos: Mapping | None = None, arrows=None, with_labels=True, **kwds): ...
def draw_networkx_nodes(
    G: Graph,
    pos: Mapping,
    nodelist=None,
    node_size=300,
    node_color="#1f78b4",
    node_shape="o",
    alpha=None,
    cmap=None,
    vmin=None,
    vmax=None,
    ax=None,
    linewidths=None,
    edgecolors=None,
    label=None,
    margins=None,
): ...
def draw_networkx_edges(
    G: Graph,
    pos: Mapping,
    edgelist=None,
    width=1.0,
    edge_color="k",
    style="solid",
    alpha=None,
    arrowstyle=None,
    arrowsize=10,
    edge_cmap=None,
    edge_vmin: float | None = None,
    edge_vmax: float | None = None,
    ax=None,
    arrows=None,
    label: str | None = None,
    node_size=300,
    nodelist=None,
    node_shape="o",
    connectionstyle="arc3",
    min_source_margin=0,
    min_target_margin=0,
): ...
def draw_networkx_labels(
    G: Graph,
    pos: Mapping,
    labels=None,
    font_size=12,
    font_color="k",
    font_family="sans-serif",
    font_weight="normal",
    alpha=None,
    bbox=None,
    horizontalalignment="center",
    verticalalignment="center",
    ax=None,
    clip_on=True,
) -> Mapping: ...
def draw_networkx_edge_labels(
    G: Graph,
    pos: Mapping,
    edge_labels=None,
    label_pos=0.5,
    font_size=10,
    font_color="k",
    font_family="sans-serif",
    font_weight="normal",
    alpha=None,
    bbox=None,
    horizontalalignment="center",
    verticalalignment="center",
    ax=None,
    rotate=True,
    clip_on=True,
) -> Mapping: ...
def draw_circular(G: Graph, **kwargs): ...
def draw_kamada_kawai(G: Graph, **kwargs): ...
def draw_random(G: Graph, **kwargs): ...
def draw_spectral(G: Graph, **kwargs): ...
def draw_spring(G: Graph, **kwargs): ...
def draw_shell(G: Graph, nlist=None, **kwargs): ...
def draw_planar(G: Graph, **kwargs): ...
def apply_alpha(
    colors,
    alpha: float | ArrayLike,
    elem_list,
    cmap=None,
    vmin: float | None = None,
    vmax: float | None = None,
): ...
