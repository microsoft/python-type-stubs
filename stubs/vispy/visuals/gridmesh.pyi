from numpy.typing import NDArray

from .mesh import MeshVisual
from ..geometry import create_grid_mesh, MeshData

class GridMeshVisual(MeshVisual):
    def __init__(
        self, xs: NDArray, ys: NDArray, zs: NDArray, colors: NDArray | None = None, shading: str | None = "smooth", **kwargs
    ): ...
    def set_data(
        self,
        xs: NDArray | None = None,
        ys: NDArray | None = None,
        zs: NDArray | None = None,
        colors: NDArray | None = None,
    ): ...
