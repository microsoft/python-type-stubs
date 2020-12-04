from typing import Any

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    free_email_domains: Any = ...
    tlds: Any = ...
