from sympy.utilities.decorator import doctest_depends_on
from sympy.plotting.pygletplot.plot import PygletPlot as Plot

@doctest_depends_on(modules=('pyglet', ))
def PygletPlot(*args, **kwargs) -> PygletPlot:
    ...

