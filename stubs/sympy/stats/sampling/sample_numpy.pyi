from functools import singledispatch
from sympy.stats.crv_types import BetaDistribution, ChiSquaredDistribution, ExponentialDistribution, FDistributionDistribution, GammaDistribution, GumbelDistribution, LaplaceDistribution, LogNormalDistribution, LogisticDistribution, NormalDistribution, ParetoDistribution, RayleighDistribution, TriangularDistribution, UniformDistribution
from sympy.stats.drv_types import GeometricDistribution, PoissonDistribution, ZetaDistribution
from sympy.stats.frv_types import BinomialDistribution, HypergeometricDistribution

numpy = ...
@singledispatch
def do_sample_numpy(dist, size, rand_state) -> None:
    ...

@do_sample_numpy.register(BetaDistribution)
def _(dist: BetaDistribution, size, rand_state):
    ...

@do_sample_numpy.register(ChiSquaredDistribution)
def _(dist: ChiSquaredDistribution, size, rand_state):
    ...

@do_sample_numpy.register(ExponentialDistribution)
def _(dist: ExponentialDistribution, size, rand_state):
    ...

@do_sample_numpy.register(FDistributionDistribution)
def _(dist: FDistributionDistribution, size, rand_state):
    ...

@do_sample_numpy.register(GammaDistribution)
def _(dist: GammaDistribution, size, rand_state):
    ...

@do_sample_numpy.register(GumbelDistribution)
def _(dist: GumbelDistribution, size, rand_state):
    ...

@do_sample_numpy.register(LaplaceDistribution)
def _(dist: LaplaceDistribution, size, rand_state):
    ...

@do_sample_numpy.register(LogisticDistribution)
def _(dist: LogisticDistribution, size, rand_state):
    ...

@do_sample_numpy.register(LogNormalDistribution)
def _(dist: LogNormalDistribution, size, rand_state):
    ...

@do_sample_numpy.register(NormalDistribution)
def _(dist: NormalDistribution, size, rand_state):
    ...

@do_sample_numpy.register(RayleighDistribution)
def _(dist: RayleighDistribution, size, rand_state):
    ...

@do_sample_numpy.register(ParetoDistribution)
def _(dist: ParetoDistribution, size, rand_state):
    ...

@do_sample_numpy.register(TriangularDistribution)
def _(dist: TriangularDistribution, size, rand_state):
    ...

@do_sample_numpy.register(UniformDistribution)
def _(dist: UniformDistribution, size, rand_state):
    ...

@do_sample_numpy.register(GeometricDistribution)
def _(dist: GeometricDistribution, size, rand_state):
    ...

@do_sample_numpy.register(PoissonDistribution)
def _(dist: PoissonDistribution, size, rand_state):
    ...

@do_sample_numpy.register(ZetaDistribution)
def _(dist: ZetaDistribution, size, rand_state):
    ...

@do_sample_numpy.register(BinomialDistribution)
def _(dist: BinomialDistribution, size, rand_state):
    ...

@do_sample_numpy.register(HypergeometricDistribution)
def _(dist: HypergeometricDistribution, size, rand_state):
    ...

