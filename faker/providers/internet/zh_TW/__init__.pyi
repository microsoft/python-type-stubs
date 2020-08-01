from typing import Any

from faker.utils.decorators import slugify as slugify

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    user_name_formats: Any = ...
    tlds: Any = ...
    def domain_word(self): ...
