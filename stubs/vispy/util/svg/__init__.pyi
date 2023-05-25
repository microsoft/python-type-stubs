# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
from .svg import SVG as SVG
from .path import Path as Path  # noqa
from .base import namespace as namespace
from xml.etree import ElementTree as ElementTree

def Document(filename): ...
