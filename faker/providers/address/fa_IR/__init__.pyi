from typing import Any

from .. import Provider as AddressProvider

class Provider(AddressProvider):
    city_prefixes: Any = ...
    building_number_formats: Any = ...
    street_suffixes: Any = ...
    postcode_formats: Any = ...
    states: Any = ...
    countries: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    secondary_address_formats: Any = ...
    def city_prefix(self): ...
    def secondary_address(self): ...
    def state(self): ...
