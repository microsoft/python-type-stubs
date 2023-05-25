from typing import Callable

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import inspect as inspect

from .random import random as random
from .circular import circular as circular
from .force_directed import fruchterman_reingold as fruchterman_reingold
from .networkx_layout import NetworkxCoordinates as NetworkxCoordinates

_layout_map: dict = ...

AVAILABLE_LAYOUTS = ...

def get_layout(name: str, *args, **kwargs) -> Callable: ...
