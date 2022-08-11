from typing import Any, overload

import tensorflow as tf
from tensorflow import RaggedTensor, ScalarTensorCompatible, Tensor, TensorCompatible
from tensorflow.sparse import SparseTensor

from bento.utils.tensor_types import DTypeLike

class TableInitializerBase:
    def __init__(
        self,
        key_dtype: DTypeLike | None = None,
        value_dtype: DTypeLike | None = None,
    ) -> None: ...
    @property
    def key_dtype(self) -> tf.DType: ...
    @property
    def value_dtype(self) -> tf.DType: ...

class KeyValueTensorInitializer(TableInitializerBase):
    # Only rank 1 is supported.
    def __init__(
        self,
        keys: TensorCompatible,
        values: TensorCompatible,
        key_dtype: DTypeLike | None = None,
        value_dtype: DTypeLike | None = None,
        name: str | None = None,
    ) -> None: ...

class StaticHashTable:
    def __init__(
        self, initializer: TableInitializerBase, default_value: ScalarTensorCompatible, name: str | None = None
    ) -> None: ...
    def export(self, name: str | None = None) -> tuple[Tensor, Tensor]: ...
    def size(self, name: str | None = None) -> int: ...
    @overload
    def lookup(self, keys: TensorCompatible, name: str | None = None) -> Tensor: ...
    @overload
    def lookup(self, keys: SparseTensor, name: str | None = None) -> SparseTensor: ...
    @property
    def name(self) -> str: ...
    def __getitem__(self, keys: TensorCompatible) -> Tensor: ...

class StaticVocabularyTable:
    def __init__(
        self,
        initializer: TableInitializerBase | None,
        num_oov_buckets: int,
        lookup_key_dtype: DTypeLike | None = None,
        name: str | None = None,
        experimental_is_anonymous: bool = False,
    ) -> None: ...
    @overload
    def lookup(self, keys: TensorCompatible, name: str | None = None) -> Tensor: ...
    @overload
    def lookup(self, keys: SparseTensor, name: str | None = None) -> SparseTensor: ...
    @overload
    def lookup(self, keys: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
    @overload
    def __getitem__(self, keys: TensorCompatible) -> Tensor: ...
    @overload
    def __getitem__(self, keys: SparseTensor) -> SparseTensor: ...
    @overload
    def __getitem__(self, keys: RaggedTensor) -> RaggedTensor: ...
    def size(self, name: str | None = None) -> int: ...

def __getattr__(name: str) -> Any: ...
