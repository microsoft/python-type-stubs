from typing import Callable

from sympy.plotting.pygletplot.plot_curve import PlotCurve
from sympy.plotting.pygletplot.plot_surface import PlotSurface

def float_vec3(f) -> Callable[..., tuple[float, float, float]]:
    ...

class Cartesian2D(PlotCurve):
    intervals = ...
    aliases = ...
    is_default = ...


class Cartesian3D(PlotSurface):
    intervals = ...
    aliases = ...
    is_default = ...


class ParametricCurve2D(PlotCurve):
    intervals = ...
    aliases = ...
    is_default = ...


class ParametricCurve3D(PlotCurve):
    intervals = ...
    aliases = ...
    is_default = ...


class ParametricSurface(PlotSurface):
    intervals = ...
    aliases = ...
    is_default = ...


class Polar(PlotCurve):
    intervals = ...
    aliases = ...
    is_default = ...


class Cylindrical(PlotSurface):
    intervals = ...
    aliases = ...
    is_default = ...


class Spherical(PlotSurface):
    intervals = ...
    aliases = ...
    is_default = ...


