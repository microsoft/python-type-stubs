# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

# Use OSX cocoa/quartz to get glyph bitmaps

from ctypes import byref, c_byte, c_int32

import numpy as np

from ...ext.cocoapy import (
    CFSTR,
    CFRange,
    CGGlyph,
    ObjCClass,
    UniChar,
    cf,
    ct,
    kCFNumberSInt32Type,
    kCGImageAlphaPremultipliedLast,
    kCTFontAttributeName,
    kCTFontBoldTrait,
    kCTFontFamilyNameAttribute,
    kCTFontItalicTrait,
    kCTFontSymbolicTrait,
    kCTFontTraitsAttribute,
    quartz,
)
from ._vispy_fonts import _get_vispy_font_filename, _vispy_fonts

_font_dict: dict = ...

def _load_vispy_font(face, bold, italic): ...
def _load_font(face, bold, italic): ...
def _load_glyph(f, char, glyphs_dict): ...
def _get_k_p_a(font, left, right): ...
def _list_fonts(): ...
