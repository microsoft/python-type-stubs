from . import attributes as attributes, path_registry as path_registry, strategy_options as strategy_options
from .. import util as util
from .util import state_str as state_str
from typing import Any, Optional

def instances(query: Any, cursor: Any, context: Any): ...
def merge_result(querylib: Any, query: Any, iterator: Any, load: bool = ...): ...
def get_from_identity(session: Any, mapper: Any, key: Any, passive: Any): ...
def load_on_ident(query: Any, key: Any, refresh_state: Optional[Any] = ..., with_for_update: Optional[Any] = ..., only_load_props: Optional[Any] = ...): ...
def load_on_pk_identity(query: Any, primary_key_identity: Any, refresh_state: Optional[Any] = ..., with_for_update: Optional[Any] = ..., only_load_props: Optional[Any] = ..., identity_token: Optional[Any] = ...): ...

class PostLoad:
    loaders: Any = ...
    states: Any = ...
    load_keys: Any = ...
    def __init__(self) -> None: ...
    def add_state(self, state: Any, overwrite: Any) -> None: ...
    def invoke(self, context: Any, path: Any) -> None: ...
    @classmethod
    def for_context(cls, context: Any, path: Any, only_load_props: Any): ...
    @classmethod
    def path_exists(self, context: Any, path: Any, key: Any): ...
    @classmethod
    def callable_for_path(cls, context: Any, path: Any, limit_to_mapper: Any, token: Any, loader_callable: Any, *arg: Any, **kw: Any) -> None: ...

def load_scalar_attributes(mapper: Any, state: Any, attribute_names: Any) -> None: ...
