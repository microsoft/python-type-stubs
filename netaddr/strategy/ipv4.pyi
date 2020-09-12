import sys as _sys
from socket import AF_INET
from netaddr.fbsocket import AF_INET
from typing import Dict, Iterable, Tuple
from netaddr.core import INET_PTON, ZEROFILL

"""IPv4 address logic."""
width = 32
word_size = 8
word_fmt = "%d"
word_sep = "."
family = AF_INET
family_name = "IPv4"
version = 4
word_base = 10
max_int: int
num_words: int
max_word: int
prefix_to_netmask: Dict[Tuple[int, int]]
netmask_to_prefix: Dict[Tuple[int, int]]
prefix_to_hostmask: Dict[Tuple[int, int]]
hostmask_to_prefix: Dict[Tuple[int, int]]

def valid_str(addr: str, flags: INET_PTON | ZEROFILL = ...) -> bool:
    """
    :param addr: An IPv4 address in presentation (string) format.

    :param flags: decides which rules are applied to the interpretation of the
        addr value. Supported constants are INET_PTON and ZEROFILL. See the
        netaddr.core docs for details.

    :return: ``True`` if IPv4 address is valid, ``False`` otherwise.
    """
    ...

def str_to_int(addr: str, flags: INET_PTON | ZEROFILL = ...) -> int:
    """
    :param addr: An IPv4 dotted decimal address in string form.

    :param flags: decides which rules are applied to the interpretation of the
        addr value. Supported constants are INET_PTON and ZEROFILL. See the
        netaddr.core docs for details.

    :return: The equivalent unsigned integer for a given IPv4 address.
    """
    ...

def int_to_str(int_val: int, dialect=...) -> str:
    """
    :param int_val: An unsigned integer.

    :param dialect: (unused) Any value passed in is ignored.

    :return: The IPv4 presentation (string) format address equivalent to the
        unsigned integer provided.
    """
    ...

def int_to_arpa(int_val: int) -> str:
    """
    :param int_val: An unsigned integer.

    :return: The reverse DNS lookup for an IPv4 address in network byte
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

def expand_partial_address(addr: str) -> str:
    """
    Expands a partial IPv4 address into a full 4-octet version.

    :param addr: an partial or abbreviated IPv4 address

    :return: an expanded IP address in presentation format (x.x.x.x)

    """
    ...

