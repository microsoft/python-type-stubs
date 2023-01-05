from typing import Sequence, Literal, Any
from numpy.typing import ArrayLike

# Authors: Gilles Louppe <g.louppe@gmail.com>
#          Peter Prettenhofer <peter.prettenhofer@gmail.com>
#          Brian Holt <bdholt1@gmail.com>
#          Noel Dawe <noel@dawe.me>
#          Satrajit Gosh <satrajit.ghosh@gmail.com>
#          Trevor Stephens <trev.stephens@gmail.com>
#          Li Li <aiki.nogard@gmail.com>
#          Giuseppe Vettigli <vettigli@gmail.com>
# License: BSD 3 clause
from io import StringIO
from numbers import Integral

import numpy as np

from ..utils.validation import check_is_fitted
from ..base import is_classifier

from . import _criterion
from . import _tree
from ._reingold_tilford import buchheim, Tree
from . import DecisionTreeClassifier

def _color_brew(n): ...

class Sentinel:
    def __repr__(self): ...

SENTINEL = ...

def plot_tree(
    decision_tree: Regressor | Classifier,
    *,
    max_depth: int | None = None,
    feature_names: ArrayLike | None = None,
    class_names: Sequence[str] | bool | None = None,
    label: Literal["all", "root", "none"] = "all",
    filled: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rounded: bool = False,
    precision: int = 3,
    ax: Axis | None = None,
    fontsize: int | None = None,
) -> list[Artist]: ...

class _BaseTreeExporter:
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label="all",
        filled=False,
        impurity=True,
        node_ids=False,
        proportion=False,
        rounded=False,
        precision=3,
        fontsize=None,
    ): ...
    def get_color(self, value): ...
    def get_fill_color(self, tree, node_id): ...
    def node_to_str(self, tree, node_id, criterion): ...

class _DOTTreeExporter(_BaseTreeExporter):
    def __init__(
        self,
        out_file=...,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label="all",
        filled=False,
        leaves_parallel=False,
        impurity=True,
        node_ids=False,
        proportion=False,
        rotate=False,
        rounded=False,
        special_characters=False,
        precision=3,
        fontname="helvetica",
    ): ...
    def export(self, decision_tree): ...
    def tail(self): ...
    def head(self): ...
    def recurse(self, tree, node_id, criterion, parent=None, depth=0): ...

class _MPLTreeExporter(_BaseTreeExporter):
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label="all",
        filled=False,
        impurity=True,
        node_ids=False,
        proportion=False,
        rounded=False,
        precision=3,
        fontsize=None,
    ): ...
    def _make_tree(self, node_id, et, criterion, depth=0): ...
    def export(self, decision_tree, ax=None): ...
    def recurse(self, node, tree, ax, max_x, max_y, depth=0): ...

def export_graphviz(
    decision_tree: Classifier,
    out_file: Any | str | None = None,
    *,
    max_depth: int | None = None,
    feature_names: ArrayLike | None = None,
    class_names: Sequence[str] | bool | None = None,
    label: Literal["all", "root", "none"] = "all",
    filled: bool = False,
    leaves_parallel: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rotate: bool = False,
    rounded: bool = False,
    special_characters: bool = False,
    precision: int = 3,
    fontname: str = "helvetica",
) -> str: ...
def _compute_depth(tree, node): ...
def export_text(
    decision_tree: Any,
    *,
    feature_names: ArrayLike | None = None,
    max_depth: int = 10,
    spacing: int = 3,
    decimals: int = 2,
    show_weights: bool = False,
) -> str: ...
