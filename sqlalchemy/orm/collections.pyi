from typing import Any, Optional

class _PlainColumnGetter:
    cols: Any = ...
    composite: Any = ...
    def __init__(self, cols: Any) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value: Any): ...

class _SerializableColumnGetter:
    colkeys: Any = ...
    composite: Any = ...
    def __init__(self, colkeys: Any) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value: Any): ...

class _SerializableColumnGetterV2(_PlainColumnGetter):
    colkeys: Any = ...
    composite: Any = ...
    def __init__(self, colkeys: Any) -> None: ...
    def __reduce__(self): ...

def column_mapped_collection(mapping_spec: Any): ...

class _SerializableAttrGetter:
    name: Any = ...
    getter: Any = ...
    def __init__(self, name: Any) -> None: ...
    def __call__(self, target: Any): ...
    def __reduce__(self): ...

def attribute_mapped_collection(attr_name: Any): ...
def mapped_collection(keyfunc: Any): ...

class collection:
    @staticmethod
    def appender(fn: Any): ...
    @staticmethod
    def remover(fn: Any): ...
    @staticmethod
    def iterator(fn: Any): ...
    @staticmethod
    def internally_instrumented(fn: Any): ...
    @staticmethod
    def linker(fn: Any): ...
    link: Any = ...
    @staticmethod
    def converter(fn: Any): ...
    @staticmethod
    def adds(arg: Any): ...
    @staticmethod
    def replaces(arg: Any): ...
    @staticmethod
    def removes(arg: Any): ...
    @staticmethod
    def removes_return(): ...

collection_adapter: Any

class CollectionAdapter:
    attr: Any = ...
    owner_state: Any = ...
    invalidated: bool = ...
    def __init__(self, attr: Any, owner_state: Any, data: Any) -> None: ...
    @property
    def data(self): ...
    def bulk_appender(self): ...
    def append_with_event(self, item: Any, initiator: Optional[Any] = ...) -> None: ...
    def append_without_event(self, item: Any) -> None: ...
    def append_multiple_without_event(self, items: Any) -> None: ...
    def bulk_remover(self): ...
    def remove_with_event(self, item: Any, initiator: Optional[Any] = ...) -> None: ...
    def remove_without_event(self, item: Any) -> None: ...
    def clear_with_event(self, initiator: Optional[Any] = ...) -> None: ...
    def clear_without_event(self) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def fire_append_event(self, item: Any, initiator: Optional[Any] = ...): ...
    def fire_remove_event(self, item: Any, initiator: Optional[Any] = ...) -> None: ...
    def fire_pre_remove_event(self, initiator: Optional[Any] = ...) -> None: ...

class InstrumentedList(list): ...
class InstrumentedSet(set): ...
class InstrumentedDict(dict): ...

class MappedCollection(dict):
    keyfunc: Any = ...
    def __init__(self, keyfunc: Any) -> None: ...
    def set(self, value: Any, _sa_initiator: Optional[Any] = ...) -> None: ...
    def remove(self, value: Any, _sa_initiator: Optional[Any] = ...) -> None: ...
