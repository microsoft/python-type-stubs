from typing import Any
from sympy.series.order import Order
from sympy.utilities import public

@public
def swinnerton_dyer_poly(n, x=..., polys=...) -> Any:
    ...

@public
def cyclotomic_poly(n, x=..., polys=...):
    ...

@public
def symmetric_poly(n, *gens, polys=...) -> Any | Order:
    ...

@public
def random_poly(x, n, inf, sup, domain=..., polys=...) -> Any:
    ...

@public
def interpolating_poly(n, x, X=..., Y=...) -> Order:
    ...

def fateman_poly_F_1(n) -> tuple[Any, Any, Any]:
    ...

def dmp_fateman_poly_F_1(n, K) -> tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]], list[list[Any]] | Any | list[Any]]:
    ...

def fateman_poly_F_2(n) -> tuple[Any, Any, Any]:
    ...

def dmp_fateman_poly_F_2(n, K) -> tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]], Any | list[list[Any]]]:
    ...

def fateman_poly_F_3(n) -> tuple[Any, Any, Any]:
    ...

def dmp_fateman_poly_F_3(n, K) -> tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]], Any | list[list[Any]]]:
    ...

def f_polys() -> tuple[Any, Any, Any, Any, Any, Any, Any]:
    ...

def w_polys() -> tuple[Any, Any]:
    ...

