from matplotlib.transforms import Bbox
from .backend_agg import FigureCanvasAgg
from ._backend_tk import FigureCanvasTk, _BackendTk

class FigureCanvasTkAgg(FigureCanvasAgg, FigureCanvasTk):
    def draw(self): ...
    def blit(self, bbox: Bbox = ...): ...

class _BackendTkAgg(_BackendTk):
    FigureCanvas = FigureCanvasTkAgg
