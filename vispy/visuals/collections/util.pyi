#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2013, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------

import numpy as np
from functools import reduce
from operator import mul

def dtype_reduce(dtype, level=0, depth=0): ...
def fetchcode(utype, prefix=""): ...
