import os
from collections import OrderedDict
from typing import Any
from typing_extensions import TypeAlias

from transformers.models.auto.auto_factory import _LazyAutoMapping
from transformers.tokenization_utils import PreTrainedTokenizer
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast

TOKENIZER_MAPPING_NAMES: OrderedDict[str, tuple[str | None, str | None]]
TOKENIZER_MAPPING: _LazyAutoMapping
CONFIG_TO_TYPE: dict[str, str]

def tokenizer_class_from_name(class_name: str) -> type[Any] | None: ...
def get_tokenizer_config(
    pretrained_model_name_or_path: str | os.PathLike[str],
    cache_dir: str | os.PathLike[str] | None = None,
    force_download: bool = False,
    resume_download: bool | None = None,
    proxies: dict[str, str] | None = None,
    token: bool | str | None = None,
    revision: str | None = None,
    local_files_only: bool = False,
    subfolder: str = "",
    **kwargs,
) -> dict[str, Any]: ...

class AutoTokenizer:
    def __init__(self) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: str | os.PathLike[str], *inputs, **kwargs): ...
    def register(config_class, slow_tokenizer_class=None, fast_tokenizer_class=None, exist_ok=False) -> None: ...
