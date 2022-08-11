from typing import Iterable

from tensorflow.compat.v1 import MetaGraphDef, Session

def load(
    sess: Session, tags: Iterable[str], export_dir: str, import_scope: str | None = None, **saver_kwargs
) -> MetaGraphDef: ...
