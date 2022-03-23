from lxml.etree import _Element
from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.text import RichText
from openpyxl.chart.title import Title
from typing import (
    Optional,
    Union,
)

class ChartLines:
    def __init__(self, spPr: Optional[GraphicalProperties] = ...) -> None: ...

class DateAxis:
    def __init__(
        self,
        auto: Optional[Union[str, bool]] = ...,
        lblOffset: Optional[Union[str, int]] = ...,
        baseTimeUnit: Optional[str] = ...,
        majorUnit: Optional[str] = ...,
        majorTimeUnit: Optional[str] = ...,
        minorUnit: None = ...,
        minorTimeUnit: None = ...,
        extLst: None = ...,
        **kw
    ) -> None: ...

class DisplayUnitsLabel:
    def __init__(
        self, layout: None = ..., tx: None = ..., spPr: None = ..., txPr: None = ...
    ) -> None: ...

class DisplayUnitsLabelList:
    def __init__(
        self,
        custUnit: None = ...,
        builtInUnit: Optional[str] = ...,
        dispUnitsLbl: None = ...,
        extLst: None = ...,
    ) -> None: ...

class NumericAxis:
    def __init__(
        self,
        crossBetween: Optional[str] = ...,
        majorUnit: Optional[str] = ...,
        minorUnit: Optional[str] = ...,
        dispUnits: Optional[DisplayUnitsLabelList] = ...,
        extLst: None = ...,
        **kw
    ) -> None: ...
    @classmethod
    def from_tree(cls, node: _Element) -> NumericAxis: ...

class Scaling:
    def __init__(
        self,
        logBase: Optional[Union[str, int]] = ...,
        orientation: str = ...,
        max: Optional[str] = ...,
        min: Optional[str] = ...,
        extLst: None = ...,
    ) -> None: ...

class SeriesAxis:
    def __init__(
        self,
        tickLblSkip: None = ...,
        tickMarkSkip: None = ...,
        extLst: None = ...,
        **kw
    ) -> None: ...

class TextAxis:
    def __init__(
        self,
        auto: Optional[str] = ...,
        lblAlgn: Optional[str] = ...,
        lblOffset: Optional[Union[str, int]] = ...,
        tickLblSkip: None = ...,
        tickMarkSkip: None = ...,
        noMultiLvlLbl: Optional[str] = ...,
        extLst: None = ...,
        **kw
    ) -> None: ...

class _BaseAxis:
    def __init__(
        self,
        axId: Optional[Union[str, int]] = ...,
        scaling: Optional[Scaling] = ...,
        delete: Optional[Union[str, bool]] = ...,
        axPos: str = ...,
        majorGridlines: Optional[ChartLines] = ...,
        minorGridlines: None = ...,
        title: Optional[Title] = ...,
        numFmt: Optional[NumFmt] = ...,
        majorTickMark: Optional[str] = ...,
        minorTickMark: Optional[str] = ...,
        tickLblPos: Optional[str] = ...,
        spPr: Optional[GraphicalProperties] = ...,
        txPr: Optional[RichText] = ...,
        crossAx: Optional[Union[str, int]] = ...,
        crosses: Optional[str] = ...,
        crossesAt: Optional[str] = ...,
    ) -> None: ...
