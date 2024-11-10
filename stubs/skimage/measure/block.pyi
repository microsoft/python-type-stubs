from typing import Callable, Mapping

from numpy.typing import NDArray

def block_reduce(
    image: NDArray,
    block_size=2,
    func: Callable = ...,
    cval: float = 0,
    func_kwargs: Mapping | None = None,
) -> NDArray: ...
