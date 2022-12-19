from sklearn.utils._estimator_html_repr import _VisualBlock
from typing import Literal, Sequence
from numpy.typing import ArrayLike
from contextlib import closing
from io import StringIO
from string import Template
import html

from .. import config_context

class _IDCounter:
    def __init__(self, prefix: str) -> None: ...
    def get_id(self): ...

_CONTAINER_ID_COUNTER = ...
_ESTIMATOR_ID_COUNTER = ...

class _VisualBlock:
    def __init__(
        self,
        kind: Literal["serial", "parallel", "single"],
        estimators: Sequence[Estimator | _VisualBlock] | Estimator,
        *,
        names: ArrayLike | None = None,
        name_details: Sequence[str] | str | None = None,
        dash_wrapped: bool = True,
    ): ...
    def _sk_visual_block_(self): ...

def _write_label_html(
    out,
    name,
    name_details,
    outer_class="sk-label-container",
    inner_class="sk-label",
    checked=False,
): ...
def _get_visual_block(estimator): ...
def _write_estimator_html(out, estimator, estimator_label, estimator_label_details, first_call=False): ...

_STYLE = ...  # noqa

def estimator_html_repr(estimator: Estimator) -> str: ...
