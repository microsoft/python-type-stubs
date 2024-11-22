# TODO: Remove this file in 1.3

from ..metrics import DistanceMetric as _DistanceMetric

class DistanceMetric(_DistanceMetric):
    @classmethod
    def get_metric(cls, metric, **kwargs): ...
