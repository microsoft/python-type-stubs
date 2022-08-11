from typing import Callable, Iterator

from contextlib import contextmanager

import tensorflow as tf

def scalar(name: str, data: float | tf.Tensor, step: int | None = None, description: str | None = None) -> bool: ...
@contextmanager
def record_if(condition: bool | tf.Tensor | Callable[[], bool]) -> Iterator[None]: ...
