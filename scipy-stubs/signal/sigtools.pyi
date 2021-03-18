# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.signal.sigtools, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def _convolve2d() -> typing.Any:
    'out = _convolve2d(in1, in2, flip, mode, boundary, fillvalue)'
    ...

def _correlateND() -> typing.Any:
    "out = _correlateND(a,kernel,mode) \n\n   mode = 0 - 'valid', 1 - 'same', \n  2 - 'full' (default)"
    ...

def _linear_filter() -> typing.Any:
    '(y,Vf) = _linear_filter(b,a,X,Dim=-1,Vi=None)  implemented using Direct Form II transposed flow diagram. If Vi is not given, Vf is not returned.'
    ...

def _medfilt2d() -> typing.Any:
    'filt = _median2d(data, size)'
    ...

def _order_filterND() -> typing.Any:
    'out = _order_filterND(a,domain,order)'
    ...

def _remez() -> typing.Any:
    'h = _remez(numtaps, bands, des, weight, type, fs, maxiter, grid_density)\n  returns the optimal (in the Chebyshev/minimax sense) FIR filter impulse\n  response given a set of band edges, the desired response on those bands,\n  and the weight given to the error in those bands.  Bands is a monotonic\n  vector with band edges given in frequency domain where fs is the sampling\n  frequency.'
    ...

def __getattr__(name) -> typing.Any:
    ...

