from .. import BaseProvider as BaseProvider
from .isbn import ISBN as ISBN, ISBN10 as ISBN10, ISBN13 as ISBN13
from .rules import RULES as RULES

class Provider(BaseProvider):
    def isbn13(self, separator: str = ...): ...
    def isbn10(self, separator: str = ...): ...
