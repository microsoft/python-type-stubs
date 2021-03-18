# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.signal._spectral, version: unspecified
import typing
import builtins as _mod_builtins

__all__: list
__doc__: str
__file__: str
__name__: str
__package__: str
__test__: dict
def _lombscargle(x, y, freqs) -> typing.Any:
    '\n    _lombscargle(x, y, freqs)\n\n    Computes the Lomb-Scargle periodogram.\n\n    Parameters\n    ----------\n    x : array_like\n        Sample times.\n    y : array_like\n        Measurement values (must be registered so the mean is zero).\n    freqs : array_like\n        Angular frequencies for output periodogram.\n\n    Returns\n    -------\n    pgram : array_like\n        Lomb-Scargle periodogram.\n\n    Raises\n    ------\n    ValueError\n        If the input arrays `x` and `y` do not have the same shape.\n\n    See also\n    --------\n    lombscargle\n\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

