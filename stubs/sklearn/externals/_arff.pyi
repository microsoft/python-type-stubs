from typing import ClassVar, Literal, Optional
from typing_extensions import TypedDict as TypedDict

# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - rppereira@inf.ufrgs.br
# =============================================================================
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

__author__: Literal["Renato de Pontes Pereira, Matthias Feurer, Joel Nothman"] = ...
__author_email__: str = ...
__version__: str = ...

import re
import csv

# CONSTANTS ===================================================================
_SIMPLE_TYPES: list = ...

_TK_DESCRIPTION: str = ...
_TK_COMMENT: str = ...
_TK_RELATION: str = ...
_TK_ATTRIBUTE: str = ...
_TK_DATA: str = ...

_RE_RELATION = ...
_RE_ATTRIBUTE = ...
_RE_QUOTE_CHARS = ...
_RE_ESCAPE_CHARS = ...
_RE_SPARSE_LINE = ...
_RE_NONTRIVIAL_DATA = ...

ArffDenseDataType = ...
ArffSparseDataType = ...


_ESCAPE_SUB_MAP: dict = ...
_UNESCAPE_SUB_MAP: dict = ...


DENSE: int = ...  # Constant value representing a dense matrix
COO: int = ...  # Constant value representing a sparse matrix in coordinate format
LOD: int = ...  # Constant value representing a sparse matrix in list of
# dictionaries format
DENSE_GEN: int = ...  # Generator of dictionaries
LOD_GEN: int = ...  # Generator of dictionaries
_SUPPORTED_DATA_STRUCTURES: list = ...


# EXCEPTIONS ==================================================================
class ArffException(Exception):
    message: ClassVar[Optional[str]] = ...

    def __init__(self) -> None:
        ...

    def __str__(self) -> str:
        ...


class BadRelationFormat(ArffException):
    message: ClassVar[Literal["Bad @RELATION format, at line %d."]] = ...


class BadAttributeFormat(ArffException):
    message: ClassVar[Literal["Bad @ATTRIBUTE format, at line %d."]] = ...


class BadDataFormat(ArffException):
    def __init__(self, value) -> None:
        ...


class BadAttributeType(ArffException):
    message: ClassVar[Literal["Bad @ATTRIBUTE type, at line %d."]] = ...


class BadAttributeName(ArffException):
    def __init__(self, value, value2) -> None:
        ...


class BadNominalValue(ArffException):
    def __init__(self, value) -> None:
        ...


class BadNominalFormatting(ArffException):
    def __init__(self, value) -> None:
        ...


class BadNumericalValue(ArffException):
    message: ClassVar[Literal["Invalid numerical value, at line %d."]] = ...


class BadStringValue(ArffException):
    message: ClassVar[str] = ...


class BadLayout(ArffException):
    message: ClassVar[Literal["Invalid layout of the ARFF file, at line %d."]] = ...

    def __init__(self, msg: str = "") -> None:
        ...


class BadObject(ArffException):
    def __init__(self, msg: str = "Invalid object.") -> None:
        ...

    def __str__(self) -> str:
        ...


def encode_string(s):
    ...


class EncodedNominalConversor:
    def __init__(self, values) -> None:
        ...

    def __call__(self, value):
        ...


class NominalConversor:
    def __init__(self, values) -> None:
        ...

    def __call__(self, value):
        ...


class DenseGeneratorData:
    def decode_rows(self, stream, conversors):
        ...

    def encode_data(self, data, attributes):
        ...


class _DataListMixin:
    def decode_rows(self, stream, conversors):
        ...


class Data(_DataListMixin, DenseGeneratorData):
    ...


class COOData:
    def decode_rows(self, stream, conversors):
        ...

    def encode_data(self, data, attributes):
        ...


class LODGeneratorData:
    def decode_rows(self, stream, conversors):
        ...

    def encode_data(self, data, attributes):
        ...


class LODData(_DataListMixin, LODGeneratorData):
    ...


# =============================================================================

# ADVANCED INTERFACE ==========================================================
class ArffDecoder:
    def __init__(self) -> None:
        ...

    def decode(self, s, encode_nominal: bool = False, return_type=...):
        ...


class ArffEncoder:
    def encode(self, obj):
        ...

    def iter_encode(self, obj):
        ...


# =============================================================================

# BASIC INTERFACE =============================================================
def load(fp, encode_nominal: bool = False, return_type=...):
    ...


def loads(s, encode_nominal: bool = False, return_type=...):
    ...


def dump(obj, fp):
    ...


def dumps(obj):
    ...


# =============================================================================
