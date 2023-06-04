# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

# Use OSX cocoa/quartz to get glyph bitmaps

import numpy as np
from ctypes import byref, c_int32, c_byte

from ...ext.cocoapy import (
    cf,
    ct,
    quartz,
    CFRange,
    CFSTR,
    CGGlyph,
    UniChar,
    kCTFontFamilyNameAttribute,
    kCTFontBoldTrait,
    kCTFontItalicTrait,
    kCTFontSymbolicTrait,
    kCTFontTraitsAttribute,
    kCTFontAttributeName,
    kCGImageAlphaPremultipliedLast,
    kCFNumberSInt32Type,
    ObjCClass,
)
from ._vispy_fonts import _vispy_fonts, _get_vispy_font_filename

_font_dict: dict = ...

def _load_vispy_font(face, bold, italic): ...
def _load_font(face, bold, italic): ...
def _load_glyph(f, char, glyphs_dict): ...
def _get_k_p_a(font, left, right): ...
def _list_fonts(): ...
