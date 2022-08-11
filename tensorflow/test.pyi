from typing import Any, Mapping, Sequence, overload

import numpy as np

from tensorflow import ContainerArrays, ContainerTensorsLike, Operation, Tensor

class TestCase:
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    @overload
    def evaluate(self, tensors: Tensor) -> np.ndarray[Any, Any]: ...
    @overload
    def evaluate(self, tensors: Operation) -> None: ...
    @overload
    def evaluate(self, tensors: Mapping[str, Tensor]) -> Mapping[str, np.ndarray[Any, Any]]: ...
    @overload
    def evaluate(self, tensors: Sequence[Tensor]) -> Sequence[np.ndarray[Any, Any]]: ...
    @overload
    def evaluate(self, tensors: ContainerTensorsLike) -> ContainerArrays: ...
    def assertEqual(self, first: object, second: object, msg: str | None = None) -> None: ...
    def get_temp_dir(self) -> str: ...
