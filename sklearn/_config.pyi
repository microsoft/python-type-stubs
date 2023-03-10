from typing import Iterator, Literal
from contextlib import contextmanager as contextmanager
from ._typing import Int
import os
import threading

_global_config: dict = ...
_threadlocal = ...


def get_config() -> dict[str, int | bool | str] | dict:
    ...


def set_config(
    assume_finite: bool | None = None,
    working_memory: None | Int = None,
    print_changed_only: bool | None = None,
    display: Literal["text", "diagram"] | None = None,
    pairwise_dist_chunk_size: None | Int = None,
    enable_cython_pairwise_dist: bool | None = None,
    array_api_dispatch: bool | None = None,
    transform_output: str | None = None,
) -> None:
    ...


def config_context(
    *,
    assume_finite: bool | None = None,
    working_memory: None | Int = None,
    print_changed_only: bool | None = None,
    display: Literal["text", "diagram"] | None = None,
    pairwise_dist_chunk_size: None | Int = None,
    enable_cython_pairwise_dist: bool | None = None,
    array_api_dispatch: bool | None = None,
    transform_output: str | None = None,
) -> Iterator[None]:
    ...
