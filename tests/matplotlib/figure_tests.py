from typing_extensions import assert_type

from matplotlib.axes import Axes
from matplotlib.figure import Figure

# ------------------------------- Figure.add_subplot() ------------------------------- #

# Returns an instance of `~.axes.Axes` if `projection`, `polar` and `axes_class` are
# left to defaults. Otherwise may return a subclass of `~.axes.Axes` depending on those
# keyword arguments.

fig = Figure()

# no arguments, defaults to (1, 1, 1)
ax = fig.add_subplot()
assert_type(ax, Axes)

# single 3-digit integer
ax = fig.add_subplot(235)
assert_type(ax, Axes)

# 3 integers
ax = fig.add_subplot(2, 3, 5)
assert_type(ax, Axes)

# index as tuple
ax = fig.add_subplot(3, 1, (1, 2))
assert_type(ax, Axes)
