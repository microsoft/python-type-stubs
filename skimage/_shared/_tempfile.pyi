from tempfile import NamedTemporaryFile
from contextlib import contextmanager
import os

@contextmanager
def temporary_file(suffix: str = ""): ...
