from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import base64
import logging
import sys
import inspect
import re
import traceback
import json
from functools import partial

import numpy as np
from numpy.typing import ArrayLike

###############################################################################
# LOGGING (some adapted from mne-python)

def _get_vispy_caller(): ...

# class _WrapStdOut(object):
#     """Class to work around how doctest captures stdout"""
#     def __getattr__(self, name):
#         # Even more ridiculous than this class, this must be sys.stdout (not
#         # just stdout) in order for this to work (tested on OSX and Linux)
#         return getattr(sys.stdout, name)

class _VispyFormatter(logging.Formatter):
    def __init__(self): ...
    def _vispy_set_prepend(self, prepend): ...
    def format(self, record): ...

class _VispyStreamHandler(logging.StreamHandler):
    def __init__(self): ...
    def _vispy_emit_match_andor_record(self, record): ...
    def _vispy_set_match(self, match): ...
    def _vispy_set_emit_record(self, record): ...
    def _vispy_reset_list(self): ...

logger = ...
_lf = ...
_lh = ...  # needs _lf to exist

logging_types = ...

def set_log_level(verbose: bool | str | int | None, match: str | None = None, return_old: bool = False): ...

class use_log_level(object):

    # This method mostly wraps to set_log_level, but also takes
    # care of enabling/disabling message recording in the formatter.

    def __init__(
        self,
        level: str,
        match: str | None = None,
        record: bool = False,
        print_msg: bool = True,
    ): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

def log_exception(level: str = "warning", tb_skip: int = 2): ...

logger.log_exception = ...  # make this easier to reach

def _handle_exception(ignore_callback_errors, print_callback_errors, obj, cb_event=None, node=None): ...
def _serialize_buffer(buffer, array_serialization=None): ...

class NumPyJSONEncoder(json.JSONEncoder):
    def default(self, obj): ...
