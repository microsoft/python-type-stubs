from typing import Any

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    safe_email_tlds: Any = ...
    free_email_domains: Any = ...
    tlds: Any = ...
