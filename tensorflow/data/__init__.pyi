from typing import Any, Callable, Generic, Iterator, Literal, Sequence, TypeVar
from typing_extensions import Self

import numpy as np

from tensorflow import Tensor, TensorCompatibleT, TypeSpec
from tensorflow.data import experimental as experimental

from bento.utils.tensor_types import ContainerGeneric, ScalarTensorCompatible, TensorCompatible

_T1 = TypeVar("_T1", covariant=True)
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")

class Dataset(Generic[_T1]):
    element_spec: ContainerGeneric[TypeSpec]
    def apply(self: Dataset[_T1], transformation_func: Callable[[Dataset[_T1]], Dataset[_T2]]) -> Dataset[_T2]: ...
    def as_numpy_iterator(self) -> Iterator[np.ndarray[Any, Any]]: ...
    def batch(
        self: Self,
        batch_size: ScalarTensorCompatible,
        drop_remainder: bool = False,
        num_parallel_calls: int | None = None,
        deterministic: bool | None = None,
        name: str | None = None,
    ) -> Self: ...
    def cache(self: Self, filename: str = "", name: str | None = None) -> Self: ...
    @classmethod
    def from_tensor_slices(
        cls, tensors: Sequence[TensorCompatibleT] | TensorCompatibleT, name: str | None = None
    ) -> Dataset[TensorCompatibleT]: ...
    def __iter__(self) -> Iterator[_T1]: ...
    def map(
        self: Dataset[_T1],
        map_func: Callable[[_T1], _T2],
        num_parallel_calls: int | None = None,
        deterministic: None | bool = None,
        name: str | None = None,
    ) -> Dataset[_T2]: ...
    def prefetch(self: Self, buffer_size: int, name: str | None = None) -> Self: ...
    def reduce(self, initial_state: _T2, reduce_func: Callable[[_T2, _T1], _T2], name: str | None = None) -> _T2: ...
    def repeat(self: Self, count: int | None = None, name: str | None = None) -> Self: ...
    def shard(self: Self, num_shards: int, index: int, name: str | None = None) -> Self: ...
    def shuffle(
        self: Self,
        buffer_size: int,
        seed: int | None = None,
        reshuffle_each_iteration: bool = True,
        name: str | None = None,
    ) -> Self: ...
    def take(self: Self, count: int, name: str | None = None) -> Self: ...
    @staticmethod
    def zip(datasets: tuple[Dataset[_T2], Dataset[_T3]], name: str | None = None) -> Dataset[tuple[_T2, _T3]]: ...

class TFRecordDataset(Dataset[Tensor]):
    def __init__(
        self,
        filenames: TensorCompatible | Dataset[str],
        compression_type: Literal["", "ZLIB", "GZIP"] | None = None,
        buffer_size: int | None = None,
        num_parallel_reads: int | None = None,
        name: str | None = None,
    ) -> None: ...
