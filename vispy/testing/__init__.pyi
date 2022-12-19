# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ._testing import (
    SkipTest as SkipTest,
    requires_application as requires_application,
    requires_ipython as requires_ipython,  # noqa
    requires_img_lib as requires_img_lib,  # noqa
    requires_pyopengl as requires_pyopengl,  # noqa
    requires_scipy as requires_scipy,  # noqa
    save_testing_image as save_testing_image,
    TestingCanvas as TestingCanvas,
    has_pyopengl as has_pyopengl,  # noqa
    run_tests_if_main as run_tests_if_main,
    requires_ssl as requires_ssl,  # noqa
    assert_is as assert_is,
    assert_in as assert_in,
    assert_not_in as assert_not_in,
    assert_equal as assert_equal,
    assert_not_equal as assert_not_equal,
    assert_raises as assert_raises,
    assert_true as assert_true,  # noqa
    raises as raises,
    requires_numpydoc as requires_numpydoc,
    IS_TRAVIS_CI as IS_TRAVIS_CI,
    IS_CI as IS_CI,
)  # noqa
from ._runners import test as test  # noqa
