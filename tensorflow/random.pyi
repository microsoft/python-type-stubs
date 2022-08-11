import tensorflow as tf

from bento.utils.tensor_types import DTypeLike, ScalarTensorCompatible, ShapeLike

def uniform(
    shape: ShapeLike,
    minval: ScalarTensorCompatible = 0.0,
    maxval: ScalarTensorCompatible | None = None,
    dtype: DTypeLike = tf.float32,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = tf.float32,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def truncated_normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = tf.float32,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def poisson(
    shape: ShapeLike,
    lam: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = tf.float32,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def shuffle(
    value: tf.Tensor,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
