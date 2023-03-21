from scipy import sparse as sparse
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from .._typing import MatrixLike, Int

# Authors: Aric Hagberg <hagberg@lanl.gov>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Jake Vanderplas <vanderplas@astro.washington.edu>
# License: BSD 3 clause

import numpy as np


###############################################################################
# Path and connected component analysis.
# Code adapted from networkx
def single_source_shortest_path_length(
    graph: MatrixLike, source: Int, *, cutoff: None | Int = None
) -> dict:
    ...
