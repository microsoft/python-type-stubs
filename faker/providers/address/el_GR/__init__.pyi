from .. import Provider as AddressProvider
from typing import Any

class Provider(AddressProvider):
    building_number_formats: Any = ...
    street_prefixes_short: Any = ...
    street_prefixes_long: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    postcode_formats: Any = ...
    address_formats: Any = ...
    line_address_formats: Any = ...
    def line_address(self): ...
    def street_prefix(self): ...
    def street_prefix_short(self): ...
    def street_prefix_long(self): ...
    def street(self): ...
    def city(self): ...
    def region(self): ...
    cities: Any = ...
    regions: Any = ...
    countries: Any = ...
    localities: Any = ...
