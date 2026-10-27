import sys
import warnings
from typing_extensions import assert_type

import numpy as np
from skimage.measure import CircleModel, EllipseModel, LineModelND
from skimage.transform import (
    AffineTransform,
    EssentialMatrixTransform,
    EuclideanTransform,
    FundamentalMatrixTransform,
    PiecewiseAffineTransform,
    PolynomialTransform,
    ProjectiveTransform,
    SimilarityTransform,
)


def test_legacy_estimation() -> None:
    angles = np.linspace(0, 2 * np.pi, 20, endpoint=False)
    points = np.column_stack((3 * np.cos(angles), 2 * np.sin(angles)))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        circle = CircleModel()
        ellipse = EllipseModel()
        line = LineModelND()
        assert circle.estimate(points)
        assert line.estimate(np.array([[0, 0], [1, 1], [2, 2]]))
        np.testing.assert_allclose(line.predict_y([0, 1]), [0, 1], atol=1e-14)
        assert circle.predict_xy(angles).shape == points.shape
        assert ellipse.predict_xy(angles, params=(0, 0, 3, 2, 0)).shape == points.shape


if sys.version_info >= (3, 11):
    from skimage._shared.utils import FailedEstimation, FailedEstimationAccessError
    from skimage.measure import RansacModelProtocol

    def test_explicit_model_construction() -> None:
        circle = CircleModel(center=(1, 2), radius=3)
        ellipse = EllipseModel(center=(1, 2), axis_lengths=(3, 4), theta=0)
        line = LineModelND(origin=(0, 0), direction=(1, 1))
        np.testing.assert_allclose(circle.predict_xy([0]), [[4, 2]])
        np.testing.assert_allclose(ellipse.predict_xy([0]), [[4, 2]])
        np.testing.assert_allclose(line.predict_y([0, 1]), [0, 1])
        assert isinstance(circle, RansacModelProtocol)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", FutureWarning)
            np.testing.assert_allclose(circle.params, [1, 2, 3])
            np.testing.assert_allclose(ellipse.params, [1, 2, 3, 4, 0])
            origin, direction = line.params
            assert origin is not None
            assert direction is not None
            np.testing.assert_allclose(origin, [0, 0])
            np.testing.assert_allclose(direction, [1, 1])

    def test_model_from_estimate() -> None:
        angles = np.linspace(0, 2 * np.pi, 20, endpoint=False)
        circle_points = np.column_stack((np.cos(angles), np.sin(angles)))
        circle = CircleModel.from_estimate(circle_points)
        assert_type(circle, CircleModel | FailedEstimation)
        assert isinstance(circle, CircleModel)
        assert circle.radius is not None
        np.testing.assert_allclose(circle.radius, 1)
        ellipse = EllipseModel.from_estimate(np.array([[0, 0], [1, 1]]))
        assert_type(ellipse, EllipseModel | FailedEstimation)
        assert isinstance(ellipse, FailedEstimation)
        assert not ellipse
        line = LineModelND.from_estimate(np.array([[0, 0], [1, 1], [2, 2]]))
        assert_type(line, LineModelND | FailedEstimation)
        assert isinstance(line, LineModelND)

        failure = CircleModel.from_estimate(np.ones((3, 2)))
        assert isinstance(failure, FailedEstimation)
        assert_type(bool(failure), bool)
        assert not failure
        assert failure.message
        assert failure.error_cls is FailedEstimationAccessError

    def test_transform_from_estimate() -> None:
        src = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [2, 0], [2, 1], [0, 2], [1, 2]], dtype=float)
        affine = AffineTransform.from_estimate(src=src, dst=src, weights=np.ones(len(src)))
        assert_type(affine, AffineTransform | FailedEstimation)
        assert isinstance(affine, AffineTransform)
        similarity = SimilarityTransform.from_estimate(src=src, dst=src)
        assert_type(similarity, SimilarityTransform | FailedEstimation)
        assert isinstance(similarity, SimilarityTransform)
        assert isinstance(ProjectiveTransform.from_estimate(src, src), ProjectiveTransform)
        assert isinstance(EuclideanTransform.from_estimate(src, src), EuclideanTransform)
        assert isinstance(PiecewiseAffineTransform.from_estimate(src, src), PiecewiseAffineTransform)
        assert isinstance(PolynomialTransform.from_estimate(src, src), PolynomialTransform)
        assert isinstance(EssentialMatrixTransform.from_estimate(src, src), EssentialMatrixTransform)
        assert isinstance(FundamentalMatrixTransform.from_estimate(src, src), FundamentalMatrixTransform)
        assert_type(AffineTransform.identity(), AffineTransform)
        assert_type(SimilarityTransform.identity(), SimilarityTransform)
        assert_type(PolynomialTransform.identity(), PolynomialTransform)
