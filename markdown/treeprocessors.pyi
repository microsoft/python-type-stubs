from . import inlinepatterns as inlinepatterns, util as util
from typing import Any, Optional

def build_treeprocessors(md: Any, **kwargs: Any): ...
def isString(s: Any): ...

class Treeprocessor(util.Processor):
    def run(self, root: Any) -> None: ...

class InlineProcessor(Treeprocessor):
    md: Any = ...
    inlinePatterns: Any = ...
    ancestors: Any = ...
    def __init__(self, md: Any) -> None: ...
    @property
    def markdown(self): ...
    stashed_nodes: Any = ...
    parent_map: Any = ...
    def run(self, tree: Any, ancestors: Optional[Any] = ...): ...

class PrettifyTreeprocessor(Treeprocessor):
    def run(self, root: Any) -> None: ...