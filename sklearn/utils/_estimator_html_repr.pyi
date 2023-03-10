from typing import Literal, Sequence
from inspect import isclass as isclass
from .._typing import Estimator
from contextlib import closing as closing
from io import StringIO as StringIO
from .. import config_context as config_context
from string import Template as Template
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
        estimators: Estimator | Sequence[_VisualBlock] | Sequence[Estimator],
        *,
        names: Sequence[str] | None = None,
        name_details: Sequence[str] | str | None = None,
        dash_wrapped: bool = True
    ) -> None:
        ...


_STYLE = ...  # noqa


def estimator_html_repr(estimator: Estimator) -> str:
    ...
