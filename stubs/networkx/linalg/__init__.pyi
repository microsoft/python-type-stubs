from .attrmatrix import attr_matrix as attr_matrix, attr_sparse_matrix as attr_sparse_matrix
from . import attrmatrix as attrmatrix
from .spectrum import (
    laplacian_spectrum as laplacian_spectrum,
    adjacency_spectrum as adjacency_spectrum,
    modularity_spectrum as modularity_spectrum,
    normalized_laplacian_spectrum as normalized_laplacian_spectrum,
    bethe_hessian_spectrum as bethe_hessian_spectrum,
)
from . import spectrum as spectrum
from .graphmatrix import incidence_matrix as incidence_matrix, adj_matrix as adj_matrix, adjacency_matrix as adjacency_matrix
from . import graphmatrix as graphmatrix
from .laplacianmatrix import (
    laplacian_matrix as laplacian_matrix,
    normalized_laplacian_matrix as normalized_laplacian_matrix,
    total_spanning_tree_weight as total_spanning_tree_weight,
    directed_laplacian_matrix as directed_laplacian_matrix,
    directed_combinatorial_laplacian_matrix as directed_combinatorial_laplacian_matrix,
)
from . import laplacianmatrix as laplacianmatrix
from .algebraicconnectivity import (
    algebraic_connectivity as algebraic_connectivity,
    fiedler_vector as fiedler_vector,
    spectral_ordering as spectral_ordering,
)
from .modularitymatrix import modularity_matrix as modularity_matrix, directed_modularity_matrix as directed_modularity_matrix
from . import modularitymatrix as modularitymatrix
from .bethehessianmatrix import bethe_hessian_matrix as bethe_hessian_matrix
from . import bethehessianmatrix as bethehessianmatrix
