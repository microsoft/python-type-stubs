from typing import Literal, Sequence
from string import Template as Template
from contextlib import closing as closing
from ..base import BaseEstimator
from io import StringIO as StringIO
from inspect import isclass as isclass
from .. import config_context as config_context
import html


class _IDCounter:
    def __init__(self, prefix: str) -> None:
        ...

    def get_id(self):
        ...


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
        dash_wrapped: bool = True
    ) -> None:
        ...


_STYLE = ...  # noqa


def estimator_html_repr(estimator: BaseEstimator) -> str:
    ...
