from typing import Any, ClassVar
from typing_extensions import disjoint_base

__reduce_cython__: Any
__setstate_cython__: Any
__test__: dict

@disjoint_base
class Cascade:
    __pyx_vtable__: ClassVar[Any] = ...
    eps: Any
    features_number: Any
    stages_number: Any
    stumps_number: Any
    window_height: Any
    window_width: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def detect_multi_scale(self, *args, **kwargs): ...
    def __reduce__(self): ...
