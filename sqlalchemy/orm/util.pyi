from . import attributes as attributes
from .. import event as event, inspection as inspection, sql as sql, util as util
from ..sql import expression as expression, util as sql_util
from .base import InspectionAttr as InspectionAttr, attribute_str as attribute_str, class_mapper as class_mapper, instance_str as instance_str, object_mapper as object_mapper, object_state as object_state, state_attribute_str as state_attribute_str, state_class_str as state_class_str, state_str as state_str
from .interfaces import MapperProperty as MapperProperty, PropComparator as PropComparator
from .path_registry import PathRegistry as PathRegistry
from typing import Any, Optional

all_cascades: Any

class CascadeOptions(frozenset):
    save_update: Any = ...
    delete: Any = ...
    refresh_expire: Any = ...
    merge: Any = ...
    expunge: Any = ...
    delete_orphan: Any = ...
    def __new__(cls, value_list: Any): ...
    @classmethod
    def from_string(cls, arg: Any): ...

def polymorphic_union(table_map: Any, typecolname: Any, aliasname: str = ..., cast_nulls: bool = ...): ...
def identity_key(*args: Any, **kwargs: Any): ...

class ORMAdapter(sql_util.ColumnAdapter):
    mapper: Any = ...
    aliased_class: Any = ...
    def __init__(self, entity: Any, equivalents: Optional[Any] = ..., adapt_required: bool = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ...) -> None: ...

class AliasedClass:
    __name__: Any = ...
    def __init__(self, cls: Any, alias: Optional[Any] = ..., name: Optional[Any] = ..., flat: bool = ..., adapt_on_names: bool = ..., with_polymorphic_mappers: Any = ..., with_polymorphic_discriminator: Optional[Any] = ..., base_alias: Optional[Any] = ..., use_mapper_path: bool = ..., represents_outer_join: bool = ...) -> None: ...
    def __getattr__(self, key: Any): ...

class AliasedInsp(InspectionAttr):
    mapper: Any = ...
    selectable: Any = ...
    name: Any = ...
    polymorphic_on: Any = ...
    represents_outer_join: Any = ...
    with_polymorphic_mappers: Any = ...
    def __init__(self, entity: Any, mapper: Any, selectable: Any, name: Any, with_polymorphic_mappers: Any, polymorphic_on: Any, _base_alias: Any, _use_mapper_path: Any, adapt_on_names: Any, represents_outer_join: Any) -> None: ...
    @property
    def entity(self): ...
    is_aliased_class: bool = ...
    @property
    def class_(self): ...

def aliased(element: Any, alias: Optional[Any] = ..., name: Optional[Any] = ..., flat: bool = ..., adapt_on_names: bool = ...): ...
def with_polymorphic(base: Any, classes: Any, selectable: bool = ..., flat: bool = ..., polymorphic_on: Optional[Any] = ..., aliased: bool = ..., innerjoin: bool = ..., _use_mapper_path: bool = ..., _existing_alias: Optional[Any] = ...): ...

class _ORMJoin(expression.Join):
    __visit_name__: Any = ...
    onclause: Any = ...
    def __init__(self, left: Any, right: Any, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., _left_memo: Optional[Any] = ..., _right_memo: Optional[Any] = ...) -> None: ...
    def join(self, right: Any, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
    def outerjoin(self, right: Any, onclause: Optional[Any] = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...

def join(left: Any, right: Any, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
def outerjoin(left: Any, right: Any, onclause: Optional[Any] = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
def with_parent(instance: Any, prop: Any, from_entity: Optional[Any] = ...): ...
def has_identity(object_: Any): ...
def was_deleted(object_: Any): ...
def randomize_unitofwork() -> None: ...
