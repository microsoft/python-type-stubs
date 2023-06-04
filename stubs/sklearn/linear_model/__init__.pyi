from ._glm import (
    PoissonRegressor as PoissonRegressor,
    GammaRegressor as GammaRegressor,
    TweedieRegressor as TweedieRegressor,
)
from ._perceptron import Perceptron as Perceptron
from ._stochastic_gradient import (
    SGDClassifier as SGDClassifier,
    SGDRegressor as SGDRegressor,
    SGDOneClassSVM as SGDOneClassSVM,
)
from ._least_angle import (
    Lars as Lars,
    LassoLars as LassoLars,
    lars_path as lars_path,
    lars_path_gram as lars_path_gram,
    LarsCV as LarsCV,
    LassoLarsCV as LassoLarsCV,
    LassoLarsIC as LassoLarsIC,
)
from ._huber import HuberRegressor as HuberRegressor
from ._base import LinearRegression as LinearRegression
from ._theil_sen import TheilSenRegressor as TheilSenRegressor
from ._omp import (
    orthogonal_mp as orthogonal_mp,
    orthogonal_mp_gram as orthogonal_mp_gram,
    OrthogonalMatchingPursuit as OrthogonalMatchingPursuit,
    OrthogonalMatchingPursuitCV as OrthogonalMatchingPursuitCV,
)
from ._logistic import (
    LogisticRegression as LogisticRegression,
    LogisticRegressionCV as LogisticRegressionCV,
)
from ._ransac import RANSACRegressor as RANSACRegressor
from ._sgd_fast import (
    Hinge as Hinge,
    Log as Log,
    ModifiedHuber as ModifiedHuber,
    SquaredLoss as SquaredLoss,
    Huber as Huber,
)
from ._bayes import BayesianRidge as BayesianRidge, ARDRegression as ARDRegression
from ._coordinate_descent import (
    Lasso as Lasso,
    ElasticNet as ElasticNet,
    LassoCV as LassoCV,
    ElasticNetCV as ElasticNetCV,
    lasso_path as lasso_path,
    enet_path as enet_path,
    MultiTaskLasso as MultiTaskLasso,
    MultiTaskElasticNet as MultiTaskElasticNet,
    MultiTaskElasticNetCV as MultiTaskElasticNetCV,
    MultiTaskLassoCV as MultiTaskLassoCV,
)
from ._passive_aggressive import (
    PassiveAggressiveClassifier as PassiveAggressiveClassifier,
    PassiveAggressiveRegressor as PassiveAggressiveRegressor,
)
from ._quantile import QuantileRegressor as QuantileRegressor
from ._ridge import (
    Ridge as Ridge,
    RidgeCV as RidgeCV,
    RidgeClassifier as RidgeClassifier,
    RidgeClassifierCV as RidgeClassifierCV,
    ridge_regression as ridge_regression,
)

__all__ = [
    "ARDRegression",
    "BayesianRidge",
    "ElasticNet",
    "ElasticNetCV",
    "Hinge",
    "Huber",
    "HuberRegressor",
    "Lars",
    "LarsCV",
    "Lasso",
    "LassoCV",
    "LassoLars",
    "LassoLarsCV",
    "LassoLarsIC",
    "LinearRegression",
    "Log",
    "LogisticRegression",
    "LogisticRegressionCV",
    "ModifiedHuber",
    "MultiTaskElasticNet",
    "MultiTaskElasticNetCV",
    "MultiTaskLasso",
    "MultiTaskLassoCV",
    "OrthogonalMatchingPursuit",
    "OrthogonalMatchingPursuitCV",
    "PassiveAggressiveClassifier",
    "PassiveAggressiveRegressor",
    "Perceptron",
    "QuantileRegressor",
    "Ridge",
    "RidgeCV",
    "RidgeClassifier",
    "RidgeClassifierCV",
    "SGDClassifier",
    "SGDRegressor",
    "SGDOneClassSVM",
    "SquaredLoss",
    "TheilSenRegressor",
    "enet_path",
    "lars_path",
    "lars_path_gram",
    "lasso_path",
    "orthogonal_mp",
    "orthogonal_mp_gram",
    "ridge_regression",
    "RANSACRegressor",
    "PoissonRegressor",
    "GammaRegressor",
    "TweedieRegressor",
]
