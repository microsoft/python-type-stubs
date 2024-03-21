from functools import singledispatch
from sympy.stats.crv_types import BetaDistribution, CauchyDistribution, ChiSquaredDistribution, ExponentialDistribution, GammaDistribution, GaussianInverseDistribution, LogNormalDistribution, NormalDistribution, ParetoDistribution, UniformDistribution
from sympy.stats.drv_types import GeometricDistribution, NegativeBinomialDistribution, PoissonDistribution
from sympy.stats.frv_types import BernoulliDistribution, BinomialDistribution

@singledispatch
def do_sample_pymc(dist) -> None:
    ...

@do_sample_pymc.register(BetaDistribution)
def _(dist: BetaDistribution):
    ...

@do_sample_pymc.register(CauchyDistribution)
def _(dist: CauchyDistribution):
    ...

@do_sample_pymc.register(ChiSquaredDistribution)
def _(dist: ChiSquaredDistribution):
    ...

@do_sample_pymc.register(ExponentialDistribution)
def _(dist: ExponentialDistribution):
    ...

@do_sample_pymc.register(GammaDistribution)
def _(dist: GammaDistribution):
    ...

@do_sample_pymc.register(LogNormalDistribution)
def _(dist: LogNormalDistribution):
    ...

@do_sample_pymc.register(NormalDistribution)
def _(dist: NormalDistribution):
    ...

@do_sample_pymc.register(GaussianInverseDistribution)
def _(dist: GaussianInverseDistribution):
    ...

@do_sample_pymc.register(ParetoDistribution)
def _(dist: ParetoDistribution):
    ...

@do_sample_pymc.register(UniformDistribution)
def _(dist: UniformDistribution):
    ...

@do_sample_pymc.register(GeometricDistribution)
def _(dist: GeometricDistribution):
    ...

@do_sample_pymc.register(NegativeBinomialDistribution)
def _(dist: NegativeBinomialDistribution):
    ...

@do_sample_pymc.register(PoissonDistribution)
def _(dist: PoissonDistribution):
    ...

@do_sample_pymc.register(BernoulliDistribution)
def _(dist: BernoulliDistribution):
    ...

@do_sample_pymc.register(BinomialDistribution)
def _(dist: BinomialDistribution):
    ...

