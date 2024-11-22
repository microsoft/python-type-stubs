from typing import Literal

from sympy.polys.domains.domain import Domain

class CharacteristicZero(Domain):
    has_CharacteristicZero = ...
    def characteristic(self) -> Literal[0]: ...
