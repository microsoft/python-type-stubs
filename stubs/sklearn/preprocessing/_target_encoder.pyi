from typing import ClassVar, Literal
from typing_extensions import Self

from numpy import ndarray

from .._typing import ArrayLike, Int, MatrixLike
from ..base import OneToOneFeatureMixin
from ._encoders import _BaseEncoder

class TargetEncoder(OneToOneFeatureMixin, _BaseEncoder):
    """Target Encoder for regression and classification targets.

    Each category is encoded based on a shrunk estimate of the average target
    values for observations belonging to the category. The encoding scheme mixes
    the global target mean with the target mean conditioned on the value of the
    category (see [MIC]_).

    When the target type is "multiclass", encodings are based
    on the conditional probability estimate for each class. The target is first
    binarized using the "one-vs-all" scheme via
    :class:`~sklearn.preprocessing.LabelBinarizer`, then the average target
    value for each class and each category is used for encoding, resulting in
    `n_features` * `n_classes` encoded output features.

    :class:`TargetEncoder` considers missing values, such as `np.nan` or `None`,
    as another category and encodes them like any other category. Categories
    that are not seen during :meth:`fit` are encoded with the target mean, i.e.
    `target_mean_`.

    For a demo on the importance of the `TargetEncoder` internal cross-fitting,
    see
    :ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder_cross_val.py`.
    For a comparison of different encoders, refer to
    :ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder.py`. Read
    more in the :ref:`User Guide <target_encoder>`.

    .. note::
        `fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a
        :term:`cross fitting` scheme is used in `fit_transform` for encoding.
        See the :ref:`User Guide <target_encoder>` for details.

    .. versionadded:: 1.3

    Parameters
    ----------
    categories : "auto" or list of shape (n_features,) of array-like, default="auto"
        Categories (unique values) per feature:

        - `"auto"` : Determine categories automatically from the training data.
        - list : `categories[i]` holds the categories expected in the i-th column. The
          passed categories should not mix strings and numeric values within a single
          feature, and should be sorted in case of numeric values.

        The used categories are stored in the `categories_` fitted attribute.

    target_type : {"auto", "continuous", "binary", "multiclass"}, default="auto"
        Type of target.

        - `"auto"` : Type of target is inferred with
          :func:`~sklearn.utils.multiclass.type_of_target`.
        - `"continuous"` : Continuous target
        - `"binary"` : Binary target
        - `"multiclass"` : Multiclass target

        .. note::
            The type of target inferred with `"auto"` may not be the desired target
            type used for modeling. For example, if the target consisted of integers
            between 0 and 100, then :func:`~sklearn.utils.multiclass.type_of_target`
            will infer the target as `"multiclass"`. In this case, setting
            `target_type="continuous"` will specify the target as a regression
            problem. The `target_type_` attribute gives the target type used by the
            encoder.

        .. versionchanged:: 1.4
           Added the option 'multiclass'.

    smooth : "auto" or float, default="auto"
        The amount of mixing of the target mean conditioned on the value of the
        category with the global target mean. A larger `smooth` value will put
        more weight on the global target mean.
        If `"auto"`, then `smooth` is set to an empirical Bayes estimate.

    cv : int, default=5
        Determines the number of folds in the :term:`cross fitting` strategy used in
        :meth:`fit_transform`. For classification targets, `StratifiedKFold` is used
        and for continuous targets, `KFold` is used.

    shuffle : bool, default=True
        Whether to shuffle the data in :meth:`fit_transform` before splitting into
        folds. Note that the samples within each split will not be shuffled.

    random_state : int, RandomState instance or None, default=None
        When `shuffle` is True, `random_state` affects the ordering of the
        indices, which controls the randomness of each fold. Otherwise, this
        parameter has no effect.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    encodings_ : list of shape (n_features,) or (n_features * n_classes) of \
                    ndarray
        Encodings learnt on all of `X`.
        For feature `i`, `encodings_[i]` are the encodings matching the
        categories listed in `categories_[i]`. When `target_type_` is
        "multiclass", the encoding for feature `i` and class `j` is stored in
        `encodings_[j + (i * len(classes_))]`. E.g., for 2 features (f) and
        3 classes (c), encodings are ordered:
        f0_c0, f0_c1, f0_c2, f1_c0, f1_c1, f1_c2,

    categories_ : list of shape (n_features,) of ndarray
        The categories of each input feature determined during fitting or
        specified in `categories`
        (in order of the features in `X` and corresponding with the output
        of :meth:`transform`).

    target_type_ : str
        Type of target.

    target_mean_ : float
        The overall mean of the target. This value is only used in :meth:`transform`
        to encode categories.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

    classes_ : ndarray or None
        If `target_type_` is 'binary' or 'multiclass', holds the label for each class,
        otherwise `None`.

    See Also
    --------
    OrdinalEncoder : Performs an ordinal (integer) encoding of the categorical features.
        Contrary to TargetEncoder, this encoding is not supervised. Treating the
        resulting encoding as a numerical features therefore lead arbitrarily
        ordered values and therefore typically lead to lower predictive performance
        when used as preprocessing for a classifier or regressor.
    OneHotEncoder : Performs a one-hot encoding of categorical features. This
        unsupervised encoding is better suited for low cardinality categorical
        variables as it generate one new feature per unique category.

    References
    ----------
    .. [MIC] :doi:`Micci-Barreca, Daniele. "A preprocessing scheme for high-cardinality
       categorical attributes in classification and prediction problems"
       SIGKDD Explor. Newsl. 3, 1 (July 2001), 27-32. <10.1145/507533.507538>`

    Examples
    --------
    With `smooth="auto"`, the smoothing parameter is set to an empirical Bayes estimate:

    >>> import numpy as np
    >>> from sklearn.preprocessing import TargetEncoder
    >>> X = np.array([["dog"] * 20 + ["cat"] * 30 + ["snake"] * 38], dtype=object).T
    >>> y = [90.3] * 5 + [80.1] * 15 + [20.4] * 5 + [20.1] * 25 + [21.2] * 8 + [49] * 30
    >>> enc_auto = TargetEncoder(smooth="auto")
    >>> X_trans = enc_auto.fit_transform(X, y)

    >>> # A high `smooth` parameter puts more weight on global mean on the categorical
    >>> # encodings:
    >>> enc_high_smooth = TargetEncoder(smooth=5000.0).fit(X, y)
    >>> enc_high_smooth.target_mean_
    np.float64(44.3)
    >>> enc_high_smooth.encodings_
    [array([44.1, 44.4, 44.3])]

    >>> # On the other hand, a low `smooth` parameter puts more weight on target
    >>> # conditioned on the value of the categorical:
    >>> enc_low_smooth = TargetEncoder(smooth=1.0).fit(X, y)
    >>> enc_low_smooth.encodings_
    [array([21, 80.8, 43.2])]
    """

    encodings_: list[ndarray]
    categories_: list[ndarray]
    target_type_: str
    target_mean_: float
    n_features_in_: int
    feature_names_in_: ndarray
    classes_: ndarray | None

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        categories: list[ArrayLike] | Literal["auto"] = "auto",
        target_type: Literal["auto", "continuous", "binary", "multiclass"] = "auto",
        smooth: Literal["auto"] | float = "auto",
        cv: int = 5,
        shuffle: bool = True,
        random_state: Int | None = None,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: ArrayLike) -> Self: ...
    def fit_transform(self, X: MatrixLike, y: ArrayLike) -> ndarray: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> ndarray: ...
    def __sklearn_tags__(self) -> dict: ...
