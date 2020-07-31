from . import Extension as Extension
from ..postprocessors import UnescapePostprocessor as UnescapePostprocessor
from ..treeprocessors import Treeprocessor as Treeprocessor
from ..util import AMP_SUBSTITUTE as AMP_SUBSTITUTE, AtomicString as AtomicString, HTML_PLACEHOLDER_RE as HTML_PLACEHOLDER_RE, code_escape as code_escape, parseBoolValue as parseBoolValue
from typing import Any

def slugify(value: Any, separator: Any): ...

IDCOUNT_RE: Any

def unique(id: Any, ids: Any): ...
def get_name(el: Any): ...
def stashedHTML2text(text: Any, md: Any, strip_entities: bool = ...): ...
def unescape(text: Any): ...
def nest_toc_tokens(toc_list: Any): ...

class TocTreeprocessor(Treeprocessor):
    marker: Any = ...
    title: Any = ...
    base_level: Any = ...
    slugify: Any = ...
    sep: Any = ...
    use_anchors: Any = ...
    anchorlink_class: Any = ...
    use_permalinks: Any = ...
    permalink_class: Any = ...
    permalink_title: Any = ...
    header_rgx: Any = ...
    toc_top: int = ...
    toc_bottom: Any = ...
    def __init__(self, md: Any, config: Any) -> None: ...
    def iterparent(self, node: Any) -> None: ...
    def replace_marker(self, root: Any, elem: Any) -> None: ...
    def set_level(self, elem: Any) -> None: ...
    def add_anchor(self, c: Any, elem_id: Any) -> None: ...
    def add_permalink(self, c: Any, elem_id: Any) -> None: ...
    def build_toc_div(self, toc_list: Any): ...
    def run(self, doc: Any) -> None: ...

class TocExtension(Extension):
    TreeProcessorClass: Any = ...
    config: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    md: Any = ...
    def extendMarkdown(self, md: Any) -> None: ...
    def reset(self) -> None: ...

def makeExtension(**kwargs: Any): ...