# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division as division

from . import base as base  # noqa
from ._default_app import create as create, process_events as process_events, quit as quit, run as run, use_app as use_app  # noqa
from .application import Application as Application  # noqa
from .canvas import Canvas as Canvas, KeyEvent as KeyEvent, MouseEvent as MouseEvent  # noqa
from .timer import Timer as Timer  # noqa
