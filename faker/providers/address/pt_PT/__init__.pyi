from .. import Provider as AddressProvider
from typing import Any

class Provider(AddressProvider):
    street_prefixes: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    building_number_formats: Any = ...
    postcode_formats: Any = ...
    cities: Any = ...
    countries: Any = ...
    distritos: Any = ...
    concelhos: Any = ...
    freguesias: Any = ...
    places: Any = ...
    def street_prefix(self): ...
    def city_name(self): ...
    def distrito(self): ...
    def concelho(self): ...
    def freguesia(self): ...
    def place_name(self): ...
