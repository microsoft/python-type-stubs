from .. import BaseProvider as BaseProvider
from typing import Any

localized: bool

class Provider(BaseProvider):
    formats: Any = ...
    first_names: Any = ...
    last_names: Any = ...
    language_names: Any = ...
    def name(self): ...
    def first_name(self): ...
    def last_name(self): ...
    def name_male(self): ...
    def name_female(self): ...
    def first_name_male(self): ...
    def first_name_female(self): ...
    def last_name_male(self): ...
    def last_name_female(self): ...
    def prefix(self): ...
    def prefix_male(self): ...
    def prefix_female(self): ...
    def suffix(self): ...
    def suffix_male(self): ...
    def suffix_female(self): ...
    def language_name(self): ...
