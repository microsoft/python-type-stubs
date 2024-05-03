# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from . import gl as gl, util as util  # noqa
from .buffer import IndexBuffer as IndexBuffer, VertexBuffer as VertexBuffer  # noqa
from .context import (  # noqa
    GLContext as GLContext,
    get_current_canvas as get_current_canvas,
    get_default_config as get_default_config,
)
from .framebuffer import FrameBuffer as FrameBuffer, RenderBuffer as RenderBuffer  # noqa
from .globject import GLObject as GLObject  # noqa
from .program import Program as Program  # noqa
from .texture import (  # noqa
    Texture1D as Texture1D,
    Texture2D as Texture2D,
    Texture3D as Texture3D,
    TextureAtlas as TextureAtlas,
    TextureCube as TextureCube,
    TextureEmulated3D as TextureEmulated3D,
)
from .wrappers import *  # noqa
