import logging
import os
import threading
import time
from typing import Any, Optional, Type, Union
from types import TracebackType

"""
A platform independent file lock that supports the with-statement.
"""

def logger() -> logging.Logger:
    """Returns the logger instance used in this module."""
    ...

class Timeout(TimeoutError):
    """
    Raised when the lock could not be acquired in *timeout*
    seconds.
    """
    def __init__(self, lock_file: str) -> None: ...
    
    def __str__(self) -> str: ...
    

class _Acquire_ReturnProxy(object):

    def __init__(self, lock: str) -> None: ...

    def __enter__(self) -> str: ...

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...


class BaseFileLock(object):
    """
    Implements the base class of a file lock.
    """
    def __init__(self, lock_file: str, timeout: Union[float, int, str] =...) -> None: ...
    
    @property
    def lock_file(self) -> str:
        """
        The path to the lock file.
        """
        ...
    
    @property
    def timeout(self) -> float:
        """
        You can set a default timeout for the filelock. It will be used as
        fallback value in the acquire method, if no timeout value (*None*) is
        given.

        If you want to disable the timeout, set it to a negative value.

        A timeout of 0 means, that there is exactly one attempt to acquire the
        file lock.

        .. versionadded:: 2.0.0
        """
        ...
    
    @timeout.setter
    def timeout(self, value: Union[int, str, float]) -> None:
        """
        """
        ...
    
    
    @property
    def is_locked(self) -> bool:
        """
        True, if the object holds the file lock.

        .. versionchanged:: 2.0.0

            This was previously a method and is now a property.
        """
        ...
    
    def acquire(self, timeout: Optional[float] = ..., poll_intervall: float=...) -> _Acquire_ReturnProxy:
        """
        Acquires the file lock or fails with a :exc:`Timeout` error.

        .. code-block:: python

            # You can use this method in the context manager (recommended)
            with lock.acquire():
                pass

            # Or use an equivalent try-finally construct:
            lock.acquire()
            try:
                pass
            finally:
                lock.release()

        :arg float timeout:
            The maximum time waited for the file lock.
            If ``timeout < 0``, there is no timeout and this method will
            block until the lock could be acquired.
            If ``timeout`` is None, the default :attr:`~timeout` is used.

        :arg float poll_intervall:
            We check once in *poll_intervall* seconds if we can acquire the
            file lock.

        :raises Timeout:
            if the lock could not be acquired in *timeout* seconds.

        .. versionchanged:: 2.0.0

            This method returns now a *proxy* object instead of *self*,
            so that it can be used in a with statement without side effects.
        """
        ...
    
    def release(self, force: bool = ...) -> None:
        """
        Releases the file lock.

        Please note, that the lock is only completly released, if the lock
        counter is 0.

        Also note, that the lock file itself is not automatically deleted.

        :arg bool force:
            If true, the lock counter is ignored and the lock is released in
            every case.
        """
        ...
    
    def __enter__(self) -> BaseFileLock:
        ...
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], traceback: Optional[TracebackType]) -> None:
        ...
    
    def __del__(self) -> None:
        ...
    


class WindowsFileLock(BaseFileLock):
    """
    Uses the :func:`msvcrt.locking` function to hard lock the lock file on
    windows systems.
    """
    def _acquire(self) -> None:
        ...
    
    def _release(self) -> None:
        ...
    


class UnixFileLock(BaseFileLock):
    """
    Uses the :func:`fcntl.flock` to hard lock the lock file on unix systems.
    """
    def _acquire(self) -> None:
        ...
    
    def _release(self) -> None:
        ...
    


class SoftFileLock(BaseFileLock):
    """
    Simply watches the existence of the lock file.
    """
    def _acquire(self) -> None:
        ...
    
    def _release(self) -> None:
        ...
    
