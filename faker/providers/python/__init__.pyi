from typing import Any, Optional

from .. import BaseProvider as BaseProvider

class Provider(BaseProvider):
    default_value_types: Any = ...
    def pybool(self): ...
    def pystr(self, min_chars: Optional[Any] = ..., max_chars: int = ...): ...
    def pystr_format(self, string_format: str = ..., letters: Any = ...): ...
    def pyfloat(
        self,
        left_digits: Optional[Any] = ...,
        right_digits: Optional[Any] = ...,
        positive: bool = ...,
        min_value: Optional[Any] = ...,
        max_value: Optional[Any] = ...,
    ): ...
    def pyint(self, min_value: int = ..., max_value: int = ..., step: int = ...): ...
    def pydecimal(
        self,
        left_digits: Optional[Any] = ...,
        right_digits: Optional[Any] = ...,
        positive: bool = ...,
        min_value: Optional[Any] = ...,
        max_value: Optional[Any] = ...,
    ): ...
    def pytuple(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Optional[Any] = ...,
        *allowed_types: Any
    ): ...
    def pyset(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Optional[Any] = ...,
        *allowed_types: Any
    ): ...
    def pylist(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Optional[Any] = ...,
        *allowed_types: Any
    ): ...
    def pyiterable(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Optional[Any] = ...,
        *allowed_types: Any
    ): ...
    def pydict(
        self,
        nb_elements: int = ...,
        variable_nb_elements: bool = ...,
        value_types: Optional[Any] = ...,
        *allowed_types: Any
    ): ...
    def pystruct(
        self, count: int = ..., value_types: Optional[Any] = ..., *allowed_types: Any
    ): ...
