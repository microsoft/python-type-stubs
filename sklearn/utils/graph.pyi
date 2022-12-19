from numpy import ndarray
from typing import Literal
from numpy.typing import ArrayLike

# Authors: Aric Hagberg <hagberg@lanl.gov>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Jake Vanderplas <vanderplas@astro.washington.edu>
# License: BSD 3 clause

import numpy as np
from scipy import sparse

from .deprecation import deprecated
from ..metrics.pairwise import pairwise_distances

###############################################################################
# Path and connected component analysis.
# Code adapted from networkx
def single_source_shortest_path_length(graph: NDArray, source: int, *, cutoff: int | None = None): ...
@deprecated(
    "`graph_shortest_path` is deprecated in 1.0 (renaming of 0.25) and will "
    "be removed in 1.2. Use `scipy.sparse.csgraph.shortest_path` instead."
)
def graph_shortest_path(
    dist_matrix: ArrayLike | NDArray,
    directed: bool = True,
    method: Literal["auto", "FW", "D"] = "auto",
) -> NDArray: ...
def _fix_connected_components(
    X,
    graph,
    n_connected_components,
    component_labels,
    mode="distance",
    metric="euclidean",
    **kwargs,
): ...
