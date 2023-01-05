from typing import Dict, Iterator, Optional, Union, Mapping, Literal
import os
from contextlib import contextmanager as contextmanager
import threading

_global_config: dict = ...
_threadlocal = ...

def _get_threadlocal_config() -> Dict[str, Union[bool, int, str]]: ...
def get_config() -> Mapping: ...
def set_config(
    assume_finite: bool | None = None,
    working_memory: int | None = None,
    print_changed_only: bool | None = None,
    display: Literal["text", "diagram"] | None = None,
    pairwise_dist_chunk_size: int | None = None,
    enable_cython_pairwise_dist: bool | None = None,
) -> None: ...
@contextmanager
def config_context(
    *,
    assume_finite: bool | None = None,
    working_memory: int | None = None,
    print_changed_only: bool | None = None,
    display: Literal["text", "diagram"] | None = None,
    pairwise_dist_chunk_size: int | None = None,
    enable_cython_pairwise_dist: bool | None = None,
) -> Iterator[None]: ...
