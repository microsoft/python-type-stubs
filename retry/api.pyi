import logging
from typing import Any, Callable, Dict, List, Optional, Sequence, TypeVar, Union

logging_logger = logging.getLogger(__name__)
_T = TypeVar("_T", bound=Callable[..., Any])
_Decorator = Callable[[_T], _T]
_R = TypeVar("_R")


def retry_call(
    f: Callable[..., _R],
    fargs: List[Any] = ...,
    fkwargs: Dict[str, Any] = ...,
    exceptions: Union[Exception, Sequence[Exception]] = ...,
    tries: int = ...,
    delay: int = ...,
    max_delay: int = ...,
    backoff: int = ...,
    jitter: int = ...,
    logger: Optional[logging.Logger] = ...,
) -> _R:
    """
    Calls a function and re-executes it if it failed.

    :param f: the function to execute.
    :param fargs: the positional arguments of the function to execute.
    :param fkwargs: the named arguments of the function to execute.
    :param exceptions: an exception or a tuple of exceptions to catch. default: Exception.
    :param tries: the maximum number of attempts. default: -1 (infinite).
    :param delay: initial delay between attempts. default: 0.
    :param max_delay: the maximum value of delay. default: None (no limit).
    :param backoff: multiplier applied to delay between attempts. default: 1 (no backoff).
    :param jitter: extra seconds added to delay between attempts. default: 0.
                   fixed if a number, random if a range tuple (min, max)
    :param logger: logger.warning(fmt, error, delay) will be called on failed attempts.
                   default: retry.logging_logger. if None, logging is disabled.
    :returns: the result of the f function.
    """
    ...


def retry(
    exceptions: Union[Exception, Sequence[Exception]] = ...,
    tries: int = ...,
    delay: int = ...,
    max_delay: int = ...,
    backoff: int = ...,
    jitter: int = ...,
    logger: Optional[logging.Logger] = ...,
) -> _Decorator:
    """Returns a retry decorator.

    :param exceptions: an exception or a tuple of exceptions to catch. default: Exception.
    :param tries: the maximum number of attempts. default: -1 (infinite).
    :param delay: initial delay between attempts. default: 0.
    :param max_delay: the maximum value of delay. default: None (no limit).
    :param backoff: multiplier applied to delay between attempts. default: 1 (no backoff).
    :param jitter: extra seconds added to delay between attempts. default: 0.
                   fixed if a number, random if a range tuple (min, max)
    :param logger: logger.warning(fmt, error, delay) will be called on failed attempts.
                   default: retry.logging_logger. if None, logging is disabled.
    :returns: a retry decorator.
    """
    ...

