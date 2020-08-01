from typing import Any

from .. import Provider as BaseProvider

ALPHABET: Any
ALPHANUMERIC: Any
VOWELS: str
CONSONANTS: Any
STATES_RENAPO: Any
FORBIDDEN_WORDS: Any
CURP_CHARACTERS: str

def ssn_checksum(digits: Any): ...
def curp_checksum(characters: Any): ...

class Provider(BaseProvider):
    ssn_formats: Any = ...
    def ssn(self): ...
    def curp(self): ...
    def rfc(self, natural: bool = ...): ...
