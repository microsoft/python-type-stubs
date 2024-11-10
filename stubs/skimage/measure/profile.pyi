from typing import Callable, Literal

from numpy.typing import ArrayLike

def profile_line(
    image,
    src,
    dst,
    linewidth: int = 1,
    order=None,
    mode: Literal["constant", "nearest", "reflect", "mirror", "wrap"] = "reflect",
    cval: float = 0.0,
    *,
    reduce_func: Callable = ...,
) -> ArrayLike: ...
def _line_profile_coordinates(src, dst, linewidth=1): ...
