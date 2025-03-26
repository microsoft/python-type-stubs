# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .application import Application

# Initialize default app
# Only for use within *this* module.
# One should always call use_app() to obtain the default app.
default_app: None = ...

def use_app(backend_name: str | None = None, call_reuse: bool = True): ...
def create(): ...
def run(): ...
def quit(): ...
def process_events(): ...
