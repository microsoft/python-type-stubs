from typing import Any

from .. import Provider as CompanyProvider

class Provider(CompanyProvider):
    company_names: Any = ...
    def company(self): ...
