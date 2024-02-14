import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile

@contextmanager
def temporary_file(suffix: str = ""): ...
