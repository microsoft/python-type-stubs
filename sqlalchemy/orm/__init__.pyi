from ..util.langhelpers import public_factory as public_factory
from .deprecated_interfaces import AttributeExtension as AttributeExtension, MapperExtension as MapperExtension, SessionExtension as SessionExtension
from .descriptor_props import ComparableProperty as ComparableProperty, CompositeProperty as CompositeProperty, SynonymProperty as SynonymProperty
from .interfaces import EXT_CONTINUE as EXT_CONTINUE, EXT_SKIP as EXT_SKIP, EXT_STOP as EXT_STOP, PropComparator as PropComparator
from .mapper import Mapper as Mapper, class_mapper as class_mapper, configure_mappers as configure_mappers, reconstructor as reconstructor, validates as validates
from .properties import ColumnProperty as ColumnProperty
from .query import AliasOption as AliasOption, Bundle as Bundle, Query as Query
from .relationships import RelationshipProperty as RelationshipProperty, foreign as foreign, remote as remote
from .scoping import scoped_session as scoped_session
from .session import Session as Session, close_all_sessions as close_all_sessions, make_transient as make_transient, make_transient_to_detached as make_transient_to_detached, object_session as object_session, sessionmaker as sessionmaker
from .strategy_options import Load as Load
from .util import aliased as aliased, join as join, object_mapper as object_mapper, outerjoin as outerjoin, polymorphic_union as polymorphic_union, was_deleted as was_deleted, with_parent as with_parent, with_polymorphic as with_polymorphic
from typing import Any, Optional

def create_session(bind: Optional[Any] = ..., **kwargs: Any): ...

relationship: Any

def relation(*arg: Any, **kw: Any): ...
def dynamic_loader(argument: Any, **kw: Any): ...

column_property: Any
composite: Any

def backref(name: Any, **kwargs: Any): ...
def deferred(*columns: Any, **kw: Any): ...
def query_expression(default_expr: Any = ...): ...

mapper: Any
synonym: Any
comparable_property: Any

def compile_mappers() -> None: ...
def clear_mappers() -> None: ...

joinedload: Any
joinedload_all: Any
contains_eager: Any
defer: Any
undefer: Any
undefer_group: Any
with_expression: Any
load_only: Any
lazyload: Any
lazyload_all: Any
subqueryload: Any
subqueryload_all: Any
selectinload: Any
selectinload_all: Any
immediateload: Any
noload: Any
raiseload: Any
defaultload: Any
selectin_polymorphic: Any

def eagerload(*args: Any, **kwargs: Any): ...
def eagerload_all(*args: Any, **kwargs: Any): ...

contains_alias: Any
