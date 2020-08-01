from typing import Any

from .. import Provider as CompanyProvider

def regon_checksum(digits: Any): ...
def local_regon_checksum(digits: Any): ...
def company_vat_checksum(digits: Any): ...

class Provider(CompanyProvider):
    formats: Any = ...
    company_prefixes: Any = ...
    company_suffixes: Any = ...
    def company_prefix(self): ...
    def regon(self): ...
    def local_regon(self): ...
    def company_vat(self): ...
