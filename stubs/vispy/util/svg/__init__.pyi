# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
from xml.etree import ElementTree as ElementTree

from .base import namespace as namespace
from .path import Path as Path  # noqa
from .svg import SVG as SVG

def Document(filename): ...
