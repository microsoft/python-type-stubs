from ._self_training import SelfTrainingClassifier as SelfTrainingClassifier
from ._label_propagation import (
    LabelPropagation as LabelPropagation,
    LabelSpreading as LabelSpreading,
)

__all__ = ["SelfTrainingClassifier", "LabelPropagation", "LabelSpreading"]
