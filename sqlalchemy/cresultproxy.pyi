from typing import Any

def safe_rowproxy_reconstructor(*args, **kwargs) -> Any: ...

class BaseRowProxy:
    _keymap: Any = ...
    _parent: Any = ...
    _processors: Any = ...
    _row: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def values(self, *args, **kwargs) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...