from typing import Any, Callable

from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase

class PlotCurve(PlotModeBase):
    style_override = ...
    def calculate_one_cvert(self, t) -> Any:
        ...
    
    def draw_verts(self, use_cverts) -> Callable[[], None]:
        ...
    


