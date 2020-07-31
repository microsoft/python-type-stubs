from .. import Provider as SsnProvider
from faker.utils.checksums import calculate_luhn as calculate_luhn
from typing import Any

class Provider(SsnProvider):
    def ssn(
        self, min_age: int = ..., max_age: int = ..., long: bool = ..., dash: bool = ...
    ): ...
    ORG_ID_DIGIT_1: Any = ...
    def org_id(self, long: bool = ..., dash: bool = ...): ...
    def vat_id(self): ...
    def org_and_vat_id(self, long: bool = ..., dash: bool = ...): ...
