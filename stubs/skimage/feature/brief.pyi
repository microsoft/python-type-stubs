from typing import Literal

from .util import DescriptorExtractor

class BRIEF(DescriptorExtractor):
    def __init__(
        self,
        descriptor_size: int = 256,
        patch_size: int = 49,
        mode: Literal["normal", "uniform"] = "normal",
        sigma: float = 1,
        sample_seed=1,
    ): ...
    def extract(self, image, keypoints): ...
