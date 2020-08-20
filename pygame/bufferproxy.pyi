from typing import Optional, AnyStr

class BufferProxy:
    parent: Optional[BufferProxy]
    length: int
    raw: AnyStr
    def __init__(self, parent: Optional[BufferProxy] = ...) -> None: ...
    def write(self, buffer: bytes, offset: Optional[int] = ...) -> None: ...

