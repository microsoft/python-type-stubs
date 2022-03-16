from typing import (
    Iterator,
    Optional,
    Tuple,
    Union,
)

class Alignment:
    def __init__(
        self,
        horizontal: Optional[str] = ...,
        vertical: Optional[str] = ...,
        textRotation: Union[str, int] = ...,
        wrapText: Optional[Union[str, bool]] = ...,
        shrinkToFit: Optional[str] = ...,
        indent: Union[str, int] = ...,
        relativeIndent: int = ...,
        justifyLastLine: None = ...,
        readingOrder: int = ...,
        text_rotation: Optional[int] = ...,
        wrap_text: Optional[bool] = ...,
        shrink_to_fit: Optional[bool] = ...,
        mergeCell: None = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
