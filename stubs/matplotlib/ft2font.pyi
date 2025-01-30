# Python: 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]
# Library: matplotlib, version: 3.4.0
# Module: matplotlib.ft2font, version: unspecified
import builtins as _mod_builtins
import typing

BOLD: int
EXTERNAL_STREAM: int
FAST_GLYPHS: int
FIXED_SIZES: int
FIXED_WIDTH: int

class FT2Font(_mod_builtins.object):
    
    def __init__(self, *args, **kwargs) -> None:
        
        ...

    @classmethod
    def __init_subclass__(cls) -> None:
        
        ...

    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        
        ...

    @property
    def ascender(self) -> typing.Any: ...
    @property
    def bbox(self) -> typing.Any: ...
    def clear(self) -> typing.Any:
        
        ...

    @property
    def descender(self) -> typing.Any: ...
    def draw_glyph_to_bitmap(self, bitmap, x, y, glyph) -> typing.Any:
        
        ...

    def draw_glyphs_to_bitmap(self) -> typing.Any:
        
        ...

    @property
    def face_flags(self) -> typing.Any: ...
    @property
    def family_name(self) -> typing.Any: ...
    @property
    def fname(self) -> typing.Any: ...
    def get_bitmap_offset(self) -> typing.Any:
        
        ...

    def get_char_index(self, codepoint) -> typing.Any:
        
        ...

    def get_charmap(self) -> typing.Any:
        
        ...

    def get_descent(self) -> typing.Any:
        
        ...

    def get_glyph_name(self, index) -> typing.Any:
        
        ...

    def get_image(self) -> typing.Any:
        
        ...

    def get_kerning(self, left, right, mode) -> typing.Any:
        
        ...

    def get_name_index(self, name) -> typing.Any:
        
        ...

    def get_num_glyphs(self) -> typing.Any:
        
        ...

    def get_path(self) -> typing.Any:
        
        ...

    def get_ps_font_info(self) -> typing.Any:
        
        ...

    def get_sfnt(self) -> typing.Any:
        
        ...

    def get_sfnt_table(self, name) -> typing.Any:
        
        ...

    def get_width_height(self) -> typing.Any:
        
        ...

    def get_xys(self) -> typing.Any:
        
        ...

    @property
    def height(self) -> typing.Any: ...
    def load_char(self, charcode, flags) -> typing.Any:
        
        ...

    def load_glyph(self, glyphindex, flags) -> typing.Any:
        
        ...

    @property
    def max_advance_height(self) -> typing.Any: ...
    @property
    def max_advance_width(self) -> typing.Any: ...
    @property
    def num_charmaps(self) -> typing.Any: ...
    @property
    def num_faces(self) -> typing.Any: ...
    @property
    def num_fixed_sizes(self) -> typing.Any: ...
    @property
    def num_glyphs(self) -> typing.Any: ...
    @property
    def postscript_name(self) -> typing.Any: ...
    @property
    def scalable(self) -> typing.Any: ...
    def select_charmap(self, i) -> typing.Any:
        
        ...

    def set_charmap(self, i) -> typing.Any:
        
        ...

    def set_size(self, ptsize, dpi) -> typing.Any:
        
        ...

    def set_text(self, string, angle, flags) -> typing.Any:
        
        ...

    @property
    def style_flags(self) -> typing.Any: ...
    @property
    def style_name(self) -> typing.Any: ...
    @property
    def underline_position(self) -> typing.Any: ...
    @property
    def underline_thickness(self) -> typing.Any: ...
    @property
    def units_per_EM(self) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

class FT2Image(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None:
        
        ...

    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        
        ...

    def draw_rect(self, x0, y0, x1, y1) -> typing.Any:
        
        ...

    def draw_rect_filled(self, x0, y0, x1, y1) -> typing.Any:
        
        ...

    def __getattr__(self, name) -> typing.Any: ...

GLYPH_NAMES: int
HORIZONTAL: int
ITALIC: int
KERNING: int
KERNING_DEFAULT: int
KERNING_UNFITTED: int
KERNING_UNSCALED: int
LOAD_CROP_BITMAP: int
LOAD_DEFAULT: int
LOAD_FORCE_AUTOHINT: int
LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH: int
LOAD_IGNORE_TRANSFORM: int
LOAD_LINEAR_DESIGN: int
LOAD_MONOCHROME: int
LOAD_NO_AUTOHINT: int
LOAD_NO_BITMAP: int
LOAD_NO_HINTING: int
LOAD_NO_RECURSE: int
LOAD_NO_SCALE: int
LOAD_PEDANTIC: int
LOAD_RENDER: int
LOAD_TARGET_LCD: int
LOAD_TARGET_LCD_V: int
LOAD_TARGET_LIGHT: int
LOAD_TARGET_MONO: int
LOAD_TARGET_NORMAL: int
LOAD_VERTICAL_LAYOUT: int
MULTIPLE_MASTERS: int
SCALABLE: int
SFNT: int
VERTICAL: int
__doc__: typing.Any
__file__: str
__freetype_build_type__: str
__freetype_version__: str
__name__: str
__package__: str

def __getattr__(name) -> typing.Any: ...
