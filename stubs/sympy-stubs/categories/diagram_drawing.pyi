from typing import Any
from sympy.utilities.decorator import doctest_depends_on

__doctest_requires__ = ...
class _GrowableGrid:
    def __init__(self, width, height) -> None:
        ...
    
    @property
    def width(self) -> Any:
        ...
    
    @property
    def height(self) -> Any:
        ...
    
    def __getitem__(self, i_j):
        ...
    
    def __setitem__(self, i_j, newvalue) -> None:
        ...
    
    def append_row(self) -> None:
        ...
    
    def append_column(self) -> None:
        ...
    
    def prepend_row(self) -> None:
        ...
    
    def prepend_column(self) -> None:
        ...
    


class DiagramGrid:
    def __init__(self, diagram, groups=..., **hints) -> None:
        ...
    
    @property
    def width(self):
        ...
    
    @property
    def height(self):
        ...
    
    def __getitem__(self, i_j):
        ...
    
    @property
    def morphisms(self) -> dict[Any, Any]:
        ...
    
    def __str__(self) -> str:
        ...
    


class ArrowStringDescription:
    def __init__(self, unit, curving, curving_amount, looping_start, looping_end, horizontal_direction, vertical_direction, label_position, label) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class XypicDiagramDrawer:
    def __init__(self) -> None:
        ...
    
    def draw(self, diagram, grid, masked=..., diagram_format=...):
        ...
    


def xypic_draw_diagram(diagram, masked=..., diagram_format=..., groups=..., **hints):
    ...

@doctest_depends_on(exe=('latex', 'dvipng'), modules=('pyglet', ))
def preview_diagram(diagram, masked=..., diagram_format=..., groups=..., output=..., viewer=..., euler=..., **hints) -> None:
    ...

