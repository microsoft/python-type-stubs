from typing import Generic, Iterator, NamedTuple, TypeVar

from enum import Enum

from tensorflow import TypeSpec

from bento.utils.tensor_types import ContainerGeneric

class InputContext:
    def __init__(
        self, num_input_pipelines: int = 1, input_pipeline_id: int = 0, num_replicas_in_sync: int = 1
    ) -> None: ...
    @property
    def num_input_pipelines(self) -> int: ...
    @property
    def input_pipeline_id(self) -> int: ...
    @property
    def num_replicas_in_sync(self) -> int: ...
    def get_per_replica_batch_size(self, global_batch_size: int) -> int: ...

class InputReplicationMode(Enum):
    PER_WORKER = "PER_WORKER"
    PER_REPLICA = "PER_REPLICA"

class InputOptions(NamedTuple):
    experimental_fetch_to_device: bool | None = None
    experimental_replication_mode: InputReplicationMode = InputReplicationMode.PER_WORKER
    experimental_place_dataset_on_device: bool = False
    experimental_per_replica_buffer_size: int = 1

_T1 = TypeVar("_T1", covariant=True)

class DistributedIterator(Generic[_T1]):
    element_spec: ContainerGeneric[TypeSpec]
    def __iter__(self) -> Iterator[_T1]: ...

class DistributedDataset(Generic[_T1]):
    element_spec: ContainerGeneric[TypeSpec]
    def __iter__(self) -> DistributedIterator[_T1]: ...
