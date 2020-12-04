from . import base as base, collections as collections, exc as exc, interfaces as interfaces, state as state
from .. import util as util
from typing import Any, Optional

class ClassManager(dict):
    MANAGER_ATTR: Any = ...
    STATE_ATTR: Any = ...
    deferred_scalar_loader: Any = ...
    original_init: Any = ...
    factory: Any = ...
    class_: Any = ...
    info: Any = ...
    new_init: Any = ...
    local_attrs: Any = ...
    originals: Any = ...
    def __init__(self, class_: Any) -> None: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    @property
    def is_mapped(self): ...
    def mapper(self) -> None: ...
    def manage(self) -> None: ...
    def dispose(self) -> None: ...
    def manager_getter(self): ...
    def state_getter(self): ...
    def dict_getter(self): ...
    def instrument_attribute(self, key: Any, inst: Any, propagated: bool = ...) -> None: ...
    def subclass_managers(self, recursive: Any) -> None: ...
    def post_configure_attribute(self, key: Any) -> None: ...
    def uninstrument_attribute(self, key: Any, propagated: bool = ...) -> None: ...
    def unregister(self) -> None: ...
    def install_descriptor(self, key: Any, inst: Any) -> None: ...
    def uninstall_descriptor(self, key: Any) -> None: ...
    def install_member(self, key: Any, implementation: Any) -> None: ...
    def uninstall_member(self, key: Any) -> None: ...
    def instrument_collection_class(self, key: Any, collection_class: Any): ...
    def initialize_collection(self, key: Any, state: Any, factory: Any): ...
    def is_instrumented(self, key: Any, search: bool = ...): ...
    def get_impl(self, key: Any): ...
    @property
    def attributes(self): ...
    def new_instance(self, state: Optional[Any] = ...): ...
    def setup_instance(self, instance: Any, state: Optional[Any] = ...) -> None: ...
    def teardown_instance(self, instance: Any) -> None: ...
    def has_state(self, instance: Any): ...
    def has_parent(self, state: Any, key: Any, optimistic: bool = ...): ...
    def __bool__(self): ...
    __nonzero__: Any = ...

class _SerializeManager:
    class_: Any = ...
    def __init__(self, state: Any, d: Any) -> None: ...
    def __call__(self, state: Any, inst: Any, state_dict: Any) -> None: ...

class InstrumentationFactory:
    def create_manager_for_cls(self, class_: Any): ...
    def unregister(self, class_: Any) -> None: ...

instance_state: Any

instance_dict: Any
manager_of_class = base.manager_of_class

def register_class(class_: Any): ...
def unregister_class(class_: Any) -> None: ...
def is_instrumented(instance: Any, key: Any): ...