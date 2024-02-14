import html
from contextlib import closing as closing
from inspect import isclass as isclass
from io import StringIO as StringIO
from string import Template as Template
from typing import Literal, Sequence

from .. import config_context as config_context
from ..base import BaseEstimator

class _IDCounter:
    def __init__(self, prefix: str) -> None: ...
    def get_id(self): ...

_CONTAINER_ID_COUNTER = ...
_ESTIMATOR_ID_COUNTER = ...

class _VisualBlock:
    def __init__(
        self,
        kind: Literal["serial", "parallel", "single"],
        estimators: Sequence[BaseEstimator] | BaseEstimator | Sequence[_VisualBlock],
        *,
        names: None | Sequence[str] = None,
        name_details: Sequence[str] | None | str = None,
        dash_wrapped: bool = True,
    ) -> None: ...

_STYLE = ...  # noqa

def estimator_html_repr(estimator: BaseEstimator) -> str: ...
