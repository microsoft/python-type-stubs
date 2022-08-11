from typing import Any, Mapping

from tensorflow.keras import Model as Model

# Fix type Any later
def load_model(
    filepath: str, custom_objects: Mapping[str, object] | None = None, compile: bool = True, options: Any = None
) -> Any: ...
