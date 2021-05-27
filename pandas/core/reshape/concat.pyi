from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import Dtype
from typing import Hashable, Iterable, Literal, Mapping, Optional, Union, overload


@overload
def concat(objs: Union[Iterable[Optional[Series]], Mapping[Optional[Hashable], Optional[Series]]], join: str=..., ignore_index: bool=..., keys=..., levels=..., names=..., verify_integrity: bool=..., sort: bool=..., copy: bool=..., axis::Literal[0,'index',1,'columns']=Union[0,'index']) -> Series[Dtype]: ...
@overload
def concat(objs: Union[Iterable[Optional[Series]], Mapping[Optional[Hashable], Optional[Series]]], join: str=..., ignore_index: bool=..., keys=..., levels=..., names=..., verify_integrity: bool=..., sort: bool=..., copy: bool=..., axis:Literal[0,'index',1,'columns']=Union[1,'columns']) -> DataFrame: ...
@overload
def concat(objs: Union[Iterable[Optional[Series]], Mapping[Optional[Hashable], Optional[Series]]], join: str=..., ignore_index: bool=..., keys=..., levels=..., names=..., verify_integrity: bool=..., sort: bool=..., copy: bool=...) -> Series[Dtype]: ...
@overload
def concat(objs: Union[Iterable[Optional[Union[DataFrame, Series]]], Mapping[Optional[Hashable], Optional[Union[DataFrame, Series]]]], axis:Literal[0,'index',1,'columns']=..., join: str=..., ignore_index: bool=..., keys=..., levels=..., names=..., verify_integrity: bool=..., sort: bool=..., copy: bool=...) -> DataFrame: ...

