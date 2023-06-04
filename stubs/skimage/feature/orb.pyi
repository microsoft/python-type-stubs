import numpy as np

from ..feature.util import (
    FeatureDetector,
    DescriptorExtractor,
    _mask_border_keypoints,
    _prepare_grayscale_input_2D,
)

from ..feature import corner_fast, corner_orientations, corner_peaks, corner_harris
from ..transform import pyramid_gaussian
from .._shared.utils import check_nD

OFAST_MASK = ...
OFAST_UMAX: list = ...

class ORB(FeatureDetector, DescriptorExtractor):
    def __init__(
        self,
        downscale: float = 1.2,
        n_scales: int = 8,
        n_keypoints: int = 500,
        fast_n: int = 9,
        fast_threshold: float = 0.08,
        harris_k: float = 0.04,
    ): ...
    def _build_pyramid(self, image): ...
    def _detect_octave(self, octave_image): ...
    def detect(self, image): ...
    def _extract_octave(self, octave_image, keypoints, orientations): ...
    def extract(self, image, keypoints, scales, orientations): ...
    def detect_and_extract(self, image): ...
