import numpy as np
from sklearn.base import BaseEstimator
from typing import Optional

_DEFAULT_TAGS: dict = ...

def _safe_tags(estimator: BaseEstimator, key: Optional[str] = None) -> bool: ...
