from typing import Any, Literal, Sequence
from ._reingold_tilford import buchheim as buchheim
from ..base import ClassifierMixin, RegressorMixin
from numpy import ndarray, longlong
from matplotlib.axes import Axes
from numbers import Integral as Integral
from io import StringIO as StringIO
from matplotlib.text import Annotation
from ..base import is_classifier as is_classifier
from ._classes import DecisionTreeClassifier
from .._typing import Int
from ._tree import Tree
from ..utils.validation import check_is_fitted as check_is_fitted

import numpy as np


class Sentinel:
    def __repr__(self) -> str:
        ...


SENTINEL = ...


def plot_tree(
    decision_tree: ClassifierMixin | DecisionTreeClassifier | RegressorMixin,
    *,
    max_depth: None | Int = None,
    feature_names: None | Sequence[str] = None,
    class_names: Sequence[str | bool] | None = None,
    label: Literal["all", "root", "none", "all"] = "all",
    filled: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rounded: bool = False,
    precision: Int = 3,
    ax: None | Axes = None,
    fontsize: None | Int = None,
) -> list[Annotation]:
    ...


class _BaseTreeExporter:
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
        filled: bool = False,
        impurity: bool = True,
        node_ids: bool = False,
        proportion: bool = False,
        rounded: bool = False,
        precision: int = 3,
        fontsize=None,
    ) -> None:
        ...

    def get_color(self, value: ndarray) -> str:
        ...

    def get_fill_color(self, tree: Tree, node_id: longlong | int) -> str:
        ...

    def node_to_str(self, tree: Tree, node_id: longlong | int, criterion: str) -> str:
        ...


class _DOTTreeExporter(_BaseTreeExporter):
    def __init__(
        self,
        out_file=...,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
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
    ) -> None:
        ...

    def export(self, decision_tree):
        ...

    def tail(self):
        ...

    def head(self):
        ...

    def recurse(self, tree, node_id, criterion, parent=None, depth: int = 0):
        ...


class _MPLTreeExporter(_BaseTreeExporter):
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
        filled: bool = False,
        impurity: bool = True,
        node_ids: bool = False,
        proportion: bool = False,
        rounded: bool = False,
        precision: int = 3,
        fontsize=None,
    ) -> None:
        ...

    def export(
        self, decision_tree: DecisionTreeClassifier, ax=None
    ) -> list[Annotation]:
        ...

    def recurse(self, node, tree, ax, max_x, max_y, depth: int = 0):
        ...


def export_graphviz(
    decision_tree: ClassifierMixin,
    out_file: Any = None,
    *,
    max_depth: None | Int = None,
    feature_names: None | Sequence[str] = None,
    class_names: Sequence[str | bool] | None = None,
    label: Literal["all", "root", "none", "all"] = "all",
    filled: bool = False,
    leaves_parallel: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rotate: bool = False,
    rounded: bool = False,
    special_characters: bool = False,
    precision: Int = 3,
    fontname: str = "helvetica",
) -> str:
    ...


def export_text(
    decision_tree: Any,
    *,
    feature_names: None | Sequence[str] = None,
    max_depth: Int = 10,
    spacing: Int = 3,
    decimals: Int = 2,
    show_weights: bool = False,
) -> str:
    ...
