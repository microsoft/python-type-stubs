from tensorflow import RaggedTensor, ScalarTensorCompatible, SparseTensorCompatible, Tensor, TensorCompatible
from tensorflow.math import sigmoid as sigmoid
from tensorflow.math import tanh as tanh

def relu(features: TensorCompatible, name: str | None = None) -> Tensor: ...
def leaky_relu(features: TensorCompatible, alpha: float = 0.2, name: str | None = None) -> Tensor: ...
def log_poisson_loss(
    targets: TensorCompatible, log_input: TensorCompatible, compute_full_loss: bool = False, name: str | None = None
) -> Tensor: ...
def sigmoid_cross_entropy_with_logits(
    labels: TensorCompatible, logits: TensorCompatible, name: str | None = None
) -> Tensor: ...
def softmax(
    logits: TensorCompatible, axis: ScalarTensorCompatible | None = None, name: str | None = None
) -> Tensor: ...
def selu(features: TensorCompatible, name: str | None = None) -> Tensor: ...
def embeddings_lookup(
    params: TensorCompatible, ids: TensorCompatible, max_norm: float | None = None, name: str | None = None
) -> Tensor: ...
def safe_embedding_lookup_sparse(
    embedding_weights: Tensor | list[Tensor],
    sparse_ids: SparseTensorCompatible,
    sparse_weights: SparseTensorCompatible | None = None,
    combiner: str = "mean",
    default_id: ScalarTensorCompatible | None = None,
    max_norm: float | None = None,
    name: str | None = None,
) -> Tensor: ...
def moments(
    x: TensorCompatible | RaggedTensor, axes: TensorCompatible, keepdims: bool = False, name: str | None = None
) -> tuple[Tensor, Tensor]: ...
