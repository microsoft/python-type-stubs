from ..metrics import DistanceMetric as _DistanceMetric

# TODO: Remove this file in 1.3
import warnings


class DistanceMetric(_DistanceMetric):
    @classmethod
    def get_metric(cls, metric, **kwargs):
        ...
