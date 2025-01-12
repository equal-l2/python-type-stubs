from numpy import ndarray
from typing import Dict, Optional, Tuple, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Nicolas Tresegnie <nicolas.tresegnie@gmail.com>
#          Sergey Feldman <sergeyfeldman@gmail.com>
# License: BSD 3 clause

import numbers
import warnings
from collections import Counter

import numpy as np
import numpy.ma as ma
from scipy import sparse as sp

from ..base import BaseEstimator, TransformerMixin
from ..utils.fixes import _mode
from ..utils.sparsefuncs import _get_median
from ..utils.validation import check_is_fitted
from ..utils.validation import FLOAT_DTYPES
from ..utils.validation import _check_feature_names_in
from ..utils._mask import _get_mask
from ..utils import _is_pandas_na
from ..utils import is_scalar_nan

def _check_inputs_dtype(X: ndarray, missing_values: float) -> None: ...
def _most_frequent(array, extra_value, n_repeat): ...

class _BaseImputer(TransformerMixin, BaseEstimator):
    def __init__(self, *, missing_values=..., add_indicator=False) -> None: ...
    def _fit_indicator(self, X: ndarray) -> None: ...
    def _transform_indicator(self, X: ndarray) -> Optional[ndarray]: ...
    def _concatenate_indicator(self, X_imputed: ndarray, X_indicator: Optional[ndarray]) -> ndarray: ...
    def _concatenate_indicator_feature_names_out(self, names, input_features): ...
    def _more_tags(self) -> Dict[str, bool]: ...

class SimpleImputer(_BaseImputer):
    def __init__(
        self,
        *,
        missing_values: int | float | str | None = ...,
        strategy: str = "mean",
        fill_value: str | int | float | None = None,
        verbose: int | str = "deprecated",
        copy: bool = True,
        add_indicator: bool = False,
    ) -> None: ...
    def _validate_input(self, X: ndarray, in_fit: bool) -> ndarray: ...
    def fit(self, X: NDArray | ArrayLike, y: Optional[ndarray] = None) -> "SimpleImputer": ...
    def _sparse_fit(self, X, strategy, missing_values, fill_value): ...
    def _dense_fit(self, X: ndarray, strategy: str, missing_values: float, fill_value: int) -> ndarray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

class MissingIndicator(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        missing_values: int | float | str | None = ...,
        features: Literal["missing-only", "all"] = "missing-only",
        sparse: bool | Literal["auto"] = "auto",
        error_on_new: bool = True,
    ) -> None: ...
    def _get_missing_features_info(self, X: ndarray) -> Tuple[ndarray, ndarray]: ...
    def _validate_input(self, X, in_fit): ...
    def _fit(self, X: ndarray, y: None = None, precomputed: bool = False) -> ndarray: ...
    def fit(self, X: NDArray | ArrayLike, y=None) -> Any: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def fit_transform(self, X: NDArray | ArrayLike, y=None) -> NDArray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def _more_tags(self): ...
