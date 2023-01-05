import typing as typing

from ._split import BaseCrossValidator as BaseCrossValidator
from ._split import BaseShuffleSplit as BaseShuffleSplit
from ._split import KFold as KFold
from ._split import GroupKFold as GroupKFold
from ._split import StratifiedKFold as StratifiedKFold
from ._split import TimeSeriesSplit as TimeSeriesSplit
from ._split import LeaveOneGroupOut as LeaveOneGroupOut
from ._split import LeaveOneOut as LeaveOneOut
from ._split import LeavePGroupsOut as LeavePGroupsOut
from ._split import LeavePOut as LeavePOut
from ._split import RepeatedKFold as RepeatedKFold
from ._split import RepeatedStratifiedKFold as RepeatedStratifiedKFold
from ._split import ShuffleSplit as ShuffleSplit
from ._split import GroupShuffleSplit as GroupShuffleSplit
from ._split import StratifiedShuffleSplit as StratifiedShuffleSplit
from ._split import StratifiedGroupKFold as StratifiedGroupKFold
from ._split import PredefinedSplit as PredefinedSplit
from ._split import train_test_split as train_test_split
from ._split import check_cv as check_cv

from ._validation import cross_val_score as cross_val_score
from ._validation import cross_val_predict as cross_val_predict
from ._validation import cross_validate as cross_validate
from ._validation import learning_curve as learning_curve
from ._validation import permutation_test_score as permutation_test_score
from ._validation import validation_curve as validation_curve

from ._search import GridSearchCV as GridSearchCV
from ._search import RandomizedSearchCV as RandomizedSearchCV
from ._search import ParameterGrid as ParameterGrid
from ._search import ParameterSampler as ParameterSampler

__all__ = [
    "BaseCrossValidator",
    "BaseShuffleSplit",
    "GridSearchCV",
    "TimeSeriesSplit",
    "KFold",
    "GroupKFold",
    "GroupShuffleSplit",
    "LeaveOneGroupOut",
    "LeaveOneOut",
    "LeavePGroupsOut",
    "LeavePOut",
    "RepeatedKFold",
    "RepeatedStratifiedKFold",
    "ParameterGrid",
    "ParameterSampler",
    "PredefinedSplit",
    "RandomizedSearchCV",
    "ShuffleSplit",
    "StratifiedKFold",
    "StratifiedGroupKFold",
    "StratifiedShuffleSplit",
    "check_cv",
    "cross_val_predict",
    "cross_val_score",
    "cross_validate",
    "learning_curve",
    "permutation_test_score",
    "train_test_split",
    "validation_curve",
]

# TODO: remove this check once the estimator is no longer experimental.
def __getattr__(name: str): ...
