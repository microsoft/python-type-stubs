from .. import Provider as CompanyProvider
from typing import Any

class Provider(CompanyProvider):
    formats: Any = ...
    catch_phrase_words: Any = ...
    bsWords: Any = ...
    company_suffixes: Any = ...
    def catch_phrase(self): ...
    def bs(self): ...
