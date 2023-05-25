# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
from .raw_path_collection import RawPathCollection
from .agg_path_collection import AggPathCollection
from .agg_fast_path_collection import AggFastPathCollection

def PathCollection(mode="agg", *args, **kwargs): ...
