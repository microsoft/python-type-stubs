from pandas import DataFrame as DataFrame, Series as Series
from typing import Hashable, Iterable, Mapping, Optional, Union, overload, Literal, Any

@overload
def concat(
    objs: Union[Iterable[Optional[Series]], Mapping[Any, Optional[Series]]],
    join: str = ...,
    ignore_index: bool = ...,
    keys=...,
    levels=...,
    names=...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
    axis: Literal[0, "index"] = ...,
) -> Series: ...
@overload
def concat(
    objs: Union[Iterable[Optional[Series]], Mapping[Any, Optional[Series]]],
    axis: Literal[1, "columns"],
    join: str = ...,
    ignore_index: bool = ...,
    keys=...,
    levels=...,
    names=...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
) -> DataFrame: ...
@overload
def concat(
    objs: Union[Iterable[Optional[Union[DataFrame, Series]]], Mapping[Any, Optional[Union[DataFrame, Series]]]],
    axis: Literal[0, "index", 1, "columns"] = ...,
    join: str = ...,
    ignore_index: bool = ...,
    keys=...,
    levels=...,
    names=...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool = ...,
) -> DataFrame: ...
