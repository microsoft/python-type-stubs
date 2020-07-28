from ._typing import TYPE_CHECKING as TYPE_CHECKING, cast as cast
from .version import InvalidVersion as InvalidVersion, Version as Version
from typing import Any, Union

NormalizedName: Any

def canonicalize_name(name: str) -> NormalizedName: ...
def canonicalize_version(_version: str) -> Union[Version, str]: ...
