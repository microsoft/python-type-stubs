__all__ = [
    "HasACycle",
    "NodeNotFound",
    "PowerIterationFailedConvergence",
    "ExceededMaxIterations",
    "AmbiguousSolution",
    "NetworkXAlgorithmError",
    "NetworkXException",
    "NetworkXError",
    "NetworkXNoCycle",
    "NetworkXNoPath",
    "NetworkXNotImplemented",
    "NetworkXPointlessConcept",
    "NetworkXUnbounded",
    "NetworkXUnfeasible",
]

class NetworkXException(Exception):
    pass

class NetworkXError(NetworkXException):
    pass

class NetworkXPointlessConcept(NetworkXException):
    pass

class NetworkXAlgorithmError(NetworkXException):
    pass

class NetworkXUnfeasible(NetworkXAlgorithmError):
    pass

class NetworkXNoPath(NetworkXUnfeasible):
    pass

class NetworkXNoCycle(NetworkXUnfeasible):
    pass

class HasACycle(NetworkXException):
    pass

class NetworkXUnbounded(NetworkXAlgorithmError):
    pass

class NetworkXNotImplemented(NetworkXException):
    pass

class NodeNotFound(NetworkXException):
    pass

class AmbiguousSolution(NetworkXException):
    pass

class ExceededMaxIterations(NetworkXException):
    pass

class PowerIterationFailedConvergence(ExceededMaxIterations):
    def __init__(self, num_iterations, *args, **kw): ...
