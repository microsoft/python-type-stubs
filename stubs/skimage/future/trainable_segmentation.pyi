from numpy.typing import NDArray

from ..feature import multiscale_basic_features

class TrainableSegmenter:
    def __init__(self, clf=None, features_func=None): ...
    def compute_features(self, image): ...
    def fit(self, image: NDArray, labels: NDArray): ...
    def predict(self, image: NDArray): ...

def fit_segmenter(labels: NDArray, features: NDArray, clf): ...
def predict_segmenter(features: NDArray, clf) -> NDArray: ...
