import matplotlib
import numpy as np
from pandas.core.series import Series
from pandas.core.frame import DataFrame
from typing import Any, Dict, Optional, Sequence, Tuple, Union

def table(ax, data, rowLabels=None, colLabels=None,) -> Any: ... 
def register() -> None: ...
def deregister() -> None: ...
def scatter_matrix(
    frame: DataFrame,
    alpha: float = ...,
    figsize: Optional[Tuple[float, float]] = ...,
    ax: Optional[matplotlib.axes.Axes] = ...,
    grid: bool = ...,
    diagonal: str = ...,
    marker: str = ...,
    density_kwds: Any = ...,
    hist_kwds: Any = ...,
    range_padding: float = ...,
) -> np.ndarray: ...
def radviz(
    frame: DataFrame,
    class_column: str,
    ax: Optional[matplotlib.axes.Axes] = ...,
    color: Optional[Union[Sequence[str], Tuple[str]]] = ...,
    colormap: Any = ...,
) -> matplotlib.axes.Axes: ...
def andrews_curves(
    frame: DataFrame,
    class_column: str,
    ax: Optional[matplotlib.axes.Axes] = ...,
    samples: int = ...,
    color: Optional[Union[Sequence[str], Tuple[str]]] = ...,
    colormap: Any = ...,
) -> matplotlib.axes.Axes: ...
def bootstrap_plot(
    series: Series, fig: Optional[matplotlib.pyplot.Figure] = ..., size: int = ..., samples: int = ...,
) -> matplotlib.pyplot.Figure: ...
def parallel_coordinates(
    frame: DataFrame,
    class_column: str,
    cols: Optional[Sequence[str]] = ...,
    ax: Optional[matplotlib.axes.Axes] = ...,
    color: Optional[Union[Sequence[str], Tuple[str]]] = ...,
    use_columns: bool = ...,
    xticks: Optional[Union[Sequence, Tuple]] = ...,
    colormap: Any = ...,
    axvlines: bool = ...,
    axvlines_kwds: Any = ...,
    sort_labels: bool = ...,
) -> matplotlib.axes.Axes: ...
def lag_plot(series: Series, lag: int = ..., ax: Optional[matplotlib.axes.Axes] = ...,) -> matplotlib.axes.Axes: ...
def autocorrelation_plot(series: Series, ax: Optional[matplotlib.axes.Axes] = ...,) -> matplotlib.axes.Axes: ...

class _Options(dict):
    def __init__(self, deprecated: bool = ...) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any): ...
    def __delitem__(self, key: Any): ...
    def __contains__(self, key: Any) -> bool: ...
    def reset(self) -> None: ...
    def use(self, key: Any, value: Any) -> None: ...

plot_params: Dict[str, Any]
