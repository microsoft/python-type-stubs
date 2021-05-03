from typing import Any

from matplotlib._typing import ArrayLike


class TransformNode:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class BboxBase(TransformNode):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Bbox(BboxBase):
    def __init__(self, points: ArrayLike, **kwargs: Any) -> None: ...

    @staticmethod
    def from_bounds(x0: int, y0: int, width: int, height: int) -> Bbox: ...

    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Transform(TransformNode):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Affine2D:
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
