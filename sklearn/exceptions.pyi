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
    pass

class ConvergenceWarning(UserWarning):
    pass

class DataConversionWarning(UserWarning):
    pass

class DataDimensionalityWarning(UserWarning):
    pass

class EfficiencyWarning(UserWarning):
    pass

class FitFailedWarning(RuntimeWarning):
    pass

class SkipTestWarning(UserWarning):
    pass

class UndefinedMetricWarning(UserWarning):
    pass

class PositiveSpectrumWarning(UserWarning):
    pass
