import os
from collections import OrderedDict
from typing import Any

from transformers.configuration_utils import PretrainedConfig
from transformers.tokenization_utils import PreTrainedTokenizer
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast

from .auto_factory import _LazyAutoMapping

TOKENIZER_MAPPING_NAMES: OrderedDict[str, tuple[str | None, str | None]]
TOKENIZER_MAPPING: _LazyAutoMapping
CONFIG_TO_TYPE: dict[type[PretrainedConfig], str]

def tokenizer_class_from_name(class_name: str) -> PreTrainedTokenizer | PreTrainedTokenizerFast: ...
def get_tokenizer_config(
    pretrained_model_name_or_path: str | os.PathLike[str],
    cache_dir: str | os.PathLike[str] | None = None,
    force_download: bool = False,
    resume_download: bool = False,
    proxies: dict[str, str] | None = None,
    use_auth_token: bool | str | None = None,
    revision: str | None = None,
    local_files_only: bool = False,
    subfolder: str = "",
    **kwargs,
) -> dict[str, Any]: ...

class AutoTokenizer:
    def __init__(self) -> None: ...
    @classmethod
    def from_pretrained(
        cls, pretrained_model_name_or_path: str | os.PathLike[str], *inputs, **kwargs
    ) -> PreTrainedTokenizer | PreTrainedTokenizerFast: ...
    def register(config_class, slow_tokenizer_class=None, fast_tokenizer_class=None) -> None: ...
