from typing import Any, Callable, Generic, Iterable, Literal, Mapping, Protocol, Sequence, TypeVar

from os import PathLike

import tensorflow as tf
from tensorflow.compat.v1 import Session
from tensorflow.estimator import export as export
from tensorflow.estimator.export import ExportOutput

from bento.utilities.typehints.recursive_types import ContainerGeneric
from bento.utils.tensor_types import TensorCompatible

_FeaturesT = TypeVar("_FeaturesT", bound=tf.Tensor | Mapping[str, tf.Tensor], contravariant=True)
_LabelsT = TypeVar("_LabelsT", bound=tf.Tensor | Mapping[str, tf.Tensor], contravariant=True)

# The duplication is an artifact of there is no nice way to indicate
# an argument may optionally be present. There's 8 possible cases
# and we currently have 3 (full version + 2 used in codebase).
# More cases can be added as needed.
class ModelFn1(Generic[_FeaturesT, _LabelsT], Protocol):
    def __call__(
        self,
        features: _FeaturesT,
        labels: _LabelsT | None,
        *,
        mode: ModeKeysT,
        config: RunConfig,
        params: dict[str, object],
    ) -> EstimatorSpec: ...

class ModelFn2(Generic[_FeaturesT, _LabelsT], Protocol):
    def __call__(
        self,
        features: _FeaturesT,
        labels: _LabelsT | None,
        *,
        mode: ModeKeysT,
        params: dict[str, object],
    ) -> EstimatorSpec: ...

class ModelFn3(Generic[_FeaturesT, _LabelsT], Protocol):
    def __call__(
        self,
        features: _FeaturesT,
        labels: _LabelsT | None,
        *,
        mode: ModeKeysT,
    ) -> EstimatorSpec: ...

class ModelFn4(Generic[_FeaturesT, _LabelsT], Protocol):
    def __call__(
        self,
        features: _FeaturesT,
        labels: _LabelsT | None,
    ) -> EstimatorSpec: ...

ModelFn = (
    ModelFn1[_FeaturesT, _LabelsT]
    | ModelFn2[_FeaturesT, _LabelsT]
    | ModelFn3[_FeaturesT, _LabelsT]
    | ModelFn4[_FeaturesT, _LabelsT]
)

class CheckpointSaverListener: ...
class SessionRunHook: ...

class Estimator(Generic[_FeaturesT, _LabelsT]):
    def __init__(
        self,
        model_fn: ModelFn[_FeaturesT, _LabelsT],
        model_dir: PathLike[str] | str | None = None,
        config: RunConfig | None = None,
        params: Mapping[str, object] | None = None,
        warm_start_from: str | WarmStartSettings | None = None,
    ) -> None: ...
    def _add_meta_graph_for_mode(
        self,
        builder: tf.compat.v1.saved_model.Builder,
        input_receiver_fn_map: dict[ModeKeysT, Callable[[], tf.estimator.export.ServingInputReceiver]],
        checkpoint_path: str,
        save_variables: bool = True,
        mode: ModeKeysT = ModeKeys.PREDICT,
        export_tags: Iterable[str] | None = None,
        check_variables: bool = True,
        strip_default_attrs: bool = True,
    ): ...
    def train(
        self,
        input_fn: Callable[[], tf.data.Dataset[tuple[_FeaturesT, _LabelsT] | tuple[_FeaturesT, _LabelsT]]],
        hooks: Sequence[SessionRunHook] | None = None,
        steps: int | None = None,
        max_steps: int | None = None,
        saving_listeners: Sequence[CheckpointSaverListener] | None = None,
    ): ...
    def __getattr__(self, name: str) -> Any: ...

class RunConfig:
    def __getattr__(self, name: str) -> Any: ...

class WarmStartSettings:
    def __getattr__(self, name: str) -> Any: ...

class EstimatorSpec:
    def __init__(
        self,
        mode: ModeKeysT,
        predictions: tf.Tensor | Mapping[str, tf.Tensor] | None = None,
        loss: tf.Tensor | None = None,
        train_op: tf.Operation | None = None,
        export_outputs: Mapping[str, ExportOutput] | None = None,
        training_chief_hooks: Iterable[SessionRunHook] | None = None,
        training_hooks: Iterable[SessionRunHook] | None = None,
        evaluation_hooks: Iterable[SessionRunHook] | None = None,
        prediction_hooks: Iterable[SessionRunHook] | None = None,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class SessionRunContext:
    def __init__(self, original_args: SessionRunArgs, session: Session) -> None: ...
    @property
    def original_args(self) -> SessionRunArgs: ...
    @property
    def session(self) -> Session: ...
    @property
    def stop_requested(self) -> bool: ...
    def request_stop(self) -> None: ...

class SessionRunValues: ...

FetchT = tf.Tensor | tf.Operation | tf.SparseTensor | str

class SessionRunArgs:
    def __init__(
        self,
        fetches: ContainerGeneric[FetchT],
        feed_dict: Mapping[tf.Tensor, TensorCompatible] | None = None,
    ) -> None: ...
    @property
    def fetches(self) -> ContainerGeneric[FetchT]: ...
    @property
    def feed_dict(self) -> Mapping[tf.Tensor, TensorCompatible]: ...

class ModeKeys:
    TRAIN = "train"
    EVAL = "eval"
    PREDICT = "infer"

ModeKeysT = Literal["train", "eval", "infer"]

def __getattr__(name: str) -> Any: ...
