from typing import ClassVar, Optional, Tuple, Union
from ._structures import (
    Infinity as Infinity,
    InfinityType as InfinityType,
    NegativeInfinity as NegativeInfinity,
    NegativeInfinityType as NegativeInfinityType,
)

# Copyright (c) Donald Stufft and individual contributors.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.

#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import collections
import itertools
import re
import warnings

__all__ = ["parse", "Version", "LegacyVersion", "InvalidVersion", "VERSION_PATTERN"]

InfiniteTypes = ...
PrePostDevType = ...
SubLocalType = ...
LocalType = ...
CmpKey = ...
LegacyCmpKey = ...
VersionComparisonMethod = ...

_Version = ...


def parse(version: str) -> Union["LegacyVersion", "Version"]:
    ...


class InvalidVersion(ValueError):
    ...


class _BaseVersion:
    _key: ClassVar[Union[CmpKey, LegacyCmpKey]] = ...

    def __hash__(self) -> int:
        ...

    # Please keep the duplicated `isinstance` check
    # in the six comparisons hereunder
    # unless you find a way to avoid adding overhead function calls.
    def __lt__(self, other: "_BaseVersion") -> bool:
        ...

    def __le__(self, other: "_BaseVersion") -> bool:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __ge__(self, other: "_BaseVersion") -> bool:
        ...

    def __gt__(self, other: "_BaseVersion") -> bool:
        ...

    def __ne__(self, other: object) -> bool:
        ...


class LegacyVersion(_BaseVersion):
    def __init__(self, version: str) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def public(self) -> str:
        ...

    def base_version(self) -> str:
        ...

    def epoch(self) -> int:
        ...

    def release(self) -> None:
        ...

    def pre(self) -> None:
        ...

    def post(self) -> None:
        ...

    def dev(self) -> None:
        ...

    def local(self) -> None:
        ...

    def is_prerelease(self) -> bool:
        ...

    def is_postrelease(self) -> bool:
        ...

    def is_devrelease(self) -> bool:
        ...


_legacy_version_component_re = ...

_legacy_version_replacement_map: dict = ...


# Deliberately not anchored to the start and end of the string, to make it
# easier for 3rd party code to reuse
VERSION_PATTERN: str = ...


class Version(_BaseVersion):

    _regex = ...

    def __init__(self, version: str) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def epoch(self) -> int:
        ...

    def release(self) -> Tuple[int, ...]:
        ...

    def pre(self) -> Optional[Tuple[str, int]]:
        ...

    def post(self) -> Optional[int]:
        ...

    def dev(self) -> Optional[int]:
        ...

    def local(self) -> Optional[str]:
        ...

    def public(self) -> str:
        ...

    def base_version(self) -> str:
        ...

    def is_prerelease(self) -> bool:
        ...

    def is_postrelease(self) -> bool:
        ...

    def is_devrelease(self) -> bool:
        ...

    def major(self) -> int:
        ...

    def minor(self) -> int:
        ...

    def micro(self) -> int:
        ...


_local_version_separators = ...
