from typing import Callable, Type, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")

def run_all_in_graph_and_eager_modes(cls: Type[T]) -> Type[T]: ...
def run_in_graph_and_eager_modes(func: Callable[P, R]) -> Callable[P, R]: ...
