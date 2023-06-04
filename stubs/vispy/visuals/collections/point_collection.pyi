# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from .raw_point_collection import RawPointCollection
from .agg_point_collection import AggPointCollection

def PointCollection(mode="raw", *args, **kwargs): ...
