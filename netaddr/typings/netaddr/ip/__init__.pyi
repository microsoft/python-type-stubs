import sys as _sys
from typing import Any, Iterable, List, Literal, Tuple, Type, Union
from netaddr.strategy import ipv4 as _ipv4, ipv6 as _ipv6
from netaddr.core import DictDotLookup

PROTOCOL_VERSION: Literal[4, 6]
FLAGS: Literal[1, 2]
WIDTH: Literal[32, 128]

"""Routines for IPv4 and IPv6 addresses, subnets and ranges."""

class BaseIP(object):
    """
    An abstract base class for common operations shared between various IP
    related subclasses.

    """

    def __init__(self) -> None:
        """Constructor."""
        ...
    value = ...
    def key(self) -> NotImplemented:
        """
        :return: a key tuple that uniquely identifies this IP address.
        """
        ...
    def sort_key(self) -> NotImplemented:
        """
        :return: A key tuple used to compare and sort this `IPAddress`
            correctly.
        """
        ...
    def __hash__(self) -> int:
        """
        :return: A hash value uniquely indentifying this IP object.
        """
        ...
    def __eq__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            equivalent to ``other``, ``False`` otherwise.
        """
        ...
    def __ne__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            not equivalent to ``other``, ``False`` otherwise.
        """
        ...
    def __lt__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            less than ``other``, ``False`` otherwise.
        """
        ...
    def __le__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            less than or equal to ``other``, ``False`` otherwise.
        """
        ...
    def __gt__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            greater than ``other``, ``False`` otherwise.
        """
        ...
    def __ge__(self, other: BaseIP) -> bool:
        """
        :param other: an `IPAddress` or `IPNetwork` object.

        :return: ``True`` if this `IPAddress` or `IPNetwork` object is
            greater than or equal to ``other``, ``False`` otherwise.
        """
        ...
    def is_unicast(self) -> bool:
        """:return: ``True`` if this IP is unicast, ``False`` otherwise"""
        ...
    def is_multicast(self) -> bool:
        """:return: ``True`` if this IP is multicast, ``False`` otherwise"""
        ...
    def is_loopback(self) -> bool:
        """
        :return: ``True`` if this IP is loopback address (not for network
            transmission), ``False`` otherwise.
            References: RFC 3330 and 4291.
        """
        ...
    def is_private(self) -> bool:
        """
        :return: ``True`` if this IP is for internal/private use only
            (i.e. non-public), ``False`` otherwise. Reference: RFCs 1918,
            3330, 4193, 3879 and 2365.
        """
        ...
    def is_link_local(self) -> bool:
        """
        :return: ``True`` if this IP is link-local address ``False`` otherwise.
            Reference: RFCs 3927 and 4291.
        """
        ...
    def is_reserved(self) -> bool:
        """
        :return: ``True`` if this IP is in IANA reserved range, ``False``
            otherwise. Reference: RFCs 3330 and 3171.
        """
        ...
    def is_ipv4_mapped(self) -> bool:
        """
        :return: ``True`` if this IP is IPv4-compatible IPv6 address, ``False``
            otherwise.
        """
        ...
    def is_ipv4_compat(self) -> bool:
        """
        :return: ``True`` if this IP is IPv4-mapped IPv6 address, ``False``
            otherwise.
        """
        ...
    @property
    def info(self) -> DictDotLookup:
        """
        A record dict containing IANA registration details for this IP address
        if available, None otherwise.
        """
        ...
    @property
    def version(self) -> PROTOCOL_VERSION:
        """the IP protocol version represented by this IP object."""
        ...

class IPAddress(BaseIP):
    """
    An individual IPv4 or IPv6 address without a net mask or subnet prefix.

    To support these and other network based operations, see `IPNetwork`.

    """

    __slots__ = ...
    def __init__(self, addr: Union[BaseIP, str], version: PROTOCOL_VERSION = ..., flags: FLAGS = ...) -> None:
        """
        Constructor.

        :param addr: an IPv4 or IPv6 address which may be represented in an
            accepted string format, as an unsigned integer or as another
            IPAddress object (copy construction).

        :param version: (optional) optimizes version detection if specified
            and distinguishes between IPv4 and IPv6 for addresses with an
            equivalent integer value.

        :param flags: (optional) decides which rules are applied to the
            interpretation of the addr value. Supported constants are
            INET_PTON and ZEROFILL. See the netaddr.core docs for further
            details.

        """
        ...
    def __getstate__(self) -> Tuple[Any, PROTOCOL_VERSION]:
        """:returns: Pickled state of an `IPAddress` object."""
        ...
    def __setstate__(self, state: Tuple[Any, PROTOCOL_VERSION]) -> None:
        """
        :param state: data used to unpickle a pickled `IPAddress` object.

        """
        ...
    def netmask_bits(self) -> int:
        """
        @return: If this IP is a valid netmask, the number of non-zero
            bits are returned, otherwise it returns the width in bits for
            the IP address version.
        """
        ...
    def is_hostmask(self) -> bool:
        """
        :return: ``True`` if this IP address host mask, ``False`` otherwise.
        """
        ...
    def is_netmask(self) -> bool:
        """
        :return: ``True`` if this IP address network mask, ``False`` otherwise.
        """
        ...
    def __iadd__(self, num: int) -> IPAddress:
        """
        Increases the numerical value of this IPAddress by num.

        An IndexError is raised if result exceeds maximum IP address value or
        is less than zero.

        :param num: size of IP address increment.
        """
        ...
    def __isub__(self, num: int) -> IPAddress:
        """
        Decreases the numerical value of this IPAddress by num.

        An IndexError is raised if result is less than zero or exceeds maximum
        IP address value.

        :param num: size of IP address decrement.
        """
        ...
    def __add__(self, num: int) -> IPAddress:
        """
        Add the numerical value of this IP address to num and provide the
        result as a new IPAddress object.

        :param num: size of IP address increase.

        :return: a new IPAddress object with its numerical value increased by num.
        """
        ...
    __radd__ = ...
    def __sub__(self, num: int) -> IPAddress:
        """
        Subtract the numerical value of this IP address from num providing
        the result as a new IPAddress object.

        :param num: size of IP address decrease.

        :return: a new IPAddress object with its numerical value decreased by num.
        """
        ...
    def __rsub__(self, num: int) -> IPAddress:
        """
        Subtract num (lvalue) from the numerical value of this IP address
        (rvalue) providing the result as a new IPAddress object.

        :param num: size of IP address decrease.

        :return: a new IPAddress object with its numerical value decreased by num.
        """
        ...
    def key(self) -> Tuple[PROTOCOL_VERSION, Any]:
        """
        :return: a key tuple that uniquely identifies this IP address.
        """
        ...
    def sort_key(self) -> Tuple[PROTOCOL_VERSION, Any, WIDTH]:
        """:return: A key tuple used to compare and sort this `IPAddress` correctly."""
        ...
    def __int__(self) -> int:
        """:return: the value of this IP address as an unsigned integer"""
        ...
    def __long__(self) -> int:
        """:return: the value of this IP address as an unsigned integer"""
        ...
    def __oct__(self) -> str:
        """:return: an octal string representation of this IP address."""
        ...
    def __hex__(self) -> str:
        """:return: a hexadecimal string representation of this IP address."""
        ...
    def __index__(self) -> int:
        """
        :return: return the integer value of this IP address when called by \
            hex(), oct() or bin().
        """
        ...
    def __bytes__(self) -> bytes:
        """ 
        :return: a bytes object equivalent to this IP address. In network
        byte order, big-endian.
        """
        ...
    def bits(self, word_sep: str = ...) -> str:
        """
        :param word_sep: (optional) the separator to insert between words.
            Default: None - use default separator for address type.

        :return: the value of this IP address as a binary digit string."""
        ...
    @property
    def packed(self) -> str:
        """The value of this IP address as a packed binary string."""
        ...
    @property
    def words(self) -> List[int]:
        """
        A list of unsigned integer words (octets for IPv4, hextets for IPv6)
        found in this IP address.
        """
        ...
    @property
    def bin(self) -> str:
        """
        The value of this IP adddress in standard Python binary
        representational form (0bxxx). A back port of the format provided by
        the builtin bin() function found in Python 2.6.x and higher.
        """
        ...
    @property
    def reverse_dns(self) -> str:
        """The reverse DNS lookup record for this IP address"""
        ...
    def ipv4(self) -> Union[IPAddress, None]:
        """
        Raises an `AddrConversionError` if IPv6 address cannot be converted
        to IPv4.

        :return: A numerically equivalent version 4 `IPAddress` object.
        """
        ...
    def ipv6(self, ipv4_compatible: bool = ...) -> Union[IPAddress, None]:
        """
        .. note:: The IPv4-mapped IPv6 address format is now considered \
            deprecated. See RFC 4291 or later for details.

        :param ipv4_compatible: If ``True`` returns an IPv4-mapped address
            (::ffff:x.x.x.x), an IPv4-compatible (::x.x.x.x) address
            otherwise. Default: False (IPv4-mapped).

        :return: A numerically equivalent version 6 `IPAddress` object.
        """
        ...
    def format(self, dialect: Type[IPAddress] = ...) -> str:
        """
        Only relevant for IPv6 addresses. Has no effect for IPv4.

        :param dialect: An ipv6_* dialect class.

        :return: an alternate string representation for this IP address.
        """
        ...
    def __or__(self, other: IPAddress) -> IPAddress:
        """
        :param other: An `IPAddress` object (or other int-like object).

        :return: bitwise OR (x | y) between the integer value of this IP
            address and ``other``.
        """
        ...
    def __and__(self, other: IPAddress) -> IPAddress:
        """
        :param other: An `IPAddress` object (or other int-like object).

        :return: bitwise AND (x & y) between the integer value of this IP
            address and ``other``.
        """
        ...
    def __xor__(self, other: IPAddress) -> IPAddress:
        """
        :param other: An `IPAddress` object (or other int-like object).

        :return: bitwise exclusive OR (x ^ y) between the integer value of
            this IP address and ``other``.
        """
        ...
    def __lshift__(self, numbits: int) -> IPAddress:
        """
        :param numbits: size of bitwise shift.

        :return: an `IPAddress` object based on this one with its integer
            value left shifted by ``numbits``.
        """
        ...
    def __rshift__(self, numbits: int) -> IPAddress:
        """
        :param numbits: size of bitwise shift.

        :return: an `IPAddress` object based on this one with its integer
            value right shifted by ``numbits``.
        """
        ...
    def __nonzero__(self):
        """:return: ``True`` if the numerical value of this IP address is not \
            zero, ``False`` otherwise."""
        ...
    __bool__ = ...
    def __str__(self) -> str:
        """:return: IP address in presentational format"""
        ...
    def __repr__(self) -> str:
        """:return: Python statement to create an equivalent object"""
        ...

class IPListMixin(object):
    """
    A mixin class providing shared list-like functionality to classes
    representing groups of IP addresses.

    """

    def __iter__(self) -> Iterable[IPAddress]:
        """
        :return: An iterator providing access to all `IPAddress` objects
            within range represented by this ranged IP object.
        """
        ...
    @property
    def size(self) -> int:
        """
        The total number of IP addresses within this ranged IP object.
        """
        ...
    def __len__(self) -> int:
        """
        :return: the number of IP addresses in this ranged IP object. Raises
            an `IndexError` if size > system max int (a Python 2.x
            limitation). Use the .size property for subnets of any size.
        """
        ...
    def __getitem__(self, index: int) -> Union[IPAddress, None]:
        """
        :return: The IP address(es) in this `IPNetwork` object referenced by
            index or slice. As slicing can produce large sequences of objects
            an iterator is returned instead of the more usual `list`.
        """
        ...
    def __contains__(self, other: IPAddress) -> bool:
        """
        :param other: an `IPAddress` or ranged IP object.

        :return: ``True`` if other falls within the boundary of this one,
            ``False`` otherwise.
        """
        ...
    def __nonzero__(self) -> bool:
        """
        Ranged IP objects always represent a sequence of at least one IP
        address and are therefore always True in the boolean context.
        """
        ...

def parse_ip_network(
    module: Any, addr: Union[Tuple[int, int], str], implicit_prefix: bool = ..., flags: int = ...
) -> Tuple[int, int]: ...

class IPNetwork(BaseIP, IPListMixin):
    """
    An IPv4 or IPv6 network or subnet.

    A combination of an IP address and a network mask.

    Accepts CIDR and several related variants :

    a) Standard CIDR::

        x.x.x.x/y -> 192.0.2.0/24
        x::/y -> fe80::/10

    b) Hybrid CIDR format (netmask address instead of prefix), where 'y' \
       address represent a valid netmask::

        x.x.x.x/y.y.y.y -> 192.0.2.0/255.255.255.0
        x::/y:: -> fe80::/ffc0::

    c) ACL hybrid CIDR format (hostmask address instead of prefix like \
       Cisco's ACL bitmasks), where 'y' address represent a valid netmask::

        x.x.x.x/y.y.y.y -> 192.0.2.0/0.0.0.255
        x::/y:: -> fe80::/3f:ffff:ffff:ffff:ffff:ffff:ffff:ffff

    d) Abbreviated CIDR format (as of netaddr 0.7.x this requires the \
       optional constructor argument ``implicit_prefix=True``)::

        x       -> 192
        x/y     -> 10/8
        x.x/y   -> 192.168/16
        x.x.x/y -> 192.168.0/24

        which are equivalent to::

        x.0.0.0/y   -> 192.0.0.0/24
        x.0.0.0/y   -> 10.0.0.0/8
        x.x.0.0/y   -> 192.168.0.0/16
        x.x.x.0/y   -> 192.168.0.0/24

    .. warning::

        The next release (0.9.0) will contain a backwards incompatible change
        connected to handling of RFC 6164 IPv6 addresses (/127 and /128 subnets).
        When iterating ``IPNetwork`` and ``IPNetwork.iter_hosts()`` the first
        addresses in the networks will no longer be excluded and ``broadcast``
        will be ``None``.
    """

    def __init__(
        self,
        addr: Union[IPAddress, IPNetwork, Tuple[int, int], str],
        implicit_prefix: bool = ...,
        version: PROTOCOL_VERSION = ...,
        flags: int = ...,
    ) -> None:
        """
        Constructor.

        :param addr: an IPv4 or IPv6 address with optional CIDR prefix,
            netmask or hostmask. May be an IP address in presentation
            (string) format, an tuple containing and integer address and a
            network prefix, or another IPAddress/IPNetwork object (copy
            construction).

        :param implicit_prefix: (optional) if True, the constructor uses
            classful IPv4 rules to select a default prefix when one is not
            provided. If False it uses the length of the IP address version.
            (default: False)

        :param version: (optional) optimizes version detection if specified
            and distinguishes between IPv4 and IPv6 for addresses with an
            equivalent integer value.

        :param flags: (optional) decides which rules are applied to the
            interpretation of the addr value. Currently only supports the
            NOHOST option. See the netaddr.core docs for further details.

        """
        ...
    def __getstate__(self) -> Tuple[Any, PROTOCOL_VERSION]:
        """:return: Pickled state of an `IPNetwork` object."""
        ...
    def __setstate__(self, state: Tuple[Any, PROTOCOL_VERSION]) -> None:
        """
        :param state: data used to unpickle a pickled `IPNetwork` object.

        """
        ...
    prefixlen: int = ...
    @property
    def ip(self):
        """
        The IP address of this `IPNetwork` object. This is may or may not be
        the same as the network IP address which varies according to the value
        of the CIDR subnet prefix.
        """
        ...
    @property
    def network(self):
        """The network address of this `IPNetwork` object."""
        ...
    @property
    def broadcast(self):
        """The broadcast address of this `IPNetwork` object.

        .. warning::

            The next release (0.9.0) will contain a backwards incompatible change
            connected to handling of RFC 6164 IPv6 addresses (/127 and /128 subnets).
            ``broadcast`` will be ``None`` when dealing with those networks.
        """
        ...
    @property
    def first(self) -> Union[IPAddress, None]:
        """
        The integer value of first IP address found within this `IPNetwork`
        object.
        """
        ...
    @property
    def last(self) -> Union[IPAddress, None]:
        """
        The integer value of last IP address found within this `IPNetwork`
        object.
        """
        ...
    @property
    def netmask(self):
        """The subnet mask of this `IPNetwork` object."""
        ...
    @netmask.setter
    def netmask(self, value):
        """Set the prefixlen using a subnet mask"""
        ...
    @property
    def hostmask(self):
        """The host mask of this `IPNetwork` object."""
        ...
    @property
    def cidr(self):
        """
        The true CIDR address for this `IPNetwork` object which omits any
        host bits to the right of the CIDR subnet prefix.
        """
        ...
    def __iadd__(self, num: int) -> IPNetwork:
        """
        Increases the value of this `IPNetwork` object by the current size
        multiplied by ``num``.

        An `IndexError` is raised if result exceeds maximum IP address value
        or is less than zero.

        :param num: (optional) number of `IPNetwork` blocks to increment \
            this IPNetwork's value by.
        """
        ...
    def __isub__(self, num: int) -> IPNetwork:
        """
        Decreases the value of this `IPNetwork` object by the current size
        multiplied by ``num``.

        An `IndexError` is raised if result is less than zero or exceeds
        maximum IP address value.

        :param num: (optional) number of `IPNetwork` blocks to decrement \
            this IPNetwork's value by.
        """
        ...
    def __contains__(self, other):
        """
        :param other: an `IPAddress` or ranged IP object.

        :return: ``True`` if other falls within the boundary of this one,
            ``False`` otherwise.
        """
        ...
    def key(self):
        """
        :return: A key tuple used to uniquely identify this `IPNetwork`.
        """
        ...
    def sort_key(self):
        """
        :return: A key tuple used to compare and sort this `IPNetwork` correctly.
        """
        ...
    def ipv4(self):
        """
        :return: A numerically equivalent version 4 `IPNetwork` object. \
            Raises an `AddrConversionError` if IPv6 address cannot be \
            converted to IPv4.
        """
        ...
    def ipv6(self, ipv4_compatible=...):
        """
        .. note:: the IPv4-mapped IPv6 address format is now considered \
        deprecated. See RFC 4291 or later for details.

        :param ipv4_compatible: If ``True`` returns an IPv4-mapped address
            (::ffff:x.x.x.x), an IPv4-compatible (::x.x.x.x) address
            otherwise. Default: False (IPv4-mapped).

        :return: A numerically equivalent version 6 `IPNetwork` object.
        """
        ...
    def previous(self, step=...):
        """
        :param step: the number of IP subnets between this `IPNetwork` object
            and the expected subnet. Default: 1 (the previous IP subnet).

        :return: The adjacent subnet preceding this `IPNetwork` object.
        """
        ...
    def next(self, step=...):
        """
        :param step: the number of IP subnets between this `IPNetwork` object
            and the expected subnet. Default: 1 (the next IP subnet).

        :return: The adjacent subnet succeeding this `IPNetwork` object.
        """
        ...
    def supernet(self, prefixlen=...):
        """
        Provides a list of supernets for this `IPNetwork` object between the
        size of the current prefix and (if specified) an endpoint prefix.

        :param prefixlen: (optional) a CIDR prefix for the maximum supernet.
            Default: 0 - returns all possible supernets.

        :return: a tuple of supernet `IPNetwork` objects.
        """
        ...
    def subnet(self, prefixlen, count=..., fmt=...):
        """
        A generator that divides up this IPNetwork's subnet into smaller
        subnets based on a specified CIDR prefix.

        :param prefixlen: a CIDR prefix indicating size of subnets to be
            returned.

        :param count: (optional) number of consecutive IP subnets to be
            returned.

        :return: an iterator containing IPNetwork subnet objects.
        """
        ...
    def iter_hosts(self):
        """
        A generator that provides all the IP addresses that can be assigned
        to hosts within the range of this IP object's subnet.

        - for IPv4, the network and broadcast addresses are always excluded. \
          for subnets that contains less than 4 IP addresses /31 and /32 \
          report in a manner per RFC 3021

        - for IPv6, only the unspecified address '::' or Subnet-Router anycast \
          address (first address in the network) is excluded.

        .. warning::

            The next release (0.9.0) will contain a backwards incompatible change
            connected to handling of RFC 6164 IPv6 addresses (/127 and /128 subnets).
            When iterating ``IPNetwork`` and ``IPNetwork.iter_hosts()`` the first
            addresses in the networks will no longer be excluded.

        :return: an IPAddress iterator
        """
        ...
    def __str__(self) -> str:
        """:return: this IPNetwork in CIDR format"""
        ...
    def __repr__(self):
        """:return: Python statement to create an equivalent object"""
        ...

class IPRange(BaseIP, IPListMixin):
    """
    An arbitrary IPv4 or IPv6 address range.

    Formed from a lower and upper bound IP address. The upper bound IP cannot
    be numerically smaller than the lower bound and the IP version of both
    must match.

    """

    __slots__ = ...
    def __init__(self, start, end, flags=...) -> None:
        """
        Constructor.

        :param start: an IPv4 or IPv6 address that forms the lower
            boundary of this IP range.

        :param end: an IPv4 or IPv6 address that forms the upper
            boundary of this IP range.

        :param flags: (optional) decides which rules are applied to the
            interpretation of the start and end values. Supported constants
            are INET_PTON and ZEROFILL. See the netaddr.core docs for further
            details.

        """
        ...
    def __getstate__(self):
        """:return: Pickled state of an `IPRange` object."""
        ...
    def __setstate__(self, state):
        """
        :param state: data used to unpickle a pickled `IPRange` object.
        """
        ...
    def __contains__(self, other): ...
    @property
    def first(self):
        """The integer value of first IP address in this `IPRange` object."""
        ...
    @property
    def last(self):
        """The integer value of last IP address in this `IPRange` object."""
        ...
    def key(self):
        """
        :return: A key tuple used to uniquely identify this `IPRange`.
        """
        ...
    def sort_key(self):
        """
        :return: A key tuple used to compare and sort this `IPRange` correctly.
        """
        ...
    def cidrs(self):
        """
        The list of CIDR addresses found within the lower and upper bound
        addresses of this `IPRange`.
        """
        ...
    def __str__(self) -> str:
        """:return: this `IPRange` in a common representational format."""
        ...
    def __repr__(self):
        """:return: Python statement to create an equivalent object"""
        ...

def iter_unique_ips(*args):
    """
    :param args: A list of IP addresses and subnets passed in as arguments.

    :return: A generator that flattens out IP subnets, yielding unique
        individual IP addresses (no duplicates).
    """
    ...

def cidr_abbrev_to_verbose(abbrev_cidr):
    """
    A function that converts abbreviated IPv4 CIDRs to their more verbose
    equivalent.

    :param abbrev_cidr: an abbreviated CIDR.

    Uses the old-style classful IP address rules to decide on a default
    subnet prefix if one is not explicitly provided.

    Only supports IPv4 addresses.

    Examples ::

        10                  - 10.0.0.0/8
        10/16               - 10.0.0.0/16
        128                 - 128.0.0.0/16
        128/8               - 128.0.0.0/8
        192.168             - 192.168.0.0/16

    :return: A verbose CIDR from an abbreviated CIDR or old-style classful \
        network address. The original value if it was not recognised as a \
        supported abbreviation.
    """
    ...

def cidr_merge(ip_addrs):
    """
    A function that accepts an iterable sequence of IP addresses and subnets
    merging them into the smallest possible list of CIDRs. It merges adjacent
    subnets where possible, those contained within others and also removes
    any duplicates.

    :param ip_addrs: an iterable sequence of IP addresses, subnets or ranges.

    :return: a summarized list of `IPNetwork` objects.
    """
    ...

def cidr_exclude(target, exclude):
    """
    Removes an exclude IP address or subnet from target IP subnet.

    :param target: the target IP address or subnet to be divided up.

    :param exclude: the IP address or subnet to be removed from target.

    :return: list of `IPNetwork` objects remaining after exclusion.
    """
    ...

def cidr_partition(target, exclude):
    """
    Partitions a target IP subnet on an exclude IP address.

    :param target: the target IP address or subnet to be divided up.

    :param exclude: the IP address or subnet to partition on

    :return: list of `IPNetwork` objects before, the partition and after, sorted.

    Adding the three lists returns the equivalent of the original subnet.
    """
    ...

def spanning_cidr(ip_addrs):
    """
    Function that accepts a sequence of IP addresses and subnets returning
    a single `IPNetwork` subnet that is large enough to span the lower and
    upper bound IP addresses with a possible overlap on either end.

    :param ip_addrs: sequence of IP addresses and subnets.

    :return: a single spanning `IPNetwork` subnet.
    """
    ...

def iter_iprange(start, end, step=...):
    """
    A generator that produces IPAddress objects between an arbitrary start
    and stop IP address with intervals of step between them. Sequences
    produce are inclusive of boundary IPs.

    :param start: start IP address.

    :param end: end IP address.

    :param step: (optional) size of step between IP addresses. Default: 1

    :return: an iterator of one or more `IPAddress` objects.
    """
    ...

def iprange_to_cidrs(start, end):
    """
    A function that accepts an arbitrary start and end IP address or subnet
    and returns a list of CIDR subnets that fit exactly between the boundaries
    of the two with no overlap.

    :param start: the start IP address or subnet.

    :param end: the end IP address or subnet.

    :return: a list of one or more IP addresses and subnets.
    """
    ...

def smallest_matching_cidr(ip, cidrs):
    """
    Matches an IP address or subnet against a given sequence of IP addresses
    and subnets.

    :param ip: a single IP address or subnet.

    :param cidrs: a sequence of IP addresses and/or subnets.

    :return: the smallest (most specific) matching IPAddress or IPNetwork
        object from the provided sequence, None if there was no match.
    """
    ...

def largest_matching_cidr(ip, cidrs):
    """
    Matches an IP address or subnet against a given sequence of IP addresses
    and subnets.

    :param ip: a single IP address or subnet.

    :param cidrs: a sequence of IP addresses and/or subnets.

    :return: the largest (least specific) matching IPAddress or IPNetwork
        object from the provided sequence, None if there was no match.
    """
    ...

def all_matching_cidrs(ip, cidrs):
    """
    Matches an IP address or subnet against a given sequence of IP addresses
    and subnets.

    :param ip: a single IP address.

    :param cidrs: a sequence of IP addresses and/or subnets.

    :return: all matching IPAddress and/or IPNetwork objects from the provided
        sequence, an empty list if there was no match.
    """
    ...

IPV4_LOOPBACK = IPNetwork("127.0.0.0/8")
IPV4_PRIVATE = (
    IPNetwork("10.0.0.0/8"),
    IPNetwork("100.64.0.0/10"),
    IPNetwork("172.16.0.0/12"),
    IPNetwork("192.0.0.0/24"),
    IPNetwork("192.168.0.0/16"),
    IPNetwork("198.18.0.0/15"),
    IPRange("239.0.0.0", "239.255.255.255"),
)
IPV4_LINK_LOCAL = IPNetwork("169.254.0.0/16")
IPV4_MULTICAST = IPNetwork("224.0.0.0/4")
IPV4_6TO4 = IPNetwork("192.88.99.0/24")
IPV4_RESERVED = (
    IPNetwork("0.0.0.0/8"),
    IPNetwork("192.0.2.0/24"),
    IPNetwork("240.0.0.0/4"),
    IPNetwork("198.51.100.0/24"),
    IPNetwork("203.0.113.0/24"),
    IPNetwork("233.252.0.0/24"),
    IPRange("234.0.0.0", "238.255.255.255"),
    IPRange("225.0.0.0", "231.255.255.255"),
) + (IPV4_LOOPBACK, IPV4_6TO4)
IPV6_LOOPBACK = IPAddress("::1")
IPV6_PRIVATE = (IPNetwork("fc00::/7"), IPNetwork("fec0::/10"))
IPV6_LINK_LOCAL = IPNetwork("fe80::/10")
IPV6_MULTICAST = IPNetwork("ff00::/8")
IPV6_RESERVED = (
    IPNetwork("ff00::/12"),
    IPNetwork("::/8"),
    IPNetwork("0100::/8"),
    IPNetwork("0200::/7"),
    IPNetwork("0400::/6"),
    IPNetwork("0800::/5"),
    IPNetwork("1000::/4"),
    IPNetwork("4000::/3"),
    IPNetwork("6000::/3"),
    IPNetwork("8000::/3"),
    IPNetwork("A000::/3"),
    IPNetwork("C000::/3"),
    IPNetwork("E000::/4"),
    IPNetwork("F000::/5"),
    IPNetwork("F800::/6"),
    IPNetwork("FE00::/9"),
)

