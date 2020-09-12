from typing import Any, Iterable, List, Literal, Tuple, Type, Union
from netaddr.core import DictDotLookup
from netaddr.ip import IPAddress

"""
Classes and functions for dealing with MAC addresses, EUI-48, EUI-64, OUI, IAB
identifiers.
"""

class BaseIdentifier(object):
    """Base class for all IEEE identifiers."""

    def __init__(self) -> None: ...
    def __int__(self) -> int:
        """:return: integer value of this identifier"""
        ...
    def __long__(self) -> int:
        """:return: integer value of this identifier"""
        ...
    def __oct__(self) -> str:
        """:return: octal string representation of this identifier."""
        ...
    def __hex__(self) -> str:
        """:return: hexadecimal string representation of this identifier."""
        ...
    def __index__(self) -> int:
        """
        :return: return the integer value of this identifier when passed to
            hex(), oct() or bin().
        """
        ...

class OUI(BaseIdentifier):
    """
    An individual IEEE OUI (Organisationally Unique Identifier).

    For online details see - http://standards.ieee.org/regauth/oui/

    """

    def __init__(self, oui: Union[int, str]) -> None:
        """
        Constructor

        :param oui: an OUI string ``XX-XX-XX`` or an unsigned integer. \
            Also accepts and parses full MAC/EUI-48 address strings (but not \
            MAC/EUI-48 integers)!
        """
        ...
    def __eq__(self, other: Union[OUI, int, str]) -> bool: ...
    def __ne__(self, other: Union[OUI, int, str]) -> bool: ...
    def __getstate__(self) -> Any:
        """:returns: Pickled state of an `OUI` object."""
        ...
    def __setstate__(self, state: Any) -> None:
        """:param state: data used to unpickle a pickled `OUI` object."""
        ...
    @property
    def reg_count(self) -> int:
        """Number of registered organisations with this OUI"""
        ...
    def registration(self, index: int = ...) -> DictDotLookup:
        """
        The IEEE registration details for this OUI.

        :param index: the index of record (may contain multiple registrations)
            (Default: 0 - first registration)

        :return: Objectified Python data structure containing registration
            details.
        """
        ...
    def __str__(self) -> str:
        """:return: string representation of this OUI"""
        ...
    def __repr__(self) -> str:
        """:return: executable Python string to recreate equivalent object."""
        ...

class IAB(BaseIdentifier):
    IAB_EUI_VALUES: Tuple[int, int]
    @classmethod
    def split_iab_mac(cls, eui_int: int, strict: bool = ...) -> Tuple[int, int]:
        """
        :param eui_int: a MAC IAB as an unsigned integer.

        :param strict: If True, raises a ValueError if the last 12 bits of
            IAB MAC/EUI-48 address are non-zero, ignores them otherwise.
            (Default: False)
        """
        ...
    def __init__(self, iab: Union[int, str], strict: bool = ...) -> None:
        """
        Constructor

        :param iab: an IAB string ``00-50-C2-XX-X0-00`` or an unsigned \
            integer. This address looks like an EUI-48 but it should not \
            have any non-zero bits in the last 3 bytes.

        :param strict: If True, raises a ValueError if the last 12 bits \
            of IAB MAC/EUI-48 address are non-zero, ignores them otherwise. \
            (Default: False)
        """
        ...
    def __eq__(self, other: Union[IAB, int, str]) -> bool: ...
    def __ne__(self, other: Union[IAB, int, str]) -> bool: ...
    def __getstate__(self) -> Any:
        """:returns: Pickled state of an `IAB` object."""
        ...
    def __setstate__(self, state: Any) -> None:
        """:param state: data used to unpickle a pickled `IAB` object."""
        ...
    def registration(self) -> DictDotLookup:
        """The IEEE registration details for this IAB"""
        ...
    def __str__(self) -> str:
        """:return: string representation of this IAB"""
        ...
    def __repr__(self) -> str:
        """:return: executable Python string to recreate equivalent object."""
        ...

class EUI(BaseIdentifier):
    """
    An IEEE EUI (Extended Unique Identifier).

    Both EUI-48 (used for layer 2 MAC addresses) and EUI-64 are supported.

    Input parsing for EUI-48 addresses is flexible, supporting many MAC
    variants.

    """

    __slots__ = ...
    def __init__(self, addr: Union[EUI, int, str], version: Literal[48, 64] = ..., dialect: Type = ...) -> None:
        """
        Constructor.

        :param addr: an EUI-48 (MAC) or EUI-64 address in string format or \
            an unsigned integer. May also be another EUI object (copy \
            construction).

        :param version: (optional) the explicit EUI address version, either \
            48 or 64. Mainly used to distinguish EUI-48 and EUI-64 identifiers \
            specified as integers which may be numerically equivalent.

        :param dialect: (optional) the mac_* dialect to be used to configure \
            the formatting of EUI-48 (MAC) addresses.
        """
        ...
    def __getstate__(self) -> Any:
        """:returns: Pickled state of an `EUI` object."""
        ...
    def __setstate__(self, state: Any) -> None:
        """
        :param state: data used to unpickle a pickled `EUI` object.

        """
        ...
    value: Union[int, Type] = ...
    dialect: Type = ...
    @property
    def oui(self) -> OUI:
        """The OUI (Organisationally Unique Identifier) for this EUI."""
        ...
    @property
    def ei(self) -> Union[str, None]:
        """The EI (Extension Identifier) for this EUI"""
        ...
    def is_iab(self) -> bool:
        """:return: True if this EUI is an IAB address, False otherwise"""
        ...
    @property
    def iab(self) -> Union[IAB, None]:
        """
        If is_iab() is True, the IAB (Individual Address Block) is returned,
        ``None`` otherwise.
        """
        ...
    @property
    def version(self):
        """The EUI version represented by this EUI object."""
        ...
    def __getitem__(self, idx: int) -> Union[int, slice]:
        """
        :return: The integer value of the word referenced by index (both \
            positive and negative). Raises ``IndexError`` if index is out \
            of bounds. Also supports Python list slices for accessing \
            word groups.
        """
        ...
    def __setitem__(self, idx: Union[slice, int], value: int) -> None:
        """Set the value of the word referenced by index in this address"""
        ...
    def __hash__(self) -> int:
        """:return: hash of this EUI object suitable for dict keys, sets etc"""
        ...
    def __eq__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically the same as other, \
            ``False`` otherwise.
        """
        ...
    def __ne__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically the same as other, \
            ``False`` otherwise.
        """
        ...
    def __lt__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically lower in value than \
            other, ``False`` otherwise.
        """
        ...
    def __le__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically lower or equal in \
            value to other, ``False`` otherwise.
        """
        ...
    def __gt__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically greater in value \
            than other, ``False`` otherwise.
        """
        ...
    def __ge__(self, other: Union[EUI, int, str]) -> bool:
        """
        :return: ``True`` if this EUI object is numerically greater or equal \
            in value to other, ``False`` otherwise.
        """
        ...
    def bits(self, word_sep: str = ...) -> str:
        """
        :param word_sep: (optional) the separator to insert between words. \
            Default: None - use default separator for address type.

        :return: human-readable binary digit string of this address.
        """
        ...
    @property
    def packed(self) -> str:
        """The value of this EUI address as a packed binary string."""
        ...
    @property
    def words(self) -> List[int]:
        """A list of unsigned integer octets found in this EUI address."""
        ...
    @property
    def bin(self) -> str:
        """
        The value of this EUI adddress in standard Python binary
        representational form (0bxxx). A back port of the format provided by
        the builtin bin() function found in Python 2.6.x and higher.
        """
        ...
    def eui64(self) -> EUI:
        """
        - If this object represents an EUI-48 it is converted to EUI-64 \
            as per the standard.
        - If this object is already an EUI-64, a new, numerically \
            equivalent object is returned instead.

        :return: The value of this EUI object as a new 64-bit EUI object.
        """
        ...
    def modified_eui64(self) -> EUI:
        """
        - create a new EUI object with a modified EUI-64 as described in RFC 4291 section 2.5.1

        :return: a new and modified 64-bit EUI object.
        """
        ...
    def ipv6(self, prefix: Union[str, int]) -> IPAddress:
        """
        .. note:: This poses security risks in certain scenarios. \
            Please read RFC 4941 for details. Reference: RFCs 4291 and 4941.

        :param prefix: ipv6 prefix

        :return: new IPv6 `IPAddress` object based on this `EUI` \
            using the technique described in RFC 4291.
        """
        ...
    def ipv6_link_local(self) -> IPAddress:
        """
        .. note:: This poses security risks in certain scenarios. \
            Please read RFC 4941 for details. Reference: RFCs 4291 and 4941.

        :return: new link local IPv6 `IPAddress` object based on this `EUI` \
            using the technique described in RFC 4291.
        """
        ...
    @property
    def info(self) -> DictDotLookup:
        """
        A record dict containing IEEE registration details for this EUI
        (MAC-48) if available, None otherwise.
        """
        ...
    def format(self, dialect: Type = ...) -> str:
        """
        Format the EUI into the representational format according to the given
        dialect

        :param dialect: the mac_* dialect defining the formatting of EUI-48 \
            (MAC) addresses.

        :return: EUI in representational format according to the given dialect
        """
        ...
    def __str__(self) -> str:
        """:return: EUI in representational format"""
        ...
    def __repr__(self) -> str:
        """:return: executable Python string to recreate equivalent object."""
        ...

