from typing import Iterable, Tuple, Type

"""
IEEE 64-bit EUI (Extended Unique Indentifier) logic.
"""
AF_EUI64 = 64
width = 64
family = AF_EUI64
family_name = "EUI-64"
version = 64
max_int = 2 ** width - 1

class eui64_base(object):
    """A standard IEEE EUI-64 dialect class."""

    word_size: int = ...
    num_words: int = ...
    max_word: int = ...
    word_sep: str = ...
    word_fmt: str = ...
    word_base: int = ...

class eui64_unix(eui64_base):
    """A UNIX-style MAC address dialect class."""

    word_size: int = ...
    num_words: int = ...
    word_sep: str = ...
    word_fmt: str = ...
    word_base: int = ...

class eui64_unix_expanded(eui64_unix):
    """A UNIX-style MAC address dialect class with leading zeroes."""

    word_fmt: str = ...

class eui64_cisco(eui64_base):
    """A Cisco 'triple hextet' MAC address dialect class."""

    word_size: int = ...
    num_words: int = ...
    word_sep: str = ...
    word_fmt: str = ...
    word_base: int = ...

class eui64_bare(eui64_base):
    """A bare (no delimiters) MAC address dialect class."""

    word_size: int = ...
    num_words: int = ...
    word_sep: str = ...
    word_fmt: str = ...
    word_base: int = ...

DEFAULT_EUI64_DIALECT = eui64_base
RE_EUI64_FORMATS: Tuple[str]

def valid_str(addr: str) -> bool:
    """
    :param addr: An IEEE EUI-64 indentifier in string form.

    :return: ``True`` if EUI-64 indentifier is valid, ``False`` otherwise.
    """
    ...

def str_to_int(addr: str) -> int:
    """
    :param addr: An IEEE EUI-64 indentifier in string form.

    :return: An unsigned integer that is equivalent to value represented
        by EUI-64 string address formatted according to the dialect
    """
    ...

def int_to_str(int_val: int, dialect: Type[eui64_base] = ...):
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options

    :return: An IEEE EUI-64 identifier that is equivalent to unsigned integer.
    """
    ...

def int_to_packed(int_val: int) -> str:
    """
    :param int_val: the integer to be packed.

    :return: a packed string that is equivalent to value represented by an
    unsigned integer.
    """
    ...

def packed_to_int(packed_int: str) -> int:
    """
    :param packed_int: a packed string containing an unsigned integer.
        It is assumed that string is packed in network byte order.

    :return: An unsigned integer equivalent to value of network address
        represented by packed binary string.
    """
    ...

def valid_words(words, dialect: Type[eui64_base] = ...) -> bool:
    """
    :param words: A sequence of unsigned integer word values.

    :param dialect: (optional) a Python class defining formatting options.

    :return: ``True`` if word sequence is valid for this address type,
        ``False`` otherwise.
    """
    ...

def int_to_words(int_val: int, dialect: Type[eui64_base] = ...) -> Iterable[int]:
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options.

    :return: An integer word (octet) sequence that is equivalent to value
        represented by an unsigned integer.
    """
    ...

def words_to_int(words: Iterable[int], dialect: Type[eui64_base] = ...) -> int:
    """
    :param words: A list or tuple containing integer octets.

    :param dialect: (optional) a Python class defining formatting options.

    :return: An unsigned integer that is equivalent to value represented
        by word (octet) sequence.
    """
    ...

def valid_bits(bits: str, dialect: Type[eui64_base] = ...) -> bool:
    """
    :param bits: A network address in a delimited binary string format.

    :param dialect: (optional) a Python class defining formatting options.

    :return: ``True`` if network address is valid, ``False`` otherwise.
    """
    ...

def bits_to_int(bits: str, dialect: Type[eui64_base] = ...):
    """
    :param bits: A network address in a delimited binary string format.

    :param dialect: (optional) a Python class defining formatting options.

    :return: An unsigned integer that is equivalent to value represented
        by network address in readable binary form.
    """
    ...

def int_to_bits(int_val: int, dialect: Type[eui64_base] = ...) -> str:
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options.

    :return: A network address in a delimited binary string format that is
        equivalent in value to unsigned integer.
    """
    ...

def valid_bin(bin_val: str, dialect: Type[eui64_base] = ...) -> bool:
    """
    :param bin_val: A network address in Python's binary representation format
        ('0bxxx').

    :param dialect: (optional) a Python class defining formatting options.

    :return: ``True`` if network address is valid, ``False`` otherwise.
    """
    ...

def int_to_bin(int_val: int) -> str:
    """
    :param int_val: An unsigned integer.

    :return: Equivalent string value in Python's binary representation format
        ('0bxxx').
    """
    ...

def bin_to_int(bin_val: str) -> int:
    """
    :param bin_val: A string containing an unsigned integer in Python's binary
        representation format ('0bxxx').

    :return: An unsigned integer that is equivalent to value represented
        by Python binary string format.
    """
    ...

