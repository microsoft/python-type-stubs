from vispy.util.svg.color import Color
from vispy.color.color_array import ColorArray
from numpy.typing import NDArray

from .mesh import MeshVisual
import numpy as np
from numpy.linalg import norm
from ..util.transforms import rotate
from ..color import ColorArray

import collections

class TubeVisual(MeshVisual):
    def __init__(
        self,
        points: NDArray,
        radius: NDArray | float = 1.0,
        closed: bool = False,
        color: ColorArray | Color | str = "purple",
        tube_points: int = 8,
        shading: str | None = "smooth",
        vertex_colors: NDArray | None = None,
        face_colors: NDArray | None = None,
        mode: str = "triangles",
    ): ...

def _frenet_frames(points, closed): ...
