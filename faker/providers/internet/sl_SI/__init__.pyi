from .. import Provider as InternetProvider
from typing import Any

class Provider(InternetProvider):
    user_name_formats: Any = ...
    email_formats: Any = ...
    free_email_domains: Any = ...
    uri_pages: Any = ...
    uri_paths: Any = ...
    uri_extensions: Any = ...
    tlds: Any = ...
