from typing import Any, Callable

from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase

class PlotSurface(PlotModeBase):
    default_rot_preset = ...
    def calculate_one_cvert(self, u, v) -> Any:
        ...
    
    def draw_verts(self, use_cverts, use_solid_color) -> Callable[[], None]:
        ...
    


