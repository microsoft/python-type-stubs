import re
from typing import Any, Iterable, Optional

def smart_truncate(
    string: str, max_length: int = ..., word_boundary: bool = ..., separator: str = ..., save_order: bool = ...
) -> str:
    """
    Truncate a string.
    :param string (str): string for modification
    :param max_length (int): output string length
    :param word_boundary (bool):
    :param save_order (bool): if True then word order of output string is like input string
    :param separator (str): separator between words
    :return:
    """
    ...

def slugify(
    text: str,
    entities: bool = ...,
    decimal: bool = ...,
    hexadecimal: bool = ...,
    max_length: int = ...,
    word_boundary: bool = ...,
    separator: str = ...,
    save_order: bool = ...,
    stopwords: Iterable[str] = ...,
    regex_pattern: str = ...,
    lowercase: bool = ...,
    replacements: Iterable[str] = ...,
) -> str:
    """
    Make a slug from the given text.
    :param text (str): initial text
    :param entities (bool): converts html entities to unicode
    :param decimal (bool): converts html decimal to unicode
    :param hexadecimal (bool): converts html hexadecimal to unicode
    :param max_length (int): output string length
    :param word_boundary (bool): truncates to complete word even if length ends up shorter than max_length
    :param save_order (bool): if parameter is True and max_length > 0 return whole words in the initial order
    :param separator (str): separator between words
    :param stopwords (iterable): words to discount
    :param regex_pattern (str): regex pattern for allowed characters
    :param lowercase (bool): activate case sensitivity by setting it to False
    :param replacements (iterable): list of replacement rules e.g. [['|', 'or'], ['%', 'percent']]
    :return (str):
    """
    ...

