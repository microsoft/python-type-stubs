from ... import BaseProvider as BaseProvider
from typing import Any

class Provider(BaseProvider):
    globe_mobile_number_prefixes: Any = ...
    smart_mobile_number_prefixes: Any = ...
    sun_mobile_number_prefixes: Any = ...
    globe_mobile_number_formats: Any = ...
    smart_mobile_number_formats: Any = ...
    sun_mobile_number_formats: Any = ...
    mobile_number_formats: Any = ...
    bayantel_landline_identifiers: Any = ...
    misc_landline_identifiers: Any = ...
    non_area2_landline_area_codes: Any = ...
    globe_area2_landline_number_formats: Any = ...
    pldt_area2_landline_number_formats: Any = ...
    bayantel_area2_landline_number_formats: Any = ...
    misc_area2_landline_number_formats: Any = ...
    area2_landline_number_formats: Any = ...
    non_area2_landline_number_formats: Any = ...
    landline_number_formats: Any = ...
    def globe_mobile_number_prefix(self): ...
    def smart_mobile_number_prefix(self): ...
    def sun_mobile_number_prefix(self): ...
    def bayantel_landline_identifier(self): ...
    def misc_landline_identifier(self): ...
    def non_area2_landline_area_code(self): ...
    def globe_mobile_number(self): ...
    def smart_mobile_number(self): ...
    def sun_mobile_number(self): ...
    def mobile_number(self): ...
    def globe_area2_landline_number(self): ...
    def pldt_area2_landline_number(self): ...
    def bayantel_area2_landline_number(self): ...
    def misc_area2_landline_number(self): ...
    def area2_landline_number(self): ...
    def non_area2_landline_number(self): ...
    def landline_number(self): ...
