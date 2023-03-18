from .._typing import MatrixLike, ArrayLike, Float
from scipy.special import expit as logistic_sigmoid, xlogy as xlogy

# Author: Issam H. Laradji <issam.laradji@gmail.com>
# License: BSD 3 clause

import numpy as np


def inplace_identity(X: MatrixLike) -> None:
    ...


def inplace_logistic(X: MatrixLike) -> None:
    ...


def inplace_tanh(X: MatrixLike):
    ...


def inplace_relu(X: MatrixLike) -> None:
    ...


def inplace_softmax(X: MatrixLike) -> None:
    ...


ACTIVATIONS: dict = ...


def inplace_identity_derivative(Z: MatrixLike, delta: MatrixLike):
    ...


def inplace_logistic_derivative(Z: MatrixLike, delta: MatrixLike):
    ...


def inplace_tanh_derivative(Z: MatrixLike, delta: MatrixLike):
    ...


def inplace_relu_derivative(Z: MatrixLike, delta: MatrixLike) -> None:
    ...


DERIVATIVES: dict = ...


def squared_loss(
    y_true: MatrixLike | ArrayLike, y_pred: MatrixLike | ArrayLike
) -> Float:
    ...


def log_loss(y_true: MatrixLike | ArrayLike, y_prob: MatrixLike) -> Float:
    ...


def binary_log_loss(y_true: MatrixLike | ArrayLike, y_prob: MatrixLike) -> Float:
    ...


LOSS_FUNCTIONS: dict = ...
