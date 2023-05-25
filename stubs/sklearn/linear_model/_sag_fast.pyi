  
import numpy as np
from ..utils._seq_dataset import SequentialDataset32, SequentialDataset64


def sag32(
    dataset: SequentialDataset32,
    weights_array: np.ndarray,
    intercept_array: np.ndarray,
    n_samples: int,
    n_features: int,
    n_classes: int,
    tol: float,
    max_iter: int,
    loss_function: str,
    step_size: float,
    alpha: float,
    beta: float,
    sum_gradient_init: np.ndarray,
    gradient_memory_init: np.ndarray,
    seen_init: np.ndarray,
    num_seen: int,
    fit_intercept: bool,
    intercept_sum_gradient_init: np.ndarray,
    intercept_decay: float,
    saga: bool,
    verbose: bool
) -> tuple[int, int]: ...


def sag64(
    dataset: SequentialDataset64,
    weights_array: np.ndarray,
    intercept_array: np.ndarray,
    n_samples: int,
    n_features: int,
    n_classes: int,
    tol: float,
    max_iter: int,
    loss_function: str,
    step_size: float,
    alpha: float,
    beta: float,
    sum_gradient_init: np.ndarray,
    gradient_memory_init: np.ndarray,
    seen_init: np.ndarray,
    num_seen: int,
    fit_intercept: bool,
    intercept_sum_gradient_init: np.ndarray,
    intercept_decay: float,
    saga: bool,
    verbose: bool
) -> tuple[int, int]: ...
