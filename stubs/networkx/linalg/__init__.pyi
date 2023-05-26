from .attrmatrix import attr_matrix, attr_sparse_matrix
from . import attrmatrix as attrmatrix
from .spectrum import (
    laplacian_spectrum,
    adjacency_spectrum,
    modularity_spectrum,
    normalized_laplacian_spectrum,
    bethe_hessian_spectrum,
)
from . import spectrum as spectrum
from .graphmatrix import incidence_matrix, adj_matrix, adjacency_matrix
from . import graphmatrix as graphmatrix
from .laplacianmatrix import (
    laplacian_matrix,
    normalized_laplacian_matrix,
    total_spanning_tree_weight,
    directed_laplacian_matrix,
    directed_combinatorial_laplacian_matrix,
)
from . import laplacianmatrix as laplacianmatrix
from .algebraicconnectivity import (
    algebraic_connectivity,
    fiedler_vector,
    spectral_ordering,
)
from .modularitymatrix import modularity_matrix, directed_modularity_matrix
from . import modularitymatrix as modularitymatrix
from .bethehessianmatrix import bethe_hessian_matrix as bethe_hessian_matrix
from . import bethehessianmatrix as bethehessianmatrix
