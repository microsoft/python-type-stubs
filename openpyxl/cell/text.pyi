from openpyxl.styles.colors import Color
from typing import (
    List,
    Optional,
    Tuple,
    Union,
)

class InlineFont:
    def __init__(
        self,
        rFont: Optional[str] = ...,
        charset: Optional[str] = ...,
        family: Optional[str] = ...,
        b: Optional[bool] = ...,
        i: None = ...,
        strike: None = ...,
        outline: None = ...,
        shadow: None = ...,
        condense: None = ...,
        extend: None = ...,
        color: Optional[Color] = ...,
        sz: Optional[str] = ...,
        u: Optional[str] = ...,
        vertAlign: None = ...,
        scheme: Optional[str] = ...,
    ) -> None: ...

class PhoneticProperties:
    def __init__(
        self,
        fontId: Optional[Union[str, int]] = ...,
        type: Optional[str] = ...,
        alignment: None = ...,
    ) -> None: ...

class PhoneticText:
    def __init__(
        self,
        sb: Optional[Union[str, int]] = ...,
        eb: Optional[Union[str, int]] = ...,
        t: Optional[str] = ...,
    ) -> None: ...

class RichText:
    def __init__(
        self, rPr: Optional[InlineFont] = ..., t: Optional[str] = ...
    ) -> None: ...

class Text:
    def __init__(
        self,
        t: Optional[str] = ...,
        r: Union[Tuple, List[RichText]] = ...,
        rPh: Tuple = ...,
        phoneticPr: None = ...,
    ) -> None: ...
    @property
    def content(self) -> str: ...
