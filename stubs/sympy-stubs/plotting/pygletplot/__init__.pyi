from sympy.utilities.decorator import doctest_depends_on

@doctest_depends_on(modules=("pyglet",))
def PygletPlot(*args, **kwargs) -> PygletPlot: ...
