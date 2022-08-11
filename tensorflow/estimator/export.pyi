from typing import Any, Generic, TypeVar

from tensorflow import Tensor

class ServingInputReceiver:
    def __getattr__(self, name: str) -> Any: ...

_T = TypeVar("_T", bound=Tensor | dict[str, Tensor])

class ExportOutput: ...

class PredictOutput(Generic[_T], ExportOutput):
    outputs: _T
    def __init__(self, outputs: _T) -> None: ...
