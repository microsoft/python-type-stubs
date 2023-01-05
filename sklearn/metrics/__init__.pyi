from ._ranking import auc as auc
from ._ranking import average_precision_score as average_precision_score
from ._ranking import coverage_error as coverage_error
from ._ranking import det_curve as det_curve
from ._ranking import dcg_score as dcg_score
from ._ranking import (
    label_ranking_average_precision_score as label_ranking_average_precision_score,
)
from ._ranking import label_ranking_loss as label_ranking_loss
from ._ranking import ndcg_score as ndcg_score
from ._ranking import precision_recall_curve as precision_recall_curve
from ._ranking import roc_auc_score as roc_auc_score
from ._ranking import roc_curve as roc_curve
from ._ranking import top_k_accuracy_score as top_k_accuracy_score

from ._classification import accuracy_score as accuracy_score
from ._classification import balanced_accuracy_score as balanced_accuracy_score
from ._classification import classification_report as classification_report
from ._classification import cohen_kappa_score as cohen_kappa_score
from ._classification import confusion_matrix as confusion_matrix
from ._classification import f1_score as f1_score
from ._classification import fbeta_score as fbeta_score
from ._classification import hamming_loss as hamming_loss
from ._classification import hinge_loss as hinge_loss
from ._classification import jaccard_score as jaccard_score
from ._classification import log_loss as log_loss
from ._classification import matthews_corrcoef as matthews_corrcoef
from ._classification import (
    precision_recall_fscore_support as precision_recall_fscore_support,
)
from ._classification import precision_score as precision_score
from ._classification import recall_score as recall_score
from ._classification import zero_one_loss as zero_one_loss
from ._classification import brier_score_loss as brier_score_loss
from ._classification import multilabel_confusion_matrix as multilabel_confusion_matrix

from ._dist_metrics import DistanceMetric as DistanceMetric

from . import cluster as cluster
from .cluster import adjusted_mutual_info_score as adjusted_mutual_info_score
from .cluster import adjusted_rand_score as adjusted_rand_score
from .cluster import rand_score as rand_score
from .cluster import pair_confusion_matrix as pair_confusion_matrix
from .cluster import completeness_score as completeness_score
from .cluster import consensus_score as consensus_score
from .cluster import (
    homogeneity_completeness_v_measure as homogeneity_completeness_v_measure,
)
from .cluster import homogeneity_score as homogeneity_score
from .cluster import mutual_info_score as mutual_info_score
from .cluster import normalized_mutual_info_score as normalized_mutual_info_score
from .cluster import fowlkes_mallows_score as fowlkes_mallows_score
from .cluster import silhouette_samples as silhouette_samples
from .cluster import silhouette_score as silhouette_score
from .cluster import calinski_harabasz_score as calinski_harabasz_score
from .cluster import v_measure_score as v_measure_score
from .cluster import davies_bouldin_score as davies_bouldin_score

from .pairwise import euclidean_distances as euclidean_distances
from .pairwise import nan_euclidean_distances as nan_euclidean_distances
from .pairwise import pairwise_distances as pairwise_distances
from .pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from .pairwise import pairwise_distances_argmin_min as pairwise_distances_argmin_min
from .pairwise import pairwise_kernels as pairwise_kernels
from .pairwise import pairwise_distances_chunked as pairwise_distances_chunked

from ._regression import explained_variance_score as explained_variance_score
from ._regression import max_error as max_error
from ._regression import mean_absolute_error as mean_absolute_error
from ._regression import mean_squared_error as mean_squared_error
from ._regression import mean_squared_log_error as mean_squared_log_error
from ._regression import median_absolute_error as median_absolute_error
from ._regression import (
    mean_absolute_percentage_error as mean_absolute_percentage_error,
)
from ._regression import mean_pinball_loss as mean_pinball_loss
from ._regression import r2_score as r2_score
from ._regression import mean_tweedie_deviance as mean_tweedie_deviance
from ._regression import mean_poisson_deviance as mean_poisson_deviance
from ._regression import mean_gamma_deviance as mean_gamma_deviance
from ._regression import d2_tweedie_score as d2_tweedie_score
from ._regression import d2_pinball_score as d2_pinball_score
from ._regression import d2_absolute_error_score as d2_absolute_error_score

from ._scorer import check_scoring as check_scoring
from ._scorer import make_scorer as make_scorer
from ._scorer import SCORERS as SCORERS
from ._scorer import get_scorer as get_scorer
from ._scorer import get_scorer_names as get_scorer_names

from ._plot.det_curve import plot_det_curve as plot_det_curve
from ._plot.det_curve import DetCurveDisplay as DetCurveDisplay
from ._plot.roc_curve import plot_roc_curve as plot_roc_curve
from ._plot.roc_curve import RocCurveDisplay as RocCurveDisplay
from ._plot.precision_recall_curve import (
    plot_precision_recall_curve as plot_precision_recall_curve,
)
from ._plot.precision_recall_curve import (
    PrecisionRecallDisplay as PrecisionRecallDisplay,
)

from ._plot.confusion_matrix import plot_confusion_matrix as plot_confusion_matrix
from ._plot.confusion_matrix import ConfusionMatrixDisplay as ConfusionMatrixDisplay

__all__ = [
    "accuracy_score",
    "adjusted_mutual_info_score",
    "adjusted_rand_score",
    "auc",
    "average_precision_score",
    "balanced_accuracy_score",
    "calinski_harabasz_score",
    "check_scoring",
    "classification_report",
    "cluster",
    "cohen_kappa_score",
    "completeness_score",
    "ConfusionMatrixDisplay",
    "confusion_matrix",
    "consensus_score",
    "coverage_error",
    "d2_tweedie_score",
    "d2_absolute_error_score",
    "d2_pinball_score",
    "dcg_score",
    "davies_bouldin_score",
    "DetCurveDisplay",
    "det_curve",
    "DistanceMetric",
    "euclidean_distances",
    "explained_variance_score",
    "f1_score",
    "fbeta_score",
    "fowlkes_mallows_score",
    "get_scorer",
    "hamming_loss",
    "hinge_loss",
    "homogeneity_completeness_v_measure",
    "homogeneity_score",
    "jaccard_score",
    "label_ranking_average_precision_score",
    "label_ranking_loss",
    "log_loss",
    "make_scorer",
    "nan_euclidean_distances",
    "matthews_corrcoef",
    "max_error",
    "mean_absolute_error",
    "mean_squared_error",
    "mean_squared_log_error",
    "mean_pinball_loss",
    "mean_poisson_deviance",
    "mean_gamma_deviance",
    "mean_tweedie_deviance",
    "median_absolute_error",
    "mean_absolute_percentage_error",
    "multilabel_confusion_matrix",
    "mutual_info_score",
    "ndcg_score",
    "normalized_mutual_info_score",
    "pair_confusion_matrix",
    "pairwise_distances",
    "pairwise_distances_argmin",
    "pairwise_distances_argmin_min",
    "pairwise_distances_chunked",
    "pairwise_kernels",
    "plot_confusion_matrix",
    "plot_det_curve",
    "plot_precision_recall_curve",
    "plot_roc_curve",
    "PrecisionRecallDisplay",
    "precision_recall_curve",
    "precision_recall_fscore_support",
    "precision_score",
    "r2_score",
    "rand_score",
    "recall_score",
    "RocCurveDisplay",
    "roc_auc_score",
    "roc_curve",
    "SCORERS",
    "get_scorer_names",
    "silhouette_samples",
    "silhouette_score",
    "top_k_accuracy_score",
    "v_measure_score",
    "zero_one_loss",
    "brier_score_loss",
]
