import numpy as np
from typing import Callable, Literal, Sequence
from ._typing import *

def window_hanning(x):
    """
    Return *x* times the Hanning (or Hann) window of len(*x*).

    See Also
    --------
    window_none : Another window algorithm.
    """
    ...

def window_none(x):
    """
    No window function; simply return *x*.

    See Also
    --------
    window_hanning : Another window algorithm.
    """
    ...

def detrend(
    x: Sequence,
    key: Literal["default", "constant", "mean", "linear", "none"] | Callable = ...,
    axis: int = ...,
) -> Sequence:
    """
    Return *x* with its trend removed.

    Parameters
    ----------
    x : array or sequence
        Array or sequence containing the data.

    key : {'default', 'constant', 'mean', 'linear', 'none'} or function
        The detrending algorithm to use. 'default', 'mean', and 'constant' are
        the same as `detrend_mean`. 'linear' is the same as `detrend_linear`.
        'none' is the same as `detrend_none`. The default is 'mean'. See the
        corresponding functions for more details regarding the algorithms. Can
        also be a function that carries out the detrend operation.

    axis : int
        The axis along which to do the detrending.

    See Also
    --------
    detrend_mean : Implementation of the 'mean' algorithm.
    detrend_linear : Implementation of the 'linear' algorithm.
    detrend_none : Implementation of the 'none' algorithm.
    """
    ...

def detrend_mean(x: Sequence, axis: int = ...) -> Sequence:
    """
    Return *x* minus the mean(*x*).

    Parameters
    ----------
    x : array or sequence
        Array or sequence containing the data
        Can have any dimensionality

    axis : int
        The axis along which to take the mean.  See `numpy.mean` for a
        description of this argument.

    See Also
    --------
    detrend_linear : Another detrend algorithm.
    detrend_none : Another detrend algorithm.
    detrend : A wrapper around all the detrend algorithms.
    """
    ...

def detrend_none(x, axis: int = ...):
    """
    Return *x*: no detrending.

    Parameters
    ----------
    x : any object
        An object containing the data

    axis : int
        This parameter is ignored.
        It is included for compatibility with detrend_mean

    See Also
    --------
    detrend_mean : Another detrend algorithm.
    detrend_linear : Another detrend algorithm.
    detrend : A wrapper around all the detrend algorithms.
    """
    ...

def detrend_linear(y: Sequence) -> Sequence:
    """
    Return *x* minus best fit line; 'linear' detrending.

    Parameters
    ----------
    y : 0-D or 1-D array or sequence
        Array or sequence containing the data

    See Also
    --------
    detrend_mean : Another detrend algorithm.
    detrend_none : Another detrend algorithm.
    detrend : A wrapper around all the detrend algorithms.
    """
    ...

def stride_windows(x: Sequence, n: int, noverlap: int = ..., axis: int = ...):
    """
    Get all windows of *x* with length *n* as a single array,
    using strides to avoid data duplication.

    .. warning::

        It is not safe to write to the output array.  Multiple
        elements may point to the same piece of memory,
        so modifying one value may change others.

    Parameters
    ----------
    x : 1D array or sequence
        Array or sequence containing the data.
    n : int
        The number of data points in each window.
    noverlap : int, default: 0 (no overlap)
        The overlap between adjacent windows.
    axis : int
        The axis along which the windows will run.

    References
    ----------
    `stackoverflow: Rolling window for 1D arrays in Numpy?
    <https://stackoverflow.com/a/6811241>`_
    `stackoverflow: Using strides for an efficient moving average filter
    <https://stackoverflow.com/a/4947453>`_
    """
    ...

def psd(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]:
    r"""
    Compute the power spectral density.

    The power spectral density :math:`P_{xx}` by Welch's average
    periodogram method.  The vector *x* is divided into *NFFT* length
    segments.  Each segment is detrended by function *detrend* and
    windowed by function *window*.  *noverlap* gives the length of
    the overlap between segments.  The :math:`|\mathrm{fft}(i)|^2`
    of each segment :math:`i` are averaged to compute :math:`P_{xx}`.

    If len(*x*) < *NFFT*, it will be zero padded to *NFFT*.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Pxx : 1-D array
        The values for the power spectrum :math:`P_{xx}` (real valued)

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxx*

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John
    Wiley & Sons (1986)

    See Also
    --------
    specgram
        `specgram` differs in the default overlap; in not returning the mean of
        the segment periodograms; and in returning the times of the segments.

    magnitude_spectrum : returns the magnitude spectrum.

    csd : returns the spectral density between two signals.
    """
    ...

def csd(
    x: ArrayLike,
    y: ArrayLike,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute the cross-spectral density.

    The cross spectral density :math:`P_{xy}` by Welch's average
    periodogram method.  The vectors *x* and *y* are divided into
    *NFFT* length segments.  Each segment is detrended by function
    *detrend* and windowed by function *window*.  *noverlap* gives
    the length of the overlap between segments.  The product of
    the direct FFTs of *x* and *y* are averaged over each segment
    to compute :math:`P_{xy}`, with a scaling to correct for power
    loss due to windowing.

    If len(*x*) < *NFFT* or len(*y*) < *NFFT*, they will be zero
    padded to *NFFT*.

    Parameters
    ----------
    x, y : 1-D arrays or sequences
        Arrays or sequences containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Pxy : 1-D array
        The values for the cross spectrum :math:`P_{xy}` before scaling (real
        valued)

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxy*

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John
    Wiley & Sons (1986)

    See Also
    --------
    psd : equivalent to setting ``y = x``.
    """
    ...

complex_spectrum = ...
magnitude_spectrum = ...
angle_spectrum = ...
phase_spectrum = ...

def specgram(
    x: ArrayLike,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    mode: str = ...,
) -> tuple[ArrayLike, ArrayLike, ArrayLike]:
    """
    Compute a spectrogram.

    Compute and plot a spectrogram of data in *x*.  Data are split into
    *NFFT* length segments and the spectrum of each section is
    computed.  The windowing function *window* is applied to each
    segment, and the amount of overlap of each segment is
    specified with *noverlap*.

    Parameters
    ----------
    x : array-like
        1-D array or sequence.

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 128
        The number of points of overlap between blocks.
    mode : str, default: 'psd'
        What sort of spectrum to use:
            'psd'
                Returns the power spectral density.
            'complex'
                Returns the complex-valued frequency spectrum.
            'magnitude'
                Returns the magnitude spectrum.
            'angle'
                Returns the phase spectrum without unwrapping.
            'phase'
                Returns the phase spectrum with unwrapping.

    Returns
    -------
    spectrum : array-like
        2D array, columns are the periodograms of successive segments.

    freqs : array-like
        1-D array, frequencies corresponding to the rows in *spectrum*.

    t : array-like
        1-D array, the times corresponding to midpoints of segments
        (i.e the columns in *spectrum*).

    See Also
    --------
    psd : differs in the overlap and in the return values.
    complex_spectrum : similar, but with complex valued frequencies.
    magnitude_spectrum : similar single segment when *mode* is 'magnitude'.
    angle_spectrum : similar to single segment when *mode* is 'angle'.
    phase_spectrum : similar to single segment when *mode* is 'phase'.

    Notes
    -----
    *detrend* and *scale_by_freq* only apply when *mode* is set to 'psd'.

    """
    ...

def cohere(
    x,
    y,
    NFFT: int = ...,
    Fs: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = 0,
    pad_to: int = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
) -> tuple[np.ndarray, np.ndarray]:
    r"""
    The coherence between *x* and *y*.  Coherence is the normalized
    cross spectral density:

    .. math::

        C_{xy} = \frac{|P_{xy}|^2}{P_{xx}P_{yy}}

    Parameters
    ----------
    x, y
        Array or sequence containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Cxy : 1-D array
        The coherence vector.
    freqs : 1-D array
            The frequencies for the elements in *Cxy*.

    See Also
    --------
    :func:`psd`, :func:`csd` :
        For information about the methods used to compute :math:`P_{xy}`,
        :math:`P_{xx}` and :math:`P_{yy}`.
    """
    ...

class GaussianKDE:
    """
    Representation of a kernel-density estimate using Gaussian kernels.

    Parameters
    ----------
    dataset : array-like
        Datapoints to estimate from. In case of univariate data this is a 1-D
        array, otherwise a 2D array with shape (# of dims, # of data).
    bw_method : str, scalar or callable, optional
        The method used to calculate the estimator bandwidth.  This can be
        'scott', 'silverman', a scalar constant or a callable.  If a
        scalar, this will be used directly as `kde.factor`.  If a
        callable, it should take a `GaussianKDE` instance as only
        parameter and return a scalar. If None (default), 'scott' is used.

    Attributes
    ----------
    dataset : np.ndarray
        The dataset passed to the constructor.
    dim : int
        Number of dimensions.
    num_dp : int
        Number of datapoints.
    factor : float
        The bandwidth factor, obtained from `kde.covariance_factor`, with which
        the covariance matrix is multiplied.
    covariance : np.ndarray
        The covariance matrix of *dataset*, scaled by the calculated bandwidth
        (`kde.factor`).
    inv_cov : np.ndarray
        The inverse of *covariance*.

    Methods
    -------
    kde.evaluate(points) : np.ndarray
        Evaluate the estimated pdf on a provided set of points.
    kde(points) : np.ndarray
        Same as kde.evaluate(points)
    """

    def __init__(
        self, dataset: ArrayLike, bw_method: str | Scalar | Callable = ...
    ) -> None: ...
    def scotts_factor(self): ...
    def silverman_factor(self): ...

    covariance_factor = ...
    def evaluate(self, points) -> np.ndarray:
        """
        Evaluate the estimated pdf on a set of points.

        Parameters
        ----------
        points : (# of dimensions, # of points)-array
            Alternatively, a (# of dimensions,) vector can be passed in and
            treated as a single point.

        Returns
        -------
        (# of points,)-array
            The values at each point.

        Raises
        ------
        ValueError : if the dimensionality of the input points is different
                     than the dimensionality of the KDE.

        """
        ...
