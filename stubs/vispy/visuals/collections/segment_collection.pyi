# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
from .raw_segment_collection import RawSegmentCollection
from .agg_segment_collection import AggSegmentCollection

def SegmentCollection(mode="agg-fast", *args, **kwargs): ...
