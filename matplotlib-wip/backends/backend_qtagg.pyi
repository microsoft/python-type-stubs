from .backend_agg import FigureCanvasAgg
from .backend_qt import FigureCanvasQT, _BackendQT

class FigureCanvasQTAgg(FigureCanvasAgg, FigureCanvasQT):
    def __init__(self, figure=...) -> None: ...
    def paintEvent(self, event): ...
    def print_figure(self, *args, **kwargs): ...

class _BackendQTAgg(_BackendQT):
    FigureCanvas = FigureCanvasQTAgg
