import sys
from collections.abc import Iterator

from numpy.typing import NDArray

from .._shared import utils

def _texture_filter(gaussian_filtered): ...
def _singlescale_basic_features_singlechannel(img, sigma, intensity=True, edges=True, texture=True): ...

if sys.version_info >= (3, 11):
    def _mutiscale_basic_features_singlechannel(
        img: NDArray,
        intensity: bool = True,
        edges: bool = True,
        texture: bool = True,
        sigma_min: float = 0.5,
        sigma_max: float = 16,
        num_sigma: int | None = None,
        workers: int | None = None,
    ) -> Iterator[NDArray]: ...
else:
    def _mutiscale_basic_features_singlechannel(
        img: NDArray,
        intensity: bool = True,
        edges: bool = True,
        texture: bool = True,
        sigma_min: float = 0.5,
        sigma_max: float = 16,
        num_sigma: int | None = None,
        num_workers: int | None = None,
    ) -> Iterator[NDArray]: ...

@utils.deprecate_multichannel_kwarg(multichannel_position=1)
def multiscale_basic_features(
    image: NDArray,
    multichannel: bool = False,
    intensity: bool = True,
    edges: bool = True,
    texture: bool = True,
    sigma_min: float = 0.5,
    sigma_max: float = 16,
    num_sigma: int | None = None,
    num_workers: int | None = None,
    *,
    channel_axis: int | None = None,
): ...
