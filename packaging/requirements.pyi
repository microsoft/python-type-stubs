from ._typing import TYPE_CHECKING as TYPE_CHECKING
from .markers import MARKER_EXPR as MARKER_EXPR, Marker as Marker
from .specifiers import LegacySpecifier as LegacySpecifier, Specifier as Specifier, SpecifierSet as SpecifierSet
from typing import Any

class InvalidRequirement(ValueError): ...

ALPHANUM: Any
LBRACKET: Any
RBRACKET: Any
LPAREN: Any
RPAREN: Any
COMMA: Any
SEMICOLON: Any
AT: Any
PUNCTUATION: Any
IDENTIFIER_END: Any
IDENTIFIER: Any
NAME: Any
EXTRA = IDENTIFIER
URI: Any
URL: Any
EXTRAS_LIST: Any
EXTRAS: Any
VERSION_PEP440: Any
VERSION_LEGACY: Any
VERSION_ONE: Any
VERSION_MANY: Any
VERSION_SPEC: Any
MARKER_SEPARATOR = SEMICOLON
MARKER: Any
VERSION_AND_MARKER: Any
URL_AND_MARKER: Any
NAMED_REQUIREMENT: Any
REQUIREMENT: Any

class Requirement:
    name: Any = ...
    url: Any = ...
    extras: Any = ...
    specifier: Any = ...
    marker: Any = ...
    def __init__(self, requirement_string: str) -> None: ...
