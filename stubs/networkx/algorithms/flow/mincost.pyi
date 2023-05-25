from typing import Mapping
from ...classes.graph import Graph

__all__ = ["min_cost_flow_cost", "min_cost_flow", "cost_of_flow", "max_flow_min_cost"]

def min_cost_flow_cost(
    G: Graph, demand: str = "demand", capacity: str = "capacity", weight: str = "weight"
): ...
def min_cost_flow(
    G: Graph, demand: str = "demand", capacity: str = "capacity", weight: str = "weight"
) -> Mapping: ...
def cost_of_flow(G: Graph, flowDict: Mapping, weight: str = "weight"): ...
def max_flow_min_cost(
    G: Graph, s, t, capacity: str = "capacity", weight: str = "weight"
) -> Mapping: ...
