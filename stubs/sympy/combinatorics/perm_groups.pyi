from typing import Any, Generator, Literal, Self
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.pc_groups import PolycyclicGroup
from sympy.combinatorics.permutations import Permutation
from sympy.core import Basic
from sympy.core.function import UndefinedFunction

rmul = ...
_af_new = ...
class PermutationGroup(Basic):
    is_group = ...
    def __new__(cls, *args, dups=..., **kwargs) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __getitem__(self, i):
        ...
    
    def __contains__(self, i) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def __mul__(self, other) -> Coset | PermutationGroup:
        ...
    
    @property
    def base(self) -> list[Any]:
        ...
    
    def baseswap(self, base, strong_gens, pos, randomized=..., transversals=..., basic_orbits=..., strong_gens_distr=...) -> tuple[Any, Any]:
        ...
    
    @property
    def basic_orbits(self) -> list[list[Any]]:
        ...
    
    @property
    def basic_stabilizers(self) -> list[Any]:
        ...
    
    @property
    def basic_transversals(self) -> list[None] | None:
        ...
    
    def composition_series(self) -> list[Any]:
        ...
    
    def coset_transversal(self, H) -> list[Any | Basic | list[Any] | Permutation] | list[Permutation]:
        ...
    
    def coset_table(self, H) -> list[Any] | None:
        ...
    
    def center(self) -> Self | PermutationGroup | None:
        ...
    
    def centralizer(self, other) -> Self | PermutationGroup | None:
        ...
    
    def commutator(self, G, H) -> PermutationGroup | None:
        ...
    
    def coset_factor(self, g, factor_index=...) -> list[Any]:
        ...
    
    def generator_product(self, g, original=...) -> list[Any]:
        ...
    
    def coset_rank(self, g) -> int | None:
        ...
    
    def coset_unrank(self, rank, af=...) -> list[Any] | Permutation | None:
        ...
    
    @property
    def degree(self):
        ...
    
    @property
    def identity(self) -> Permutation:
        ...
    
    @property
    def elements(self) -> set[Any | Basic | list[Any] | Permutation]:
        ...
    
    def derived_series(self) -> list[Self]:
        ...
    
    def derived_subgroup(self) -> PermutationGroup | None:
        ...
    
    def generate(self, method=..., af=...) -> Generator[Any | Basic | list[Any] | Permutation, Any, None] | Generator[list[int] | Permutation | list[Any], Any, None]:
        ...
    
    def generate_dimino(self, af=...) -> Generator[list[int] | Permutation | list[Any], Any, None]:
        ...
    
    def generate_schreier_sims(self, af=...) -> Generator[Any | Basic | list[Any] | Permutation, Any, None]:
        ...
    
    @property
    def generators(self) -> list[Basic]:
        ...
    
    def contains(self, g, strict=...) -> bool:
        ...
    
    @property
    def is_perfect(self) -> bool:
        ...
    
    @property
    def is_abelian(self) -> bool:
        ...
    
    def abelian_invariants(self) -> list[Any]:
        ...
    
    def is_elementary(self, p) -> bool:
        ...
    
    def is_alt_sym(self, eps=..., _random_prec=...) -> bool:
        ...
    
    @property
    def is_nilpotent(self) -> bool:
        ...
    
    def is_normal(self, gr, strict=...) -> bool:
        ...
    
    def is_primitive(self, randomized=...) -> bool:
        ...
    
    def minimal_blocks(self, randomized=...) -> list[Any] | Literal[False]:
        ...
    
    @property
    def is_solvable(self) -> bool:
        ...
    
    def is_subgroup(self, G, strict=...) -> bool:
        ...
    
    @property
    def is_polycyclic(self) -> bool:
        ...
    
    def is_transitive(self, strict=...) -> bool:
        ...
    
    @property
    def is_trivial(self) -> bool:
        ...
    
    def lower_central_series(self) -> list[Self]:
        ...
    
    @property
    def max_div(self) -> Literal[1] | None:
        ...
    
    def minimal_block(self, points) -> list[Any] | Literal[False]:
        ...
    
    def conjugacy_class(self, x) -> set[Any]:
        ...
    
    def conjugacy_classes(self) -> list[set[Permutation]]:
        ...
    
    def normal_closure(self, other, k=...) -> PermutationGroup | None:
        ...
    
    def orbit(self, alpha, action=...) -> set[Any] | set[tuple[Any, ...]] | None:
        ...
    
    def orbit_rep(self, alpha, beta, schreier_vector=...) -> Permutation | Literal[False]:
        ...
    
    def orbit_transversal(self, alpha, pairs=...) -> list[tuple[Any, Permutation]] | list[tuple[Any, list[int]]] | tuple[list[tuple[Any, Permutation]] | list[tuple[Any, list[int]]], dict[Any, list[Any]]] | list[list[int]] | tuple[list[list[int]], dict[Any, list[Any]]] | list[Permutation] | tuple[list[Permutation], dict[Any, list[Any]]]:
        ...
    
    def orbits(self, rep=...) -> list[Any]:
        ...
    
    def order(self) -> int | type[UndefinedFunction]:
        ...
    
    def index(self, H) -> None:
        ...
    
    @property
    def is_symmetric(self) -> bool:
        ...
    
    @property
    def is_alternating(self) -> bool:
        ...
    
    @property
    def is_cyclic(self) -> bool:
        ...
    
    @property
    def is_dihedral(self) -> bool:
        ...
    
    def pointwise_stabilizer(self, points, incremental=...) -> PermutationGroup:
        ...
    
    def make_perm(self, n, seed=...) -> Permutation:
        ...
    
    def random(self, af=...) -> list[Any] | Permutation | None:
        ...
    
    def random_pr(self, gen_count=..., iterations=..., _random_prec=...) -> Permutation:
        ...
    
    def random_stab(self, alpha, schreier_vector=..., _random_prec=...) -> Permutation:
        ...
    
    def schreier_sims(self) -> None:
        ...
    
    def schreier_sims_incremental(self, base=..., gens=..., slp_dict=...) -> tuple[Any | list[Any], list[Basic] | Any, dict[Basic | Any, list[Basic | Any]]] | tuple[Any | list[Any], list[Basic] | Any] | tuple[Any | list[Any], list[Basic | Any], dict[Any, Any]] | tuple[Any | list[Any], list[Basic | Any]]:
        ...
    
    def schreier_sims_random(self, base=..., gens=..., consec_succ=..., _random_prec=...) -> tuple[Any | list[Any], list[Any]]:
        ...
    
    def schreier_vector(self, alpha):
        ...
    
    def stabilizer(self, alpha) -> PermGroup:
        ...
    
    @property
    def strong_gens(self) -> list[Basic] | list[Basic | Any]:
        ...
    
    def subgroup(self, gens) -> PermutationGroup:
        ...
    
    def subgroup_search(self, prop, base=..., strong_gens=..., tests=..., init_subgroup=...) -> PermutationGroup:
        ...
    
    @property
    def transitivity_degree(self) -> int:
        ...
    
    def sylow_subgroup(self, p) -> PermutationGroup | Self:
        ...
    
    def strong_presentation(self) -> FpGroup | tuple[Any, Any] | tuple[Any | list[Any], Any | list[Any]]:
        ...
    
    def presentation(self, eliminate_gens=...) -> FpGroup | tuple[Any, Any] | tuple[Any | list[Any], Any | list[Any]] | Any:
        ...
    
    def polycyclic_group(self) -> PolycyclicGroup:
        ...
    


PermGroup = PermutationGroup
class SymmetricPermutationGroup(Basic):
    def __new__(cls, deg) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __contains__(self, i) -> bool:
        ...
    
    def order(self) -> type[UndefinedFunction]:
        ...
    
    @property
    def degree(self) -> Basic:
        ...
    
    @property
    def identity(self) -> Permutation:
        ...
    


class Coset(Basic):
    def __new__(cls, g, H, G=..., dir=...) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @property
    def is_left_coset(self) -> bool:
        ...
    
    @property
    def is_right_coset(self) -> bool:
        ...
    
    def as_list(self) -> list[Any]:
        ...
    


