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
    orig = """
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
"""
    with open(os.path.join(stubpath, stubname), 'w') as f:
        f.write(orig)
    yield stubpath, docpath, stubname, orig
    stubdir.cleanup()
    docdir.cleanup()


def test_merge_stub(simplestub):
    (stubroot, docroot, fname, orig) = simplestub
 
    stubsplit.split(stubroot, docroot, fname)

    stubsplit.combine(stubroot, docroot, fname)

    with open(os.path.join(stubroot, fname)) as f:
        assert_that(f.read(), equal_to(orig))


