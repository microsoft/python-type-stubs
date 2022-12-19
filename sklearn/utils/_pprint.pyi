# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
# 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018 Python Software Foundation;
# All Rights Reserved

# Authors: Fred L. Drake, Jr. <fdrake@acm.org> (built-in CPython pprint module)
#          Nicolas Hug (scikit-learn specific changes)

# License: PSF License version 2 (see below)

# PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# --------------------------------------------

# 1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"),
# and the Individual or Organization ("Licensee") accessing and otherwise
# using this software ("Python") in source or binary form and its associated
# documentation.

# 2. Subject to the terms and conditions of this License Agreement, PSF hereby
# grants Licensee a nonexclusive, royalty-free, world-wide license to
# reproduce, analyze, test, perform and/or display publicly, prepare
# derivative works, distribute, and otherwise use Python alone or in any
# derivative version, provided, however, that PSF's License Agreement and
# PSF's notice of copyright, i.e., "Copyright (c) 2001, 2002, 2003, 2004,
# 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
# 2017, 2018 Python Software Foundation; All Rights Reserved" are retained in
# Python alone or in any derivative version prepared by Licensee.

# 3. In the event Licensee prepares a derivative work that is based on or
# incorporates Python or any part thereof, and wants to make the derivative
# work available to others as provided herein, then Licensee hereby agrees to
# include in any such work a brief summary of the changes made to Python.

# 4. PSF is making Python available to Licensee on an "AS IS" basis. PSF MAKES
# NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT
# NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF
# PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

# 5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON FOR ANY
# INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
# MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON, OR ANY DERIVATIVE
# THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

# 6. This License Agreement will automatically terminate upon a material
# breach of its terms and conditions.

# 7. Nothing in this License Agreement shall be deemed to create any
# relationship of agency, partnership, or joint venture between PSF and
# Licensee. This License Agreement does not grant permission to use PSF
# trademarks or trade name in a trademark sense to endorse or promote products
# or services of Licensee, or any third party.

# 8. By copying, installing or otherwise using Python, Licensee agrees to be
# bound by the terms and conditions of this License Agreement.

# Brief summary of changes to original code:
# - "compact" parameter is supported for dicts, not just lists or tuples
# - estimators have a custom handler, they're not just treated as objects
# - long sequences (lists, tuples, dict items) with more than N elements are
#   shortened using ellipsis (', ...') at the end.

import inspect
import pprint
from collections import OrderedDict

from ..base import BaseEstimator
from .._config import get_config
from . import is_scalar_nan
from io import StringIO
from sklearn.base import BaseEstimator
from sklearn.decomposition._pca import PCA
from sklearn.feature_selection._univariate_selection import SelectKBest
from sklearn.linear_model._stochastic_gradient import SGDClassifier
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.svm._classes import SVC
from typing import Any, Dict, List, Tuple, Union

class KeyValTuple(tuple):
    def __repr__(self) -> str: ...

class KeyValTupleParam(KeyValTuple):
    pass

def _changed_params(estimator: BaseEstimator) -> Dict[str, Any]: ...

class _EstimatorPrettyPrinter(pprint.PrettyPrinter):
    def __init__(
        self,
        indent: int = 1,
        width: int = 80,
        depth: None = None,
        stream: None = None,
        *,
        compact=False,
        indent_at_name=True,
        n_max_elements_to_show=None,
    ) -> None: ...
    def format(self, object: Any, context: Dict[int, int], maxlevels: None, level: int) -> Tuple[str, bool, bool]: ...
    def _pprint_estimator(
        self,
        object: Union[Pipeline, FeatureUnion, SGDClassifier],
        stream: StringIO,
        indent: int,
        allowance: int,
        context: Dict[int, int],
        level: int,
    ) -> None: ...
    def _format_dict_items(self, items, stream, indent, allowance, context, level): ...
    def _format_params(self, items, stream, indent, allowance, context, level): ...
    def _format_params_or_dict_items(self, object, stream, indent, allowance, context, level, is_dict): ...
    def _format_items(
        self,
        items: Union[
            List[Union[Tuple[str, FeatureUnion], Tuple[str, SVC]]],
            Tuple[str, SelectKBest],
            Tuple[str, FeatureUnion],
            List[Union[Tuple[str, PCA], Tuple[str, SelectKBest]]],
        ],
        stream: StringIO,
        indent: int,
        allowance: int,
        context: Dict[int, int],
        level: int,
    ) -> None: ...
    def _pprint_key_val_tuple(
        self,
        object: KeyValTupleParam,
        stream: StringIO,
        indent: int,
        allowance: int,
        context: Dict[int, int],
        level: int,
    ) -> None: ...

    # Note: need to copy _dispatch to prevent instances of the builtin
    # PrettyPrinter class to call methods of _EstimatorPrettyPrinter (see issue
    # 12906)
    # mypy error: "Type[PrettyPrinter]" has no attribute "_dispatch"
    _dispatch = ...  # type: ignore
    _dispatch[BaseEstimator.__repr__] = ...
    _dispatch[KeyValTuple.__repr__] = ...

def _safe_repr(
    object: Any,
    context: Dict[int, int],
    maxlevels: None,
    level: int,
    changed_only: bool = False,
) -> Tuple[str, bool, bool]: ...
