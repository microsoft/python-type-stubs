import os
import threading
from contextlib import contextmanager as contextmanager
from typing import Iterator, Literal

from ._typing import Int

_global_config: dict = ...
_threadlocal = ...

def get_config() -> dict | dict[str, bool | int | str]: ...
def set_config(
    assume_finite: None | bool = None,
    working_memory: None | Int = None,
    print_changed_only: None | bool = None,
    display: None | Literal["text", "diagram"] = None,
    pairwise_dist_chunk_size: None | Int = None,
    enable_cython_pairwise_dist: None | bool = None,
    array_api_dispatch: None | bool = None,
    transform_output: None | str = None,
) -> None: ...
def config_context(
    *,
    assume_finite: None | bool = None,
    working_memory: None | Int = None,
    print_changed_only: None | bool = None,
    display: None | Literal["text", "diagram"] = None,
    pairwise_dist_chunk_size: None | Int = None,
    enable_cython_pairwise_dist: None | bool = None,
    array_api_dispatch: None | bool = None,
    transform_output: None | str = None,
) -> Iterator[None]: ...
