from typing import Any, Callable, Dict, TypedDict

from tensorflow import Tensor

ActivationT = str | None | Callable[[Tensor], Tensor] | Dict[str, Any] | TypedDict

def get(identifier: ActivationT) -> Callable[[Tensor], Tensor]: ...
