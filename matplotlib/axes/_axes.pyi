from datetime import tzinfo
from typing import (Any, BinaryIO, Callable, ContextManager, Dict, List,
                    Literal, Mapping, Optional, Sequence, Tuple, Type, Union,
                    overload)

from matplotlib._typing import ArrayLike, Scalar, _DetrendCallable, ndarray
from matplotlib.artist import Artist
from matplotlib.axes._base import _AxesBase
from matplotlib.axes._subplots import SubplotBase
from matplotlib.backend_bases import Event, FigureManagerBase
from matplotlib.cm import Colormap, ScalarMappable
from matplotlib.collections import (BrokenBarHCollection, Collection,
                                    EventCollection, LineCollection,
                                    PathCollection, PolyCollection, QuadMesh)
from matplotlib.colorbar import Colorbar
from matplotlib.colors import Normalize, _ColorLike
from matplotlib.container import BarContainer, ErrorbarContainer, StemContainer
from matplotlib.contour import ContourSet, QuadContourSet
from matplotlib.figure import Figure
from matplotlib.image import AxesImage, FigureImage
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
from matplotlib.patches import FancyArrow, Polygon, Wedge
from matplotlib.quiver import Barbs, Quiver, QuiverKey
from matplotlib.streamploy import StreamplotSet
from matplotlib.table import Table
from matplotlib.text import Annotation, Text
from matplotlib.transforms import Bbox
from matplotlib.widgets import SubplotTool
from PIL.Image import Image


class Axes(_AxesBase):
    # TODO: Most methods on Axes are the same as pyplot
    # (as pyplot is just global functions onto a shared Axes).
    # Mirror those here.
    
    # TODO: Many of these methods are actually defined on _AxesBase.

    transData: Any  # TODO
    transAxis: Any  # TODO

    def __init__(
        self,
        fig: Figure,
        rect: Union[Bbox, Sequence[int]],
        facecolor: Optional[_ColorLike] = ...,
        frameon: bool = ...,
        sharex: Optional[Axes] = ...,
        sharey: Optional[Axes] = ...,
        label: str = ...,
        xscale: Optional[str] = ...,
        yscale: Optional[str] = ...,
        box_aspect: Optional[float] = ...,
        **kwargs: Any
    ) -> None: ...

    def acorr(self, x: ArrayLike, *, data: Optional[Any] = ..., **kwargs: Any) -> Tuple[ndarray, ndarray, Union[LineCollection, Line2D], Optional[Line2D]]: ...

    add_artist: Any  # TODO
    add_callback: Any  # TODO
    add_child_axes: Any  # TODO
    add_collection: Any  # TODO
    add_container: Any  # TODO
    add_image: Any  # TODO
    add_line: Any  # TODO
    add_patch: Any  # TODO
    add_table: Any  # TODO

    def angle_spectrum(
        self,
        x: ArrayLike,
        Fs: Optional[Scalar] = ...,
        Fc: Optional[int] = ...,
        window: Optional[Union[Callable[[Any], Any], ndarray]] = ...,
        pad_to: Optional[int] = ...,
        sides: Optional[Literal["default", "onesides", "twosided"]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ArrayLike, ArrayLike, Line2D]: ...

    def annotate(self, s: str, xy: Tuple[float, float], *args: Any, **kwargs: Any) -> Annotation: ...

    def apply_aspect(self, position: Optional[ArrayLike] = ...) -> None: ...

    def arrow(self, x: float, y: float, dx: float, dy: float, **kwargs: Any) -> FancyArrow: ...

    def autoscale(self, enable: Optional[bool] = ..., axis: Optional[Literal["both", "x", "y"]] = ..., tight: Optional[bool] = ...) -> None: ...

    def autoscale_view(self, tight: Optional[bool] = ..., scalex: bool = ..., scaley: bool = ...) -> None: ...

    def axes(self, arg: Optional[Tuple[float, float, float, float]] = ..., **kwargs: Any) -> Axes: ...

    def axhline(self, y: Optional[Scalar] = ..., xmin: Optional[Scalar] = ..., xmax: Optional[Scalar] = ..., **kwargs: Any) -> Line2D: ...

    def axhspan(self, ymin: float, ymax: float, xmin: Optional[int] = ..., xmax: Optional[int] = ..., **kwargs: Any) -> Polygon: ...

    # TODO: write overloads for various forms
    def axis(self, *args: Any, **kwargs: Any) -> Tuple[float, float, float, float]: ...

    def axvline(self, x: Optional[Scalar] = ..., ymin: Optional[Scalar] = ..., ymax: Optional[Scalar] = ..., **kwargs: Any) -> Line2D: ...

    def axvspan(self, xmin: Scalar, xmax: Scalar, ymin: Optional[Scalar] = ..., ymax: Optional[Scalar] = ..., **kwargs: Any) -> Polygon: ...

    # Docs are misleading about this
    def bar(
        self,
        x: Union[Scalar, ArrayLike],
        height: Union[Scalar, ArrayLike],
        width: Optional[Union[Scalar, ArrayLike]] = ...,
        bottom: Optional[Union[Scalar, ArrayLike]] = ...,
        *,
        align: Literal["center", "edge"] = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> BarContainer: ...

    # TODO: write overloads for various forms
    def barbs(self, *args: Any, data: Optional[Any] = ..., **kwargs: Any) -> Barbs: ...

    def bar_label(
        self,
        container: BarContainer,
        labels: Optional[ArrayLike] = ...,
        *,
        fmt: str = ...,
        label_type: Literal['edge', 'center'] = ...,
        padding: float = ...,
        **kwargs: Any
    ) -> List[Text]: ...

    # barh is just bar, but x=left and bottom=y
    def barh(
        self,
        y: Union[Scalar, ArrayLike],
        width: Union[Scalar, ArrayLike],
        height: Optional[Union[Scalar, ArrayLike]] = ...,
        left: Optional[Union[Scalar, ArrayLike]] = ...,
        *,
        align: Literal["center", "edge"] = ...,
        **kwargs: Any
    ) -> BarContainer: ...

    def boxplot(
        self,
        x: Union[ArrayLike, Sequence[ArrayLike]],
        notch: Optional[bool] = ...,
        sym: Optional[str] = ...,
        vert: Optional[bool] = ...,
        whis: Optional[Union[float, ArrayLike, str]] = ...,
        positions: Optional[ArrayLike] = ...,
        widths: Optional[Union[Scalar, ArrayLike]] = ...,
        patch_artist: Optional[bool] = ...,
        bootstrap: Optional[int] = ...,
        usermedians: Optional[ArrayLike] = ...,
        conf_intervals: Optional[ArrayLike] = ...,
        meanline: Optional[bool] = ...,
        showmeans: Optional[bool] = ...,
        showcaps: Optional[bool] = ...,
        showbox: Optional[bool] = ...,
        showfliers: Optional[bool] = ...,
        boxprops: Optional[Dict[Any, Any]] = ...,
        labels: Optional[Sequence[Any]] = ...,
        flierprops: Optional[Any] = ...,
        medianprops: Optional[Dict[Any, Any]] = ...,
        meanprops: Optional[Dict[Any, Any]] = ...,
        capprops: Optional[Dict[Any, Any]] = ...,
        whiskerprops: Optional[Dict[Any, Any]] = ...,
        manage_ticks: Optional[bool] = ...,
        autorange: Optional[bool] = ...,
        zorder: Optional[Scalar] = ...,
        *,
        data: Optional[Any] = ...
    ) -> Dict[str, Line2D]: ...

    def broken_barh(self, xranges: Sequence[Tuple[float, float]], yrange: Tuple[float, float], *, data: Optional[Any] = ..., **kwargs: Any) -> BrokenBarHCollection: ...

    bxp: Any  # TODO
    can_pan: Any  # TODO
    can_zoom: Any  # TODO

    def cla(self) -> None: ...

    def clabel(self, CS: ContourSet, *args: Any, **kwargs: Any) -> List[Text]: ...

    def clim(self, vmin: Optional[float] = ..., vmax: Optional[float] = ...) -> None: ...

    def close(self, fig: Optional[Union[int, str, Figure]] = ...) -> None: ...

    def clear(self) -> None: ...

    def cohere(
        self,
        x: ArrayLike, y: ArrayLike,
        NFFT: int = ...,
        Fs: Scalar = ...,
        Fc: int = ...,
        detrend: Union[Literal["none", "mean", "linear"], _DetrendCallable] = ...,
        window: Union[Callable, ndarray] = ...,
        noverlap: int = ...,
        pad_to: Optional[int] = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: Optional[bool] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ndarray, ndarray]: ... # ArrayLike?

    contains: Any  # TODO
    contains_point: Any  # TODO

    # TODO: write overloads for various forms
    def contour(self, *args: Any, data: Optional[Any] = ..., **kwargs: Any) -> QuadContourSet: ...
    def contourf(self, *args: Any, data: Optional[Any] = ..., **kwargs: Any) -> QuadContourSet: ...

    convert_xunits: Any  # TODO
    convert_yunits: Any  # TODO

    def csd(
        self, 
        x: ArrayLike, y: ArrayLike,
        NFFT: int = ...,
        Fs: Scalar = ...,
        Fc: int = ...,
        detrend: Union[Literal["none", "mean", "linear"], _DetrendCallable] = ...,
        window: Union[Callable, ndarray] = ...,
        noverlap: int = ...,
        pad_to: Optional[int] = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: Optional[bool] = ...,
        return_line: Optional[bool] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ndarray, ndarray, Line2D]: ... # ArrayLike?

    drag_pan: Any  # TODO

    def draw(self) -> None: ...

    draw_artist: Any  # TODO
    end_pan: Any  # TODO

    def errorbar(
        self,
        x: ArrayLike, y: ArrayLike,
        yerr: Optional[Union[Scalar, ArrayLike]] = ...,
        xerr: Optional[Union[Scalar, ArrayLike]] = ...,
        fmt: str = ...,
        ecolor: Optional[_ColorLike] = ...,
        elinewidth: Optional[Scalar] = ...,
        capsize: Optional[Scalar] = ...,
        barsabove: bool = ...,
        lolims: bool = ...,
        uplims: bool = ...,
        xlolims: bool = ...,
        xuplims: bool = ...,
        errorevery: int = ...,
        capthick: Optional[Scalar] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> ErrorbarContainer: ...

    def eventplot(
        self,
        positions: ArrayLike,
        orientation: Optional[Literal["horizontal", "vertical"]],
        lineoffsets: Optional[Union[Scalar, ArrayLike]] = ...,
        linelengths: Optional[Union[Scalar, ArrayLike]] = ...,
        linewidths: Optional[Union[Scalar, ArrayLike]] = ...,
        colors: Optional[Union[_ColorLike, Sequence[_ColorLike]]] = ...,
        linestyles: Union[str, Tuple[str, ...], Sequence[Any]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> List[EventCollection]: ...

    # TODO: write overloads for various forms
    def fill(self, *args: Any, data: Optional[Mapping[Any, Any]] = ..., **kwargs: Any) -> List[Polygon]: ...

    def fill_between(
        self,
        x: ArrayLike, y1: ArrayLike,
        y2: Union[ArrayLike, Scalar] = ...,
        where: Optional[ArrayLike] = ...,
        interpolate: bool = ...,
        step: Optional[Literal["pre", "post", "mid"]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> PolyCollection: ...

    def fill_betweenx(
        self,
        y: ArrayLike, x1: ArrayLike,
        x2: Union[ArrayLike, Scalar] = ...,
        where: Optional[ArrayLike] = ...,
        interpolate: bool = ...,
        step: Optional[Literal["pre", "post", "mid"]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> PolyCollection: ...

    def findobj(
        self,
        o: Optional[Any] = ...,
        match: Optional[Union[
            Callable[[Artist], bool],
            Line2D,
        ]] = ...,
        include_self: bool = ...
    ) -> List[Artist]: ...

    get_adjustable: Any  # TODO
    get_agg_filter: Any  # TODO
    get_alpha: Any  # TODO
    get_anchor: Any  # TODO
    get_animated: Any  # TODO
    get_aspect: Any  # TODO
    get_autoscale_on: Any  # TODO
    get_autoscalex_on: Any  # TODO
    get_autoscaley_on: Any  # TODO
    get_axes_locator: Any  # TODO
    get_axisbelow: Any  # TODO
    get_box_aspect: Any  # TODO
    get_children: Any  # TODO
    get_clip_box: Any  # TODO
    get_clip_on: Any  # TODO
    get_clip_path: Any  # TODO
    get_contains: Any  # TODO
    get_cursor_data: Any  # TODO
    get_data_ratio: Any  # TODO
    get_default_bbox_extra_artists: Any  # TODO
    get_facecolor: Any  # TODO
    get_fc: Any  # TODO
    get_figure: Any  # TODO
    get_frame_on: Any  # TODO
    get_gid: Any  # TODO
    get_images: Any  # TODO
    get_in_layout: Any  # TODO
    get_label: Any  # TODO
    get_legend: Any  # TODO
    get_legend_handles_labels: Any  # TODO
    get_lines: Any  # TODO
    get_navigate: Any  # TODO
    get_navigate_mode: Any  # TODO
    get_path_effects: Any  # TODO
    get_picker: Any  # TODO
    get_position: Any  # TODO
    get_rasterization_zorder: Any  # TODO
    get_rasterized: Any  # TODO
    get_renderer_cache: Any  # TODO
    get_shared_x_axes: Any  # TODO
    get_shared_y_axes: Any  # TODO
    get_sketch_params: Any  # TODO
    get_snap: Any  # TODO
    get_tightbbox: Any  # TODO
    get_title: Any  # TODO
    get_transform: Any  # TODO
    get_transformed_clip_path_and_affine: Any  # TODO
    get_url: Any  # TODO
    get_visible: Any  # TODO
    get_window_extent: Any  # TODO
    get_xaxis: Any  # TODO
    get_xaxis_text1_transform: Any  # TODO
    get_xaxis_text2_transform: Any  # TODO
    get_xaxis_transform: Any  # TODO
    get_xbound: Any  # TODO
    get_xgridlines: Any  # TODO
    get_xlabel: Any  # TODO
    get_xlim: Any  # TODO
    get_xmajorticklabels: Any  # TODO
    get_xminorticklabels: Any  # TODO
    get_xscale: Any  # TODO
    get_xticklabels: Any  # TODO
    get_xticklines: Any  # TODO
    get_xticks: Any  # TODO
    get_yaxis: Any  # TODO
    get_yaxis_text1_transform: Any  # TODO
    get_yaxis_text2_transform: Any  # TODO
    get_yaxis_transform: Any  # TODO
    get_ybound: Any  # TODO
    get_ygridlines: Any  # TODO
    get_ylabel: Any  # TODO
    get_ylim: Any  # TODO
    get_ymajorticklabels: Any  # TODO
    get_yminorticklabels: Any  # TODO
    get_yscale: Any  # TODO
    get_yticklabels: Any  # TODO
    get_yticklines: Any  # TODO
    get_yticks: Any  # TODO
    get_zorder: Any  # TODO

    def grid(self, b: Optional[bool] = ..., which: Literal["major", "minor", "both"] = ..., axis: Literal["both", "x", "y"] = ..., **kwargs: Any): ...

    has_data: Any  # TODO
    have_units: Any  # TODO

    def hexbin(
        self,
        x: ArrayLike,
        y: ArrayLike,
        C: Optional[ArrayLike] = ...,
        gridsize: Union[int, Tuple[int, int]] = ...,
        bins: Optional[Union[Literal["log"], int, Sequence[Any]]] = ...,
        xscale: Literal["linear", "log"] = ...,
        yscale: Literal["linear", "log"] = ...,
        extent: Optional[float] = ...,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        vmin: Optional[float] = ...,
        vmax: Optional[float] = ...,
        alpha: Optional[float] = ...,
        linewidths: Optional[float] = ...,
        edgecolors: Optional[Union[Literal["face", "none"], _ColorLike]] = ...,
        reduce_C_function: Callable[[ArrayLike], float] = ...,
        mincnt: Optional[int] = ...,
        marginals: bool = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> PolyCollection: ...

    def hist(
        self,
        x: Union[ArrayLike, Sequence[ArrayLike]],
        bins: Optional[Union[int, str, Sequence[Any]]],
        range: Optional[Tuple] = ...,
        density: Optional[bool] = ...,
        weights: Optional[ArrayLike] = ...,
        cumulative: bool = ...,
        bottom: Optional[Union[ArrayLike, Scalar]] = ...,
        histtype: Literal["bar", "barstacked", "step", "stepfilled"] = ...,
        align: Literal["left", "mid", "right"] = ...,
        orientation: Literal["vertical", "horizontal"] = ...,
        rwidth: Optional[Scalar] = ...,
        log: bool = ...,
        color: Optional[Union[_ColorLike, Sequence[_ColorLike]]] = ...,
        label: Optional[str] = ...,
        stacked: bool = ...,
        normed: Optional[bool] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[Union[ArrayLike, List[ArrayLike]], ArrayLike, Union[List[Any], List[List[Any]]]]: ...

    def hist2d(
        self,
        x: ArrayLike, y: ArrayLike,
        bins: Optional[Union[
            int,
            Tuple[int, int],
            ArrayLike,
            Tuple[ArrayLike, ArrayLike],
        ]] = ...,
        range: Optional[ArrayLike] = ...,
        density: bool = ...,
        weights: Optional[ArrayLike] = ...,
        cmin: Optional[Scalar] = ...,
        cmax: Optional[Scalar] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ArrayLike, ArrayLike, ArrayLike, QuadMesh]: ...

    def hlines(
        self,
        y: Union[Scalar, ArrayLike],
        xmin: Union[Scalar, ArrayLike],
        xmax: Union[Scalar, ArrayLike],
        colors: _ColorLike = ...,
        linestyles: Literal['solid', 'dashed', 'dashdot', 'dotted'] = ...,
        label: str = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> LineCollection: ...

    def imshow(
        self,
        X: Union[ArrayLike, Image],
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        aspect: Optional[Union[Literal["equal", "auto"], float]] = ...,
        interpolation: Optional[str] = ...,
        alpha: Optional[Scalar] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        origin: Optional[Literal["upper", "lower"]] = ...,
        extent: Optional[Tuple[Scalar, Scalar, Scalar, Scalar]] = ...,
        shape: Any = ..., # deprecated
        filternorm: bool = ...,
        filterrad: float = ...,
        imlim: Any = ..., # deprecated
        resample: Optional[bool] = ...,
        url: Optional[str] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> AxesImage: ...

    imshow: Any  # TODO
    in_axes: Any  # TODO
    indicate_inset: Any  # TODO
    indicate_inset_zoom: Any  # TODO
    inset_axes: Any  # TODO
    invert_xaxis: Any  # TODO
    invert_yaxis: Any  # TODO
    is_transform_set: Any  # TODO

    # TODO: write overloads for various forms
    def legend(self, *args: Any, **kwargs: Any) -> Legend: ...

    def locator_params(self, axis: Optional[Literal["both", "x", "y"]] = ..., tight: Optional[bool] = ..., **kwargs: Any) -> None: ...

    # TODO: write overloads for various forms
    def loglog(self, *args: Any, **kwargs: Any) -> List[Line2D]: ...

    def magnitude_spectrum(
        self,
        x: ArrayLike,
        Fs: Optional[Scalar] = ...,
        Fc: Optional[int] = ...,
        window: Optional[Union[Callable[[Any], Any], ndarray]] = ...,
        pad_to: Optional[int] = ...,
        sides: Optional[Literal["default", "onesides", "twosided"]] = ...,
        scale: Optional[Literal["default", "linear", "dB"]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ArrayLike, ArrayLike, Line2D]: ...

    def margins(self, *margins: float, x: Optional[float] = ..., y: Optional[float] = ..., tight: Optional[bool] = ...) -> Tuple[float, float]: ...

    def matshow(self, A: ArrayLike, fignum: Optional[Union[int, Literal[False]]] = None, **kwargs: Any) -> AxesImage: ...

    def minorticks_off(self) -> None: ...

    def minorticks_on(self) -> None: ...

    mouseover: Any  # TODO
    name: Any  # TODO
    pchanged: Any  # TODO

    # TODO: write overloads for various forms
    def pcolor(
        self,
        *args: Any,
        alpha: Optional[Scalar] = ...,
        norm: Optional[Normalize] = ...,
        cmap: Optional[Union[str, Colormap]] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Collection: ...

    pcolorfast: Any  # TODO

    # TODO: write overloads for various forms
    def pcolormesh(
        self,
        *args: Any,
        alpha: Optional[Scalar] = ...,
        norm: Optional[Normalize] = ...,
        cmap: Optional[Union[str, Colormap]] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        shading: Literal["flat", "gouraud"] = ...,
        antialiased: Union[bool, Sequence[bool]] = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> QuadMesh: ...

    def phase_spectrum(
        self,
        x: ArrayLike,
        Fs: Optional[Scalar] = ...,
        Fc: Optional[int] = ...,
        window: Optional[Union[Callable[[Any], Any], ndarray]] = ...,
        pad_to: Optional[int] = ...,
        sides: Optional[Literal["default", "onesides", "twosided"]] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) ->  Tuple[ArrayLike, ArrayLike, Line2D]: ...

    pick: Any  # TODO
    pickable: Any  # TODO

    def pie(
        self,
        x: ArrayLike,
        explode: Optional[ArrayLike]= ...,
        labels: Optional[Sequence[str]] = ...,
        colors: Optional[Sequence[_ColorLike]] = ...,
        autopct: Optional[Union[str, Callable[..., str]]] = ...,
        pctdistance: float = ...,
        shadow: bool = ...,
        labeldistance: Optional[float] = ...,
        startangle: Optional[float] = ...,
        radius: Optional[float] = ...,
        counterclock: bool = ...,
        wedgeprops: Optional[Dict[Any, Any]] = ...,
        textprops: Optional[Dict[Any, Any]] = ...,
        center: Sequence[float] = ...,
        frame: bool = ...,
        rotatelabels: bool = ...,
        *,
        data: Optional[Any] = ...,
    ) -> Tuple[List[Wedge], List[Text], List[Text]]: ...

    # TODO: write overloads for various forms
    def plot(self, *args: Any, scalex: bool = ..., scaley: bool = ..., data: Optional[Any] = ..., **kwargs: Any) -> List[Line2D]: ...

    def plot_date(
        self,
        x: ArrayLike,
        y: ArrayLike,
        fmt: str = ...,
        tz: Optional[Union[str, tzinfo]] = ...,
        xdate: bool = ...,
        ydate: bool = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> List[Line2D]: ...

    properties: Any  # TODO

    def psd(
        self,
        x: ArrayLike,
        NFFT: int = ...,
        Fs: Scalar = ...,
        Fc: int = ...,
        detrend: Union[Literal["none", "mean", "linear"], _DetrendCallable] = ...,
        window: Union[Callable, ndarray] = ...,
        noverlap: int = ...,
        pad_to: Optional[int] = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: Optional[bool] = ...,
        return_line: Optional[bool] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ArrayLike, ArrayLike, Line2D]: ...

    # TODO: write overloads for various forms
    def quiver(self, *args: Any, data: Optional[Any] = ..., **kw: Any) -> Quiver: ...

    def quiverkey(self, Q: Quiver, X: float, Y: float, U: float, label: str, **kw: Any) -> QuiverKey: ...

    redraw_in_frame: Any  # TODO
    relim: Any  # TODO
    remove: Any  # TODO
    remove_callback: Any  # TODO
    reset_position: Any  # TODO

    def scatter(
        self,
        x: ArrayLike,
        y: ArrayLike,
        s: Optional[Union[Scalar, ArrayLike]] = ...,
        c: Optional[Union[_ColorLike, Sequence[float], Sequence[_ColorLike]]] = ...,
        marker: Optional[MarkerStyle] = ...,
        cmap: Optional[Colormap] = ...,
        norm: Optional[Normalize] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        alpha: Optional[Scalar] = ...,
        linewidths: Optional[Union[Scalar, ArrayLike]] = ...,
        verts: Optional[Any] = ..., # not documented?
        edgecolors: Optional[Union[Literal["face", "none"], _ColorLike, Sequence[_ColorLike]]] = ...,
        *,
        plotnonfinite: bool = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> PathCollection: ...
    
    secondary_xaxis: Any  # TODO
    secondary_yaxis: Any  # TODO

    # TODO: write overloads for various forms (below is a try at it)
    def semilogx(self, *args: Any, **kwargs: Any) -> List[Line2D]: ...

    # TODO: write overloads for various forms (below is a try at it)
    def semilogy(self, *args: Any, **kwargs: Any) -> List[Line2D]: ...

    set: Any  # TODO
    set_adjustable: Any  # TODO
    set_agg_filter: Any  # TODO
    set_alpha: Any  # TODO
    set_anchor: Any  # TODO
    set_animated: Any  # TODO
    set_aspect: Any  # TODO
    set_autoscale_on: Any  # TODO
    set_autoscalex_on: Any  # TODO
    set_autoscaley_on: Any  # TODO
    set_axes_locator: Any  # TODO
    set_axis_off: Any  # TODO
    set_axis_on: Any  # TODO
    set_axisbelow: Any  # TODO
    set_box_aspect: Any  # TODO
    set_clip_box: Any  # TODO
    set_clip_on: Any  # TODO
    set_clip_path: Any  # TODO
    set_contains: Any  # TODO
    set_facecolor: Any  # TODO
    set_fc: Any  # TODO
    set_figure: Any  # TODO
    set_frame_on: Any  # TODO
    set_gid: Any  # TODO
    set_in_layout: Any  # TODO
    set_label: Any  # TODO
    set_navigate: Any  # TODO
    set_navigate_mode: Any  # TODO
    set_path_effects: Any  # TODO
    set_picker: Any  # TODO
    set_position: Any  # TODO
    set_prop_cycle: Any  # TODO
    set_rasterization_zorder: Any  # TODO
    set_rasterized: Any  # TODO
    set_sketch_params: Any  # TODO
    set_snap: Any  # TODO
    set_title: Any  # TODO
    set_transform: Any  # TODO
    set_url: Any  # TODO
    set_visible: Any  # TODO
    set_xbound: Any  # TODO
    set_xlabel: Any  # TODO
    set_xlim: Any  # TODO
    set_xmargin: Any  # TODO
    set_xscale: Any  # TODO
    set_xticklabels: Any  # TODO
    set_xticks: Any  # TODO
    set_ybound: Any  # TODO
    set_ylabel: Any  # TODO
    set_ylim: Any  # TODO
    set_ymargin: Any  # TODO
    set_yscale: Any  # TODO
    set_yticklabels: Any  # TODO
    set_yticks: Any  # TODO
    set_zorder: Any  # TODO
    sharex: Any  # TODO
    sharey: Any  # TODO

    def specgram(
        self,
        x: ArrayLike,
        NFFT: int = ...,
        Fs: Scalar = ...,
        Fc: int = ...,
        detrend: Union[Literal["none", "mean", "linear"], _DetrendCallable] = ...,
        window: Union[Callable, ndarray] = ...,
        noverlap: int = ...,
        cmap: Optional[Colormap] = ...,
        xextent: Optional[Tuple[float, float]] = ...,
        pad_to: Optional[int] = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: Optional[bool] = ...,
        mode: Optional[Literal["default", "psd", "magnitude", "angle", "phase"]] = ...,
        scale: Optional[Literal["default", "linear", "dB"]] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ndarray, ndarray, ndarray, AxesImage]: ...

    def spy(
        self,
        Z: ArrayLike,
        precision: Union[float, Literal["present"]] = ...,
        marker: Optional[Any] = ...,  # TODO
        markersize: Optional[float] = ...,
        aspect: Optional[Union[Literal["equal", "auto"], float]] = ...,
        origin: Literal["upper", "lower"] = ...,
        **kwargs: Any
    ) -> Union[AxesImage, Line2D]: ...

    def stackplot(
        self,
        x: ArrayLike,
        *args: ArrayLike,
        labels: Sequence[str] = ...,
        colors: Optional[Sequence[_ColorLike]] = ...,
        baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> List[PolyCollection]: ...

    stairs: Any  # TODO
    stale: Any  # TODO
    start_pan: Any  # TODO

    # TODO: write overloads for various forms
    def stem(
        self,
        *args: ArrayLike,
        linefmt: Optional[str] = ...,
        markerfmt: Optional[str] = ...,
        basefmt: Optional[str] = ...,
        bottom: float = ...,
        label: Optional[str] = ...,
        use_line_collection: bool = ...,
        data: Optional[Any] = ...
    ) -> StemContainer: ...

    # TODO: write overloads for various forms
    def step(
        self,
        x: ArrayLike,
        y: ArrayLike,
        *args: Any,
        where: Literal["pre", "post", "mid"] = ...,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> List[Line2D]: ...

    sticky_edges: Any  # TODO

    def streamplot(
        self,
        x: ArrayLike,
        y: ArrayLike,
        u: ArrayLike,
        v: ArrayLike,
        density: Union[float, Tuple[float, float]] = ...,
        linewidth: Optional[Union[float, ArrayLike]] = ...,
        color: Optional[Union[_ColorLike, ArrayLike]] = ...,
        cmap: Optional[Colormap] = ...,
        norm: Optional[Normalize] = ...,
        arrowsize: float = ...,
        arrowstyle: str = ...,
        minlength: float = ...,
        transform: Optional[Any] = ..., # TODO: what is this?
        zorder: Optional[int] = ...,
        start_points: Optional[ArrayLike] = ...,
        maxlength: float = ...,
        integration_direction: Literal["forward", "backward", "both"] = ...,
        *,
        data: Optional[Any] = ...,
    ) -> StreamplotSet: ... # TODO: does this type exist?

    # TODO: resolve list vs sequence
    def table(
        self,
        cellText: Optional[Sequence[Sequence[str]]] = ...,
        cellColours: Optional[Sequence[Sequence[_ColorLike]]] = ...,
        cellLoc: Literal["left", "center", "right"] = ...,
        colWidths: Optional[Sequence[float]] = ...,
        rowLabels: Literal["left", "center", "right"] = ...,
        rowColours: Literal["left", "center", "right"] = ...,
        rowLoc: Literal["left", "center", "right"] = ...,
        colLabels: Literal["left", "center", "right"] = ...,
        colColours: Literal["left", "center", "right"] = ...,
        colLoc: Literal["left", "center", "right"] = ...,
        loc: str = ...,
        bbox: Optional[Bbox] = ...,
        edges: str = ..., # TODO: be more exact
        **kwargs: Any
    ) -> Table: ...

    def text(self, x: Scalar, y: Scalar, s: str, fontdict: Dict[Any, Any] = ..., withdash: Any = ..., **kwargs: Any) -> Text: ...

    def tick_params(self, axis: Literal["x", "y", "both"] = ..., **kwargs: Any) -> None: ...

    def ticklabel_format(
        self,
        *,
        axis: Literal["x", "y", "both"] = ...,
        style: str = ...,
        scilimits: Optional[Tuple[int, int]] = ...,
        useOffset: Optional[Union[bool, int]] = ...,
        useLocale: Optional[bool] = ...,
        useMathText: Optional[bool] = ...,
    ) -> None: ...

    # TODO: write overloads for various forms
    def tricontour(self, *args: Any, **kwargs: Any) -> None: ...

    # TODO: write overloads for various forms
    def tricontourf(self, *args: Any, **kwargs: Any) -> None: ...

    # TODO: write overloads for various forms
    def tripcolor(
        self,
        *args: Any,
        alpha: Optional[Scalar] = ...,
        norm: Optional[Normalize] = ...,
        cmap: Optional[Union[str, Colormap]] = ...,
        vmin: Optional[Scalar] = ...,
        vmax: Optional[Scalar] = ...,
        shading: Literal["flat", "gouraud"] = ...,
        facecolors: Optional[_ColorLike] = ..., # TODO: not sure if this is correct, the option is undocumented
        **kwargs: Any
    ) -> None: ...

    # TODO: write overloads for various forms
    def triplot(self, *args: Any, **kwargs: Any) -> List[Line2D]: ...

    def twinx(self, ax: Optional[Axes] = ...) -> Axes: ...
    def twiny(self, ax: Optional[Axes] = ...) -> Axes: ...

    update: Any  # TODO
    update_datalim: Any  # TODO
    update_datalim_bounds: Any  # TODO
    update_from: Any  # TODO
    use_sticky_edges: Any  # TODO
    viewLim: Any  # TODO
    violin: Any  # TODO

    def violinplot(
        self,
        dataset: ArrayLike,
        positions: Optional[ArrayLike] = ...,
        vert: bool = ...,
        widths: ArrayLike = ..., # Default is 0.5, which is "array-like" even though it's a scalar.
        showmeans: bool = ...,
        showextrema: bool = ...,
        showmedians: bool = ...,
        points: Scalar = ...,
        bw_method: Optional[Union[Literal["scott", "silverman"], Scalar, Callable]] = ...,
        *,
        data: Optional[Any] = ...,
    ) -> Dict[str, Any]: ... # TODO: TypedDict for this

    def vlines(
        self,
        x: Union[Scalar, ArrayLike],
        ymin: Union[Scalar, ArrayLike],
        ymax: Union[Scalar, ArrayLike],
        colors: Optional[Union[_ColorLike, Sequence[_ColorLike]]] = ..., # TODO: This may not be the right type for colors
        linestyles: Optional[Literal["solid", "dashed", "dashdot", "dotted"]] = ...,
        label: str = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> LineCollection: ...

    xaxis_date: Any  # TODO
    xaxis_inverted: Any  # TODO

    def xcorr(
        self,
        x: ArrayLike,
        y: ArrayLike,
        normed: bool = ...,
        detrend: _DetrendCallable = ...,
        usevlines: bool = ...,
        maxlags: int = ...,
        *,
        data: Optional[Any] = ...,
        **kwargs: Any
    ) -> Tuple[ndarray, ndarray, Union[LineCollection, Line2D], Optional[Line2D]]: ...

    yaxis_date: Any  # TODO
    yaxis_inverted: Any  # TODO
    zorder: Any  # TODO

    def __getattr__(self, name: str) -> Any: ...  # incomplete
