from typing import Any
from sympy.utilities import public

def dup_jacobi(n, a, b, K) -> list[Any]:
    ...

@public
def jacobi_poly(n, a, b, x=..., polys=...):
    ...

def dup_gegenbauer(n, a, K) -> list[Any]:
    ...

def gegenbauer_poly(n, a, x=..., polys=...):
    ...

def dup_chebyshevt(n, K) -> list[Any]:
    ...

def dup_chebyshevu(n, K) -> list[Any]:
    ...

@public
def chebyshevt_poly(n, x=..., polys=...):
    ...

@public
def chebyshevu_poly(n, x=..., polys=...):
    ...

def dup_hermite(n, K) -> list[Any]:
    ...

def dup_hermite_prob(n, K) -> list[Any]:
    ...

@public
def hermite_poly(n, x=..., polys=...):
    ...

@public
def hermite_prob_poly(n, x=..., polys=...):
    ...

def dup_legendre(n, K) -> list[Any]:
    ...

@public
def legendre_poly(n, x=..., polys=...):
    ...

def dup_laguerre(n, alpha, K) -> list[Any]:
    ...

@public
def laguerre_poly(n, x=..., alpha=..., polys=...):
    ...

def dup_spherical_bessel_fn(n, K) -> list[Any]:
    ...

def dup_spherical_bessel_fn_minus(n, K) -> list[Any]:
    ...

def spherical_bessel_fn(n, x=..., polys=...):
    ...

