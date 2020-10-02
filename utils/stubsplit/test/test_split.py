import os
import pytest
from stubsplit import stubsplit
import tempfile
from hamcrest import *


@pytest.fixture
def simplestub():
    stubdir = tempfile.TemporaryDirectory()
    docdir = tempfile.TemporaryDirectory()
    stubpath = stubdir.name
    docpath = docdir.name
    stubname = 'test.pyi'
    docname = stubname + '.ds'

    with open(os.path.join(stubpath, stubname), 'w') as f:
        f.write(
            """
def one(): ...
def two():
    '''
    This is the doc
    '''
    pass

class A:
    def one(): ...

class B:
    def two():
        '''
        This is the doc
        '''
        pass

def three(a, b,
    c):
    \"\"\"
    This is
    the doc
    \"\"\"
    pass

def four(a, b,
    c) -> Any: ...

class C:

    def four(a, b,
        c) -> Any: ...
    def three(a, b,
        c):
        \"\"\"
        This is
        the doc
        \"\"\"
        pass
"""
        )
    yield stubpath, docpath, stubname
    stubdir.cleanup()
    docdir.cleanup()


def test_split_stub(simplestub):
    (stubroot, docroot, fname) = simplestub
 
    stubsplit.split(stubroot, docroot, fname)

    with open(os.path.join(stubroot, fname)) as f:
        assert_that(f.read(), equal_to("""
def one(): ...
def two(): ...

class A:
    def one(): ...

class B:
    def two(): ...

def three(a, b,
    c): ...

def four(a, b,
    c) -> Any: ...

class C:

    def four(a, b,
        c) -> Any: ...
    def three(a, b,
        c): ...
"""))

def test_split_doc(simplestub):
    (stubroot, docroot, fname) = simplestub

    stubsplit.split(stubroot, docroot, fname)

    with open(os.path.join(docroot, fname + '.ds')) as f:
        assert_that(f.read(), equal_to("""def two():
    '''
    This is the doc
    '''
    pass

class B:
    def two():
        '''
        This is the doc
        '''
        pass
def three(a, b,
    c):
    \"\"\"
    This is
    the doc
    \"\"\"
    pass

class C:
    def three(a, b,
        c):
        \"\"\"
        This is
        the doc
        \"\"\"
        pass
"""))
