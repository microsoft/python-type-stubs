"""
Classic deprecation warning
===========================

Classic ``@deprecated`` decorator to deprecate old python classes, functions or methods.

.. _The Warnings Filter: https://docs.python.org/3/library/warnings.html#the-warnings-filter
"""

from typing import (
    Any,
    Callable,
    Optional,
    Type,
    TypeVar,
)

_T = TypeVar("_T", bound=Callable[..., Any])

class ClassicAdapter:
    """
    Classic adapter -- *for advanced usage only*

    This adapter is used to get the deprecation message according to the wrapped object type:
    class, function, standard method, static method, or class method.

    This is the base class of the :class:`~deprecated.sphinx.SphinxAdapter` class
    which is used to update the wrapped object docstring.

    You can also inherit this class to change the deprecation message.

    In the following example, we change the message into "The ... is deprecated.":

    .. code-block:: python

       import inspect

       from deprecated.classic import ClassicAdapter
       from deprecated.classic import deprecated


       class MyClassicAdapter(ClassicAdapter):
           def get_deprecated_msg(self, wrapped, instance):
               if instance is None:
                   if inspect.isclass(wrapped):
                       fmt = "The class {name} is deprecated."
                   else:
                       fmt = "The function {name} is deprecated."
               else:
                   if inspect.isclass(instance):
                       fmt = "The class method {name} is deprecated."
                   else:
                       fmt = "The method {name} is deprecated."
               if self.reason:
                   fmt += " ({reason})"
               if self.version:
                   fmt += " -- Deprecated since version {version}."
               return fmt.format(name=wrapped.__name__,
                                 reason=self.reason or "",
                                 version=self.version or "")

    Then, you can use your ``MyClassicAdapter`` class like this in your source code:

    .. code-block:: python

       @deprecated(reason="use another function", adapter_cls=MyClassicAdapter)
       def some_old_function(x, y):
           return x + y
    """

    reason: str
    version: str
    action: Optional[str]
    category: Type[DeprecationWarning]

    def __init__(
        self, reason: str = "", version: str = "", action: Optional[str] = None, category: Type[DeprecationWarning] = ...,
    ) -> None:
        """
        Construct a wrapper adapter.

        :type  reason: str
        :param reason:
            Reason message which documents the deprecation in your library (can be omitted).

        :type  version: str
        :param version:
            Version of your project which deprecates this feature.
            If you follow the `Semantic Versioning <https://semver.org/>`_,
            the version number has the format "MAJOR.MINOR.PATCH".

        :type  action: str
        :param action:
            A warning filter used to activate or not the deprecation warning.
            Can be one of "error", "ignore", "always", "default", "module", or "once".
            If ``None`` or empty, the the global filtering mechanism is used.
            See: `The Warnings Filter`_ in the Python documentation.

        :type  category: type
        :param category:
            The warning category to use for the deprecation warning.
            By default, the category class is :class:`~DeprecationWarning`,
            you can inherit this class to define your own deprecation warning category.
        """

    def get_deprecated_msg(self, wrapped: Callable[..., Any], instance: object) -> str:
        """
        Get the deprecation warning message for the user.

        :param wrapped: Wrapped class or function.
        :param instance: The object to which the wrapped function was bound when it was called.
        :return: The warning message.
        """
        ...

    def __call__(self, wrapped: _T) -> Callable[[_T], _T]:
        """
        Decorate your class or function.

        :param wrapped: Wrapped class or function.
        :return: the decorated class or function.
        .. versionchanged:: 1.2.4
           Don't pass arguments to :meth:`object.__new__` (other than *cls*).

        .. versionchanged:: 1.2.8
           The warning filter is not set if the *action* parameter is ``None`` or empty.
        """
        ...


def deprecated(
    *, reason: str = "", version: str = "", action: Optional[str] = ..., category: Optional[Type[DeprecationWarning]] = ...,
) -> Callable[[_T], _T]:
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.

    **Classic usage:**

    To use this, decorate your deprecated function with **@deprecated** decorator:

    .. code-block:: python

       from deprecated import deprecated


       @deprecated
       def some_old_function(x, y):
           return x + y

    You can also decorate a class or a method:

    .. code-block:: python

       from deprecated import deprecated


       class SomeClass(object):
           @deprecated
           def some_old_method(self, x, y):
               return x + y


       @deprecated
       class SomeOldClass(object):
           pass

    You can give a *reason* message to help the developer to choose another function/class,
    and a *version* number to specify the starting version number of the deprecation.

    .. code-block:: python

       from deprecated import deprecated


       @deprecated(reason="use another function", version='1.2.0')
       def some_old_function(x, y):
           return x + y

    The *category* keyword argument allow you to specify the deprecation warning class of your choice.
    By default, :exc:`DeprecationWarning` is ued but you can choose :exc:`FutureWarning`,
    :exc:`PendingDeprecationWarning` or a custom subclass.

    .. code-block:: python

       from deprecated import deprecated


       @deprecated(category=PendingDeprecationWarning)
       def some_old_function(x, y):
           return x + y

    The *action* keyword argument allow you to locally change the warning filtering.
    *action* can be one of "error", "ignore", "always", "default", "module", or "once".
    If ``None``, empty or missing, the the global filtering mechanism is used.
    See: `The Warnings Filter`_ in the Python documentation.

    .. code-block:: python

       from deprecated import deprecated


       @deprecated(action="error")
       def some_old_function(x, y):
           return x + y

    """
    ...
