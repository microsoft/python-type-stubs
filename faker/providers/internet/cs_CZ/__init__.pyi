from typing import Any

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    user_name_formats: Any = ...
    email_formats: Any = ...
    free_email_domains: Any = ...
    tlds: Any = ...
