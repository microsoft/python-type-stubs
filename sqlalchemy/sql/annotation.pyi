from . import operators as operators
from .. import util as util
from typing import Any

class Annotated:
    def __new__(cls, *args: Any): ...
    __dict__: Any = ...
    def __init__(self, element: Any, values: Any) -> None: ...
    def __reduce__(self): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...

annotated_classes: Any
