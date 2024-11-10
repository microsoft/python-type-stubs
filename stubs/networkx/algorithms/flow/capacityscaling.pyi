__all__ = ["capacity_scaling"]


from ...classes.graph import Graph

def capacity_scaling(
    G: Graph,
    demand: str = "demand",
    capacity: str = "capacity",
    weight: str = "weight",
    heap=...,
): ...
