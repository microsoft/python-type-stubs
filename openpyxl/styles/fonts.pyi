from lxml.etree import _Element
from openpyxl.cell.text import InlineFont
from openpyxl.styles.colors import Color
from typing import (
    Optional,
    Union,
)
from xml.etree.ElementTree import Element

def _no_value(
    tagname: str, value: bool, namespace: None = ...
) -> Optional[_Element]: ...

class Font:
    def __init__(
        self,
        name: Optional[str] = ...,
        sz: Optional[Union[str, int]] = ...,
        b: Optional[Union[str, bool]] = ...,
        i: Optional[Union[str, bool]] = ...,
        charset: Optional[Union[str, int]] = ...,
        u: Optional[str] = ...,
        strike: Optional[bool] = ...,
        color: Optional[Union[Color, str]] = ...,
        scheme: Optional[str] = ...,
        family: Optional[Union[str, int]] = ...,
        size: Optional[int] = ...,
        bold: Optional[bool] = ...,
        italic: Optional[bool] = ...,
        strikethrough: Optional[bool] = ...,
        underline: Optional[str] = ...,
        vertAlign: Optional[str] = ...,
        outline: None = ...,
        shadow: None = ...,
        condense: Optional[str] = ...,
        extend: Optional[str] = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node: Union[_Element, Element]) -> Union[InlineFont, Font]: ...

DEFAULT_FONT = Font(
    name="Calibri",
    sz=11,
    family=2,
    b=False,
    i=False,
    color=Color(theme=1),
    scheme="minor",
)
