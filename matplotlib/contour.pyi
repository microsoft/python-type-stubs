from typing import Any

from matplotlib.cm import ScalarMappable


class ContourLabeler:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ContourSet(ScalarMappable, ContourLabeler):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class QuadContourSet(ContourSet):
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
