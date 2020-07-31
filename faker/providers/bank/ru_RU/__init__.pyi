from .. import Provider as BankProvider
from typing import Any

class Provider(BankProvider):
    country_code: str = ...
    region_codes: Any = ...
    department_code_formats: Any = ...
    credit_organization_code_formats: Any = ...
    checking_account_codes: Any = ...
    organization_codes: Any = ...
    currency_codes: Any = ...
    banks: Any = ...
    def bic(self): ...
    def correspondent_account(self): ...
    def checking_account(self): ...
    def bank(self): ...
