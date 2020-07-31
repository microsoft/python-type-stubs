from . import Extension as Extension
from ..inlinepatterns import SubstituteTagInlineProcessor as SubstituteTagInlineProcessor
from typing import Any

BR_RE: str

class Nl2BrExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
