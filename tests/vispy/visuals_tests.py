from typing_extensions import assert_type

from vispy.scene.events import SceneMouseEvent
from vispy.util.keys import Key
from vispy.visuals import LineVisual, MarkersVisual, TextVisual


def check_visual_properties(text: TextVisual, line: LineVisual, markers: MarkersVisual, event: SceneMouseEvent) -> None:
    assert_type(text.line_height, float)
    assert_type(text.scaling, bool)
    assert_type(line.line_caps, tuple[str, str])
    assert_type(markers.canvas_size_limits, tuple[float | None, float | None] | list[float | None] | None)
    assert_type(event.modifiers, tuple[Key, ...])

    text.line_height = 1.5
    text.scaling = True
    line.line_caps = ("round", "square")
    markers.canvas_size_limits = (None, 20.0)
    markers.canvas_size_limits = [5.0, None]
    markers.canvas_size_limits = None

    assert_type(TextVisual("multiline\ntext", line_height=1.5, scaling=True), TextVisual)
    assert_type(LineVisual(method="agg", line_caps=("round", "square")), LineVisual)
