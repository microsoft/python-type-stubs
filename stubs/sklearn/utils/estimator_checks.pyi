from typing import Sequence
from scipy import sparse as sparse
from ..exceptions import (
    DataConversionWarning as DataConversionWarning,
    NotFittedError as NotFittedError,
    SkipTestWarning as SkipTestWarning,
)
from ..base import BaseEstimator
from ..random_projection import BaseRandomProjection as BaseRandomProjection
from inspect import signature as signature
from .validation import has_fit_parameter as has_fit_parameter
from ..metrics import (
    accuracy_score as accuracy_score,
    adjusted_rand_score as adjusted_rand_score,
    f1_score as f1_score,
)
from ..utils.fixes import sp_version as sp_version, parse_version as parse_version
from ._param_validation import Interval as Interval
from ..preprocessing import StandardScaler as StandardScaler, scale as scale
from ..linear_model import (
    LinearRegression as LinearRegression,
    LogisticRegression as LogisticRegression,
    RANSACRegressor as RANSACRegressor,
    Ridge as Ridge,
    SGDRegressor as SGDRegressor,
)
from copy import deepcopy as deepcopy
from ..datasets import (
    load_iris as load_iris,
    make_blobs as make_blobs,
    make_multilabel_classification as make_multilabel_classification,
    make_regression as make_regression,
)
from ..metrics.pairwise import (
    rbf_kernel as rbf_kernel,
    linear_kernel as linear_kernel,
    pairwise_distances as pairwise_distances,
)
from .. import config_context as config_context
from collections.abc import Generator
from ..utils.validation import check_is_fitted as check_is_fitted
from ..pipeline import make_pipeline as make_pipeline
from scipy.stats import rankdata as rankdata
from _pytest.mark.structures import MarkDecorator
from ..utils._param_validation import (
    make_constraint as make_constraint,
    generate_invalid_param_val as generate_invalid_param_val,
    InvalidParameterError as InvalidParameterError,
)
from numbers import Real as Real
from functools import partial as partial, wraps as wraps
from ..base import (
    clone as clone,
    ClusterMixin as ClusterMixin,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
    is_outlier_detector as is_outlier_detector,
    RegressorMixin as RegressorMixin,
)
from ..model_selection import (
    train_test_split as train_test_split,
    ShuffleSplit as ShuffleSplit,
)
from . import IS_PYPY as IS_PYPY, is_scalar_nan as is_scalar_nan, shuffle as shuffle
from ._testing import (
    assert_raise_message as assert_raise_message,
    assert_array_equal as assert_array_equal,
    assert_array_almost_equal as assert_array_almost_equal,
    assert_allclose as assert_allclose,
    assert_allclose_dense_sparse as assert_allclose_dense_sparse,
    assert_array_less as assert_array_less,
    set_random_state as set_random_state,
    SkipTest as SkipTest,
    ignore_warnings as ignore_warnings,
    create_memmap_backed_data as create_memmap_backed_data,
    raises as raises,
)
from ..feature_selection import (
    SelectKBest as SelectKBest,
    SelectFromModel as SelectFromModel,
)
from pytest.mark import parameterize
from .._typing import ArrayLike
import types
import warnings
import pickle
import re

import numpy as np
import joblib

REGRESSION_DATASET = ...
CROSS_DECOMPOSITION: list = ...


def check_supervised_y_no_nan(name, estimator_orig):
    ...


def parametrize_with_checks(
    estimators: Sequence[BaseEstimator],
) -> MarkDecorator | parameterize:
    ...


def check_estimator(
    estimator: None | BaseEstimator = None,
    generate_only: bool = False,
    Estimator: str | BaseEstimator = "deprecated",
) -> Generator:
    ...


class _NotAnArray:
    def __init__(self, data: ArrayLike) -> None:
        ...

    def __array__(self, dtype=None):
        ...

    def __array_function__(self, func, types, args, kwargs):
        ...


def check_estimator_sparse_data(name, estimator_orig):
    ...


def check_sample_weights_pandas_series(name, estimator_orig):
    ...


def check_sample_weights_not_an_array(name, estimator_orig):
    ...


def check_sample_weights_list(name, estimator_orig):
    ...


def check_sample_weights_shape(name, estimator_orig):
    ...


def check_sample_weights_invariance(name, estimator_orig, kind: str = "ones"):
    ...


def check_sample_weights_not_overwritten(name, estimator_orig):
    ...


def check_dtype_object(name, estimator_orig):
    ...


def check_complex_data(name, estimator_orig):
    ...


def check_dict_unchanged(name, estimator_orig):
    ...


def check_dont_overwrite_parameters(name, estimator_orig):
    ...


def check_fit2d_predict1d(name, estimator_orig):
    ...


def check_methods_subset_invariance(name, estimator_orig):
    ...


def check_methods_sample_order_invariance(name, estimator_orig):
    ...


def check_fit2d_1sample(name, estimator_orig):
    ...


def check_fit2d_1feature(name, estimator_orig):
    ...


def check_fit1d(name, estimator_orig):
    ...


def check_transformer_general(name, transformer, readonly_memmap: bool = False):
    ...


def check_transformer_data_not_an_array(name, transformer):
    ...


def check_transformers_unfitted(name, transformer):
    ...


def check_pipeline_consistency(name, estimator_orig):
    ...


def check_fit_score_takes_y(name, estimator_orig):
    ...


def check_estimators_dtypes(name, estimator_orig):
    ...


def check_transformer_preserve_dtypes(name, transformer_orig):
    ...


def check_estimators_empty_data_messages(name, estimator_orig):
    ...


def check_estimators_nan_inf(name, estimator_orig):
    ...


def check_nonsquare_error(name, estimator_orig):
    ...


def check_estimators_pickle(name, estimator_orig):
    ...


def check_estimators_partial_fit_n_features(name, estimator_orig):
    ...


def check_classifier_multioutput(name, estimator):
    ...


def check_regressor_multioutput(name, estimator):
    ...


def check_clustering(name, clusterer_orig, readonly_memmap: bool = False):
    ...


def check_clusterer_compute_labels_predict(name, clusterer_orig):
    ...


def check_classifiers_one_label(name, classifier_orig):
    ...


def check_classifiers_one_label_sample_weights(name, classifier_orig):
    ...


def check_classifiers_train(
    name, classifier_orig, readonly_memmap: bool = False, X_dtype: str = "float64"
):
    ...


def check_outlier_corruption(num_outliers, expected_outliers, decision):
    ...


def check_outliers_train(name, estimator_orig, readonly_memmap: bool = True):
    ...


def check_outlier_contamination(name, estimator_orig):
    ...


def check_classifiers_multilabel_representation_invariance(name, classifier_orig):
    ...


def check_classifiers_multilabel_output_format_predict(name, classifier_orig):
    ...


def check_classifiers_multilabel_output_format_predict_proba(name, classifier_orig):
    ...


def check_classifiers_multilabel_output_format_decision_function(name, classifier_orig):
    ...


def check_get_feature_names_out_error(name, estimator_orig):
    ...


def check_estimators_fit_returns_self(
    name, estimator_orig, readonly_memmap: bool = False
):
    ...


def check_estimators_unfitted(name, estimator_orig):
    ...


def check_supervised_y_2d(name, estimator_orig):
    ...


def check_classifiers_predictions(X, y, name, classifier_orig):
    ...


def check_classifiers_classes(name, classifier_orig):
    ...


def check_regressors_int(name, regressor_orig):
    ...


def check_regressors_train(
    name, regressor_orig, readonly_memmap: bool = False, X_dtype=...
):
    ...


def check_regressors_no_decision_function(name, regressor_orig):
    ...


def check_class_weight_classifiers(name, classifier_orig):
    ...


def check_class_weight_balanced_classifiers(
    name, classifier_orig, X_train, y_train, X_test, y_test, weights
):
    ...


def check_class_weight_balanced_linear_classifier(name, Classifier):
    ...


def check_estimators_overwrite_params(name, estimator_orig):
    ...


def check_no_attributes_set_in_init(name, estimator_orig):
    ...


def check_sparsify_coefficients(name, estimator_orig):
    ...


def check_classifier_data_not_an_array(name, estimator_orig):
    ...


def check_regressor_data_not_an_array(name, estimator_orig):
    ...


def check_estimators_data_not_an_array(name, estimator_orig, X, y, obj_type):
    ...


def check_parameters_default_constructible(name, Estimator):
    ...


def check_non_transformer_estimators_n_iter(name, estimator_orig):
    ...


def check_transformer_n_iter(name, estimator_orig):
    ...


def check_get_params_invariance(name, estimator_orig):
    ...


def check_set_params(name, estimator_orig):
    ...


def check_classifiers_regression_target(name, estimator_orig):
    ...


def check_decision_proba_consistency(name, estimator_orig):
    ...


def check_outliers_fit_predict(name, estimator_orig):
    ...


def check_fit_non_negative(name, estimator_orig):
    ...


def check_fit_idempotent(name, estimator_orig):
    ...


def check_fit_check_is_fitted(name, estimator_orig):
    ...


def check_n_features_in(name, estimator_orig):
    ...


def check_requires_y_none(name, estimator_orig):
    ...


def check_n_features_in_after_fitting(name, estimator_orig):
    ...


def check_estimator_get_tags_default_keys(name, estimator_orig):
    ...


def check_dataframe_column_names_consistency(name, estimator_orig):
    ...


def check_transformer_get_feature_names_out(name, transformer_orig):
    ...


def check_transformer_get_feature_names_out_pandas(name, transformer_orig):
    ...


def check_param_validation(name, estimator_orig):
    ...


def check_set_output_transform(name, transformer_orig):
    ...


def check_set_output_transform_pandas(name, transformer_orig):
    ...


def check_global_ouptut_transform_pandas(name, transformer_orig):
    ...
