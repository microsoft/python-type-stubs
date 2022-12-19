from ._locally_linear import (
    locally_linear_embedding as locally_linear_embedding,
    LocallyLinearEmbedding as LocallyLinearEmbedding,
)
from ._isomap import Isomap as Isomap
from ._mds import MDS as MDS, smacof as smacof
from ._spectral_embedding import (
    SpectralEmbedding as SpectralEmbedding,
    spectral_embedding as spectral_embedding,
)
from ._t_sne import TSNE as TSNE, trustworthiness as trustworthiness

__all__ = [
    "locally_linear_embedding",
    "LocallyLinearEmbedding",
    "Isomap",
    "MDS",
    "smacof",
    "SpectralEmbedding",
    "spectral_embedding",
    "TSNE",
    "trustworthiness",
]
