# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from os import PathLike

# List the vispy fonts made available online
_vispy_fonts = ...

def _get_vispy_font_filename(face, bold, italic): ...
def register_vispy_font(path: str | PathLike[str], face: str, bold: bool, italic: bool) -> None: ...
