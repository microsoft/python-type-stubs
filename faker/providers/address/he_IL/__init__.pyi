from typing import Any

from .. import Provider as AddressProvider

class Provider(AddressProvider):
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    postcode_formats: Any = ...
    street_titles: Any = ...
    city_names: Any = ...
    def city_name(self): ...
    def street_title(self): ...
