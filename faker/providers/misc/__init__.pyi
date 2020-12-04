from typing import Any, Optional

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    def boolean(self, chance_of_getting_true: int = ...): ...
    def null_boolean(self): ...
    def binary(self, length: Any = ...): ...
    def md5(self, raw_output: bool = ...): ...
    def sha1(self, raw_output: bool = ...): ...
    def sha256(self, raw_output: bool = ...): ...
    def uuid4(self, cast_to: Any = ...): ...
    def password(
        self,
        length: int = ...,
        special_chars: bool = ...,
        digits: bool = ...,
        upper_case: bool = ...,
        lower_case: bool = ...,
    ): ...
    def zip(
        self,
        uncompressed_size: int = ...,
        num_files: int = ...,
        min_file_size: int = ...,
        compression: Optional[Any] = ...,
    ): ...
    def tar(
        self,
        uncompressed_size: int = ...,
        num_files: int = ...,
        min_file_size: int = ...,
        compression: Optional[Any] = ...,
    ): ...
    def dsv(
        self,
        dialect: str = ...,
        header: Optional[Any] = ...,
        data_columns: Any = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
        **fmtparams: Any
    ): ...
    def csv(
        self,
        header: Optional[Any] = ...,
        data_columns: Any = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ): ...
    def tsv(
        self,
        header: Optional[Any] = ...,
        data_columns: Any = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ): ...
    def psv(
        self,
        header: Optional[Any] = ...,
        data_columns: Any = ...,
        num_rows: int = ...,
        include_row_ids: bool = ...,
    ): ...
