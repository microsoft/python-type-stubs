from sympy.calculus.accumulationbounds import AccumulationBounds
from sympy.core.basic import Basic
from sympy.series.order import Order

def difference_delta(expr, n=..., step=...):
    ...

def dominant(expr, n) -> Basic | None:
    ...

def limit_seq(expr, n=..., trials=...) -> AccumulationBounds | Order | None:
    ...

