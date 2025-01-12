from numpy.typing import ArrayLike, NDArray

# Author: Issam H. Laradji <issam.laradji@gmail.com>
# License: BSD 3 clause

import numpy as np

from scipy.special import expit as logistic_sigmoid
from scipy.special import xlogy
from numpy import float64, ndarray

def inplace_identity(X: NDArray | ArrayLike) -> None: ...
def inplace_logistic(X: NDArray | ArrayLike) -> None: ...
def inplace_tanh(X: NDArray | ArrayLike): ...
def inplace_relu(X: NDArray | ArrayLike) -> None: ...
def inplace_softmax(X: NDArray | ArrayLike) -> None: ...

ACTIVATIONS: dict = ...

def inplace_identity_derivative(Z: NDArray | ArrayLike, delta: ArrayLike): ...
def inplace_logistic_derivative(Z: NDArray | ArrayLike, delta: ArrayLike): ...
def inplace_tanh_derivative(Z: NDArray | ArrayLike, delta: ArrayLike): ...
def inplace_relu_derivative(Z: NDArray | ArrayLike, delta: ArrayLike) -> None: ...

DERIVATIVES: dict = ...

def squared_loss(y_true: ArrayLike, y_pred: ArrayLike) -> float: ...
def log_loss(y_true: ArrayLike, y_prob: ArrayLike) -> float: ...
def binary_log_loss(y_true: ArrayLike, y_prob: ArrayLike) -> float: ...

LOSS_FUNCTIONS: dict = ...
