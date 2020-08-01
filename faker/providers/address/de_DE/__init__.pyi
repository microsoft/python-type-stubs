from typing import Any

from ..de import Provider as AddressProvider

class Provider(AddressProvider):
    city_formats: Any = ...
    city_with_postcode_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    building_number_formats: Any = ...
    street_suffixes_long: Any = ...
    street_suffixes_short: Any = ...
    postcode_formats: Any = ...
    cities: Any = ...
    states: Any = ...
    def street_suffix_short(self): ...
    def street_suffix_long(self): ...
    def city_name(self): ...
    def state(self): ...
    def city_with_postcode(self): ...
