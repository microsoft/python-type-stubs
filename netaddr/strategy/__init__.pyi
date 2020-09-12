from typing import Iterable, List, Tuple

"""Shared logic for various address types."""

def bytes_to_bits() -> List[str]:
    """
    :return: A 256 element list containing 8-bit binary digit strings. The
        list index value is equivalent to its bit string value.
    """
    ...

BYTES_TO_BITS: List[str]

def valid_words(words: Iterable[int], word_size: int, num_words: int) -> bool:
    """
    :param words: A sequence of unsigned integer word values.

    :param word_size: Width (in bits) of each unsigned integer word value.

    :param num_words: Number of unsigned integer words expected.

    :return: ``True`` if word sequence is valid for this address type,
        ``False`` otherwise.
    """
    ...

def int_to_words(int_val: int, word_size: int, num_words: int) -> Tuple[int]:
    """
    :param int_val: Unsigned integer to be divided into words of equal size.

    :param word_size: Width (in bits) of each unsigned integer word value.

    :param num_words: Number of unsigned integer words expected.

    :return: A tuple contain unsigned integer word values split according
        to provided arguments.
    """
    ...

def words_to_int(words: Iterable[int], word_size, num_words) -> int:
    """
    :param words: A sequence of unsigned integer word values.

    :param word_size: Width (in bits) of each unsigned integer word value.

    :param num_words: Number of unsigned integer words expected.

    :return: An unsigned integer that is equivalent to value represented
        by word sequence.
    """
    ...

def valid_bits(bits: str, width: int, word_sep: str = ...) -> bool:
    """
    :param bits: A network address in a delimited binary string format.

    :param width: Maximum width (in bits) of a network address (excluding
        delimiters).

    :param word_sep: (optional) character or string used to delimit word
        groups (default: '', no separator).

    :return: ``True`` if network address is valid, ``False`` otherwise.
    """
    ...

def bits_to_int(bits: str, width: int, word_sep: str = ...) -> int:
    """
    :param bits: A network address in a delimited binary string format.

    :param width: Maximum width (in bits) of a network address (excluding
        delimiters).

    :param word_sep: (optional) character or string used to delimit word
        groups (default: '', no separator).

    :return: An unsigned integer that is equivalent to value represented
        by network address in readable binary form.
    """
    ...

def int_to_bits(int_val: int, word_size: int, num_words: int, word_sep: str = ...) -> str:
    """
    :param int_val: An unsigned integer.

    :param word_size: Width (in bits) of each unsigned integer word value.

    :param num_words: Number of unsigned integer words expected.

    :param word_sep: (optional) character or string used to delimit word
        groups (default: '', no separator).

    :return: A network address in a delimited binary string format that is
        equivalent in value to unsigned integer.
    """
    ...

def valid_bin(bin_val: str, width: int) -> bool:
    """
    :param bin_val: A network address in Python's binary representation format
        ('0bxxx').

    :param width: Maximum width (in bits) of a network address (excluding
        delimiters).

    :return: ``True`` if network address is valid, ``False`` otherwise.
    """
    ...

def int_to_bin(int_val: int, width: int) -> str:
    """
    :param int_val: An unsigned integer.

    :param width: Maximum allowed width (in bits) of a unsigned integer.

    :return: Equivalent string value in Python's binary representation format
        ('0bxxx').
    """
    ...

def bin_to_int(bin_val: str, width: int) -> int:
    """
    :param bin_val: A string containing an unsigned integer in Python's binary
        representation format ('0bxxx').

    :param width: Maximum allowed width (in bits) of a unsigned integer.

    :return: An unsigned integer that is equivalent to value represented
        by Python binary string format.
    """
    ...

