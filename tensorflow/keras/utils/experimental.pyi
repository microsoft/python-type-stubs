from typing import Callable, Generic, TypeVar

from tensorflow.data import Dataset
from tensorflow.distribute import InputContext, InputOptions

_T1 = TypeVar("_T1")

class DatasetCreator(Generic[_T1]):
    def __init__(
        self, dataset_fn: Callable[[InputContext], Dataset[_T1]], input_options: InputOptions | None = None
    ): ...
    def __call__(self, input_context: InputContext) -> Dataset[_T1]: ...
