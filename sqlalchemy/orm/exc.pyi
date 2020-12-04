from .. import exc as sa_exc, util as util
from typing import Any, Optional

NO_STATE: Any

class StaleDataError(sa_exc.SQLAlchemyError): ...
ConcurrentModificationError = StaleDataError

class FlushError(sa_exc.SQLAlchemyError): ...
class UnmappedError(sa_exc.InvalidRequestError): ...
class ObjectDereferencedError(sa_exc.SQLAlchemyError): ...

class DetachedInstanceError(sa_exc.SQLAlchemyError):
    code: str = ...

class UnmappedInstanceError(UnmappedError):
    def __init__(self, base: Any, obj: Any, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedClassError(UnmappedError):
    def __init__(self, cls: Any, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class ObjectDeletedError(sa_exc.InvalidRequestError):
    def __init__(self, base: Any, state: Any, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedColumnError(sa_exc.InvalidRequestError): ...
class NoResultFound(sa_exc.InvalidRequestError): ...
class MultipleResultsFound(sa_exc.InvalidRequestError): ...

class LoaderStrategyException(sa_exc.InvalidRequestError):
    def __init__(self, applied_to_property_type: Any, requesting_property: Any, applies_to: Any, actual_strategy_type: Any, strategy_key: Any) -> None: ...
