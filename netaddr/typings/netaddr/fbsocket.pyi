from typing import Literal

"""Fallback routines for Python's standard library socket module"""
AF_INET = 2
AF_INET6 = 10

def inet_ntoa(packed_ip: int) -> str:
    """
    Convert an IP address from 32-bit packed binary format to string format.
    """
    ...

def inet_ntop(af: Literal[2, 10], packed_ip: int) -> str:
    """Convert an packed IP address of the given family to string format."""
    ...

def inet_pton(af: Literal[2, 10], ip_string: str) -> str:
    """
    Convert an IP address from string format to a packed string suitable for
    use with low-level network functions.
    """
    ...

