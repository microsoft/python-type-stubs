# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ..util.event import Event

class SceneMouseEvent(Event):
    def __init__(self, event, visual): ...
    @property
    def visual(self): ...
    @visual.setter
    def visual(self, v): ...
    @property
    def pos(self): ...
    @property
    def last_event(self): ...
    @property
    def press_event(self): ...
    @property
    def button(self): ...
    @property
    def buttons(self): ...
    @property
    def delta(self): ...
    def copy(self): ...
