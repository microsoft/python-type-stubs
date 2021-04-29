from typing import Any
from matplotlib.figure import Figure

class SubplotBase:
    # TODO: write overloads for various forms
    def __init__(self, fig: Figure, *args: Any, **kwargs: Any) -> None: ...

    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
