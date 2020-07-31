from . import Extension as Extension
from ..preprocessors import Preprocessor as Preprocessor
from .codehilite import CodeHilite as CodeHilite, CodeHiliteExtension as CodeHiliteExtension, parse_hl_lines as parse_hl_lines
from typing import Any

class FencedCodeExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

class FencedBlockPreprocessor(Preprocessor):
    FENCED_BLOCK_RE: Any = ...
    CODE_WRAP: str = ...
    LANG_TAG: str = ...
    checked_for_codehilite: bool = ...
    codehilite_conf: Any = ...
    def __init__(self, md: Any) -> None: ...
    def run(self, lines: Any): ...

def makeExtension(**kwargs: Any): ...