from typing import Any
from sympy.core.numbers import Integer, Rational

def convolution(a, b, cycle=..., dps=..., prime=..., dyadic=..., subset=...) -> list[int] | list[Any | int] | Any | list[Any]:
    ...

def convolution_fft(a, b, dps=...) -> list[Any] | Any:
    ...

def convolution_ntt(a, b, prime) -> list[int] | list[Any | int] | Any:
    ...

def convolution_fwht(a, b) -> list[Any] | Any:
    ...

def convolution_subset(a, b) -> list[Any] | Any:
    ...

def covering_product(a, b) -> list[Any] | Any:
    ...

def intersecting_product(a, b) -> list[Any] | Any:
    ...

