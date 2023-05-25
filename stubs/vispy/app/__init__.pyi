# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division as division

from .application import Application as Application  # noqa
from ._default_app import (
    use_app as use_app,
    create as create,
    run as run,
    quit as quit,
    process_events as process_events,
)  # noqa
from .canvas import (
    Canvas as Canvas,
    MouseEvent as MouseEvent,
    KeyEvent as KeyEvent,
)  # noqa
from .timer import Timer as Timer  # noqa
from . import base as base  # noqa
