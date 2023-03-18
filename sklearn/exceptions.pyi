__all__ = [
    "NotFittedError",
    "ConvergenceWarning",
    "DataConversionWarning",
    "DataDimensionalityWarning",
    "EfficiencyWarning",
    "FitFailedWarning",
    "SkipTestWarning",
    "UndefinedMetricWarning",
    "PositiveSpectrumWarning",
]


class NotFittedError(ValueError, AttributeError):
    ...


class ConvergenceWarning(UserWarning):
    ...


class DataConversionWarning(UserWarning):
    ...


class DataDimensionalityWarning(UserWarning):
    ...


class EfficiencyWarning(UserWarning):
    ...


class FitFailedWarning(RuntimeWarning):
    ...


class SkipTestWarning(UserWarning):
    ...


class UndefinedMetricWarning(UserWarning):
    ...


class PositiveSpectrumWarning(UserWarning):
    ...
