from numpy.typing import NDArray

import numpy as np

from .._shared.utils import deprecate_kwarg

from ._util import (
    _offsets_to_raveled_neighbors,
    _resolve_neighborhood,
    _set_border_values,
)

@deprecate_kwarg(
    kwarg_mapping={"selem": "footprint"},
    removed_version="1.0",
    deprecated_version="0.19",
)
def flood_fill(
    image: NDArray,
    seed_point: tuple | int,
    new_value,
    *,
    footprint: NDArray | None = None,
    connectivity: int | None = None,
    tolerance: float | int | None = None,
    in_place: bool = False
) -> NDArray: ...
@deprecate_kwarg(
    kwarg_mapping={"selem": "footprint"},
    removed_version="1.0",
    deprecated_version="0.19",
)
def flood(
    image: NDArray,
    seed_point: tuple | int,
    *,
    footprint: NDArray | None = None,
    connectivity: int | None = None,
    tolerance: float | int | None = None
) -> NDArray: ...
