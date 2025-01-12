from typing import Tuple, Union, Literal
from numpy.typing import ArrayLike

# Author: Wei Xue <xuewei4d@gmail.com>
# Modified by Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import numpy as np
from numpy.random import RandomState

from scipy import linalg

from ._base import BaseMixture, _check_shape
from ..utils import check_array
from ..utils.extmath import row_norms
from numpy import float64, ndarray

###############################################################################
# Gaussian mixture shape checkers used by the GaussianMixture class

def _check_weights(weights, n_components): ...
def _check_means(means: ndarray, n_components: int, n_features: int) -> ndarray: ...
def _check_precision_positivity(precision, covariance_type): ...
def _check_precision_matrix(precision: ndarray, covariance_type: str) -> None: ...
def _check_precisions_full(precisions, covariance_type): ...
def _check_precisions(precisions, covariance_type, n_components, n_features): ...

###############################################################################
# Gaussian mixture parameters estimators (used by the M-Step)

def _estimate_gaussian_covariances_full(
    resp: ndarray, X: ndarray, nk: ndarray, means: ndarray, reg_covar: Union[int, float]
) -> ndarray: ...
def _estimate_gaussian_covariances_tied(resp: ndarray, X: ndarray, nk: ndarray, means: ndarray, reg_covar: float) -> ndarray: ...
def _estimate_gaussian_covariances_diag(resp: ndarray, X: ndarray, nk: ndarray, means: ndarray, reg_covar: float) -> ndarray: ...
def _estimate_gaussian_covariances_spherical(
    resp: ndarray, X: ndarray, nk: ndarray, means: ndarray, reg_covar: float
) -> ndarray: ...
def _estimate_gaussian_parameters(
    X: ndarray, resp: ndarray, reg_covar: Union[int, float], covariance_type: str
) -> Tuple[ndarray, ndarray, ndarray]: ...
def _compute_precision_cholesky(covariances: ndarray, covariance_type: str) -> ndarray: ...

###############################################################################
# Gaussian mixture probability estimators
def _compute_log_det_cholesky(matrix_chol: ndarray, covariance_type: str, n_features: int) -> Union[ndarray, float64]: ...
def _estimate_log_gaussian_prob(X: ndarray, means: ndarray, precisions_chol: ndarray, covariance_type: str) -> ndarray: ...

class GaussianMixture(BaseMixture):
    def __init__(
        self,
        n_components: int = 1,
        *,
        covariance_type: Literal["full", "tied", "diag", "spherical"] = "full",
        tol: float = 1e-3,
        reg_covar: float = 1e-6,
        max_iter: int = 100,
        n_init: int = 1,
        init_params: Literal["kmeans", "k-means++", "random", "random_from_data"] = "kmeans",
        weights_init: ArrayLike | None = None,
        means_init: ArrayLike | None = None,
        precisions_init: ArrayLike | None = None,
        random_state: int | RandomState | None = None,
        warm_start: bool = False,
        verbose: int = 0,
        verbose_interval: int = 10,
    ) -> None: ...
    def _check_parameters(self, X: ndarray) -> None: ...
    def _initialize(self, X: ndarray, resp: ndarray) -> None: ...
    def _m_step(self, X: ndarray, log_resp: ndarray) -> None: ...
    def _estimate_log_prob(self, X: ndarray) -> ndarray: ...
    def _estimate_log_weights(self) -> ndarray: ...
    def _compute_lower_bound(self, _: ndarray, log_prob_norm: float64) -> float64: ...
    def _get_parameters(self) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
    def _set_parameters(self, params: Tuple[ndarray, ndarray, ndarray, ndarray]) -> None: ...
    def _n_parameters(self) -> int: ...
    def bic(self, X: ArrayLike) -> float: ...
    def aic(self, X: ArrayLike) -> float: ...
