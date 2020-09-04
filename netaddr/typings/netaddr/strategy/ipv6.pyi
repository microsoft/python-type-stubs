from netaddr.fbsocket import AF_INET6
from typing import Dict, Iterable, Tuple
from netaddr.core import INET_PTON, ZEROFILL

"""IPv6 address logic."""
OPT_IMPORTS = False
width = 128
word_size = 16
word_sep = ":"
family = AF_INET6
family_name = "IPv6"
version = 6
word_base = 16
max_int: int
num_words: int
max_word: int
prefix_to_netmask: Dict[Tuple[int, int]]
netmask_to_prefix: Dict[Tuple[int, int]]
prefix_to_hostmask: Dict[Tuple[int, int]]
hostmask_to_prefix: Dict[Tuple[int, int]]

class ipv6_compact(object):
    """An IPv6 dialect class - compact form."""

    word_fmt: str = ...
    compact = ...

class ipv6_full(ipv6_compact):
    """An IPv6 dialect class - 'all zeroes' form."""

    compact = ...

class ipv6_verbose(ipv6_compact):
    """An IPv6 dialect class - extra wide 'all zeroes' form."""

    word_fmt: str = ...
    compact = ...

def valid_str(addr: str, flags=...) -> bool:
    """
    :param addr: An IPv6 address in presentation (string) format.

    :param flags: decides which rules are applied to the interpretation of the
        addr value. Future use - currently has no effect.

    :return: ``True`` if IPv6 address is valid, ``False`` otherwise.
    """
    ...

def str_to_int(addr: str, flags=...) -> int:
    """
    :param addr: An IPv6 address in string form.

    :param flags: decides which rules are applied to the interpretation of the
        addr value. Future use - currently has no effect.

    :return: The equivalent unsigned integer for a given IPv6 address.
    """
    ...

def int_to_str(int_val: int, dialect=...) -> str:
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options.

    :return: The IPv6 presentation (string) format address equivalent to the
        unsigned integer provided.
    """
    ...

def int_to_arpa(int_val: int) -> str:
    """
    :param int_val: An unsigned integer.

    :return: The reverse DNS lookup for an IPv6 address in network byte
        order integer form.
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

def valid_words(words: Iterable[int]) -> bool:
    """
    :param words: A sequence of unsigned integer word values.

    :return: ``True`` if word sequence is valid for this address type,
        ``False`` otherwise.
    """
    ...

def int_to_words(int_val: int) -> Iterable[int]:
    """
    :param int_val: An unsigned integer.

    :return: An integer word (octet) sequence that is equivalent to value
        represented by an unsigned integer.
    """
    ...

def words_to_int(words: Iterable[int]) -> int:
    """
    :param words: A list or tuple containing integer octets.

    :return: An unsigned integer that is equivalent to value represented
        by word (octet) sequence.
    """
    ...

def valid_bits(bits: str) -> bool:
    """
    :param bits: A network address in a delimited binary string format.

    :return: ``True`` if network address is valid, ``False`` otherwise.
    """
    ...

def bits_to_int(bits: str) -> int:
    """
    :param bits: A network address in a delimited binary string format.

    :return: An unsigned integer that is equivalent to value represented
        by network address in readable binary form.
    """
    ...

def int_to_bits(int_val: int, word_sep: str = ...) -> str:
    """
    :param int_val: An unsigned integer.

    :param word_sep: (optional) character or string used to delimit word
        groups (default: '', no separator).

    :return: A network address in a delimited binary string format that is
        equivalent in value to unsigned integer.
    """
    ...

def valid_bin(bin_val: str) -> bool:
    """
    :param bin_val: A network address in Python's binary representation format
        ('0bxxx').

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

