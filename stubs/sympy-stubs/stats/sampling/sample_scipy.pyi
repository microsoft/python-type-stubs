from functools import singledispatch
from sympy.stats import DiscreteDistributionHandmade
from sympy.stats.crv import SingleContinuousDistribution
from sympy.stats.crv_types import BetaDistribution, CauchyDistribution, ChiSquaredDistribution, ExponentialDistribution, GammaDistribution, LogNormalDistribution, NormalDistribution, ParetoDistribution, StudentTDistribution, UniformDistribution
from sympy.stats.drv_types import GeometricDistribution, LogarithmicDistribution, NegativeBinomialDistribution, PoissonDistribution, SkellamDistribution, YuleSimonDistribution, ZetaDistribution
from sympy.stats.frv import SingleFiniteDistribution

scipy = ...
@singledispatch
def do_sample_scipy(dist, size, seed) -> None | int:
    ...

@do_sample_scipy.register(SingleContinuousDistribution)
def _(dist: SingleContinuousDistribution, size, seed) -> int:
    class scipy_pdf(scipy.stats.rv_continuous):
        ...
    
    

@do_sample_scipy.register(ChiSquaredDistribution)
def _(dist: ChiSquaredDistribution, size, seed):
    ...

@do_sample_scipy.register(ExponentialDistribution)
def _(dist: ExponentialDistribution, size, seed):
    ...

@do_sample_scipy.register(GammaDistribution)
def _(dist: GammaDistribution, size, seed):
    ...

@do_sample_scipy.register(LogNormalDistribution)
def _(dist: LogNormalDistribution, size, seed):
    ...

@do_sample_scipy.register(NormalDistribution)
def _(dist: NormalDistribution, size, seed):
    ...

@do_sample_scipy.register(ParetoDistribution)
def _(dist: ParetoDistribution, size, seed):
    ...

@do_sample_scipy.register(StudentTDistribution)
def _(dist: StudentTDistribution, size, seed):
    ...

@do_sample_scipy.register(UniformDistribution)
def _(dist: UniformDistribution, size, seed):
    ...

@do_sample_scipy.register(BetaDistribution)
def _(dist: BetaDistribution, size, seed):
    ...

@do_sample_scipy.register(CauchyDistribution)
def _(dist: CauchyDistribution, size, seed):
    ...

@do_sample_scipy.register(DiscreteDistributionHandmade)
def _(dist: DiscreteDistributionHandmade, size, seed) -> int:
    class scipy_pmf():
        ...
    
    

@do_sample_scipy.register(GeometricDistribution)
def _(dist: GeometricDistribution, size, seed):
    ...

@do_sample_scipy.register(LogarithmicDistribution)
def _(dist: LogarithmicDistribution, size, seed):
    ...

@do_sample_scipy.register(NegativeBinomialDistribution)
def _(dist: NegativeBinomialDistribution, size, seed):
    ...

@do_sample_scipy.register(PoissonDistribution)
def _(dist: PoissonDistribution, size, seed):
    ...

@do_sample_scipy.register(SkellamDistribution)
def _(dist: SkellamDistribution, size, seed):
    ...

@do_sample_scipy.register(YuleSimonDistribution)
def _(dist: YuleSimonDistribution, size, seed):
    ...

@do_sample_scipy.register(ZetaDistribution)
def _(dist: ZetaDistribution, size, seed):
    ...

@do_sample_scipy.register(SingleFiniteDistribution)
def _(dist: SingleFiniteDistribution, size, seed) -> int:
    ...

