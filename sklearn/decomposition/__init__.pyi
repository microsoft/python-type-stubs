from ._dict_learning import (
    dict_learning as dict_learning,
    dict_learning_online as dict_learning_online,
    sparse_encode as sparse_encode,
    DictionaryLearning as DictionaryLearning,
    MiniBatchDictionaryLearning as MiniBatchDictionaryLearning,
    SparseCoder as SparseCoder,
)
from ._fastica import FastICA as FastICA, fastica as fastica
from ..utils.extmath import randomized_svd as randomized_svd
from ._nmf import (
    NMF as NMF,
    MiniBatchNMF as MiniBatchNMF,
    non_negative_factorization as non_negative_factorization,
)
from ._kernel_pca import KernelPCA as KernelPCA
from ._sparse_pca import (
    SparsePCA as SparsePCA,
    MiniBatchSparsePCA as MiniBatchSparsePCA,
)
from ._incremental_pca import IncrementalPCA as IncrementalPCA
from ._lda import LatentDirichletAllocation as LatentDirichletAllocation
from ._factor_analysis import FactorAnalysis as FactorAnalysis
from ._pca import PCA as PCA
from ._truncated_svd import TruncatedSVD as TruncatedSVD


__all__ = [
    "DictionaryLearning",
    "FastICA",
    "IncrementalPCA",
    "KernelPCA",
    "MiniBatchDictionaryLearning",
    "MiniBatchNMF",
    "MiniBatchSparsePCA",
    "NMF",
    "PCA",
    "SparseCoder",
    "SparsePCA",
    "dict_learning",
    "dict_learning_online",
    "fastica",
    "non_negative_factorization",
    "randomized_svd",
    "sparse_encode",
    "FactorAnalysis",
    "TruncatedSVD",
    "LatentDirichletAllocation",
]
