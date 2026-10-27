These stubs were created with https://github.com/gramster/docs2stubs. 

The stubs target the latest scikit-image supported by each Python version:
0.25 on Python 3.10 and 0.26 on Python 3.11 and newer. Version-dependent APIs
use `sys.version_info` branches because scikit-image 0.26 requires Python 3.11.
For Python 3.11 and newer, use 0.26 to obtain the newly annotated model and
transform estimation APIs.

The deprecated no-argument model constructors and `estimate` methods remain
available. New `from_estimate` methods return either the requested model or
`skimage._shared.utils.FailedEstimation`, not a boolean or `None`.

`RansacModelProtocol` accepts a variadic data signature: annotate one-array
models as `RansacModelProtocol[NDArray]` and two-array transforms as
`RansacModelProtocol[NDArray, NDArray]`. These parameters are typing-only;
use postponed annotations (`from __future__ import annotations`) because the
runtime protocol does not support subscripting.

The allowlist documents five specific 0.26 signature-introspection bugs rather
than changing the annotations to match incorrect wrapper metadata. Optional
test-module entries are exact names and do not suppress public API failures.
