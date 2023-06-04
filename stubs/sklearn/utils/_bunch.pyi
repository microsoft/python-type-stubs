from numpy import ndarray


class Bunch(dict):
    def __init__(self, **kwargs) -> None:
        ...

    def __setattr__(self, key: str, value: list[str] | ndarray | str) -> None:
        ...

    def __dir__(self) -> list[str]:
        ...

    def __getattr__(self, key: str):
        ...

    def __setstate__(self, state):
        ...
