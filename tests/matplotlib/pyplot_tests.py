from typing import Any, assert_type
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np

# Squeeze default value
fig, ax = plt.subplots(1)
assert_type(ax, Axes)

fig, ax = plt.subplots(1, 1)
assert_type(ax, Axes)

fig, axs = plt.subplots(2, 1)
assert_type(axs, np.ndarray)

fig, axs = plt.subplots(2, 2)
assert_type(axs, np.ndarray)

# Squeeze true
fig, ax = plt.subplots(1, squeeze=True)
assert_type(ax, Axes)

fig, ax = plt.subplots(1, 1, squeeze=True)
assert_type(ax, Axes)

fig, axs = plt.subplots(2, 1, squeeze=True)
assert_type(axs, np.ndarray)

fig, axs = plt.subplots(2, 2, squeeze=True)
assert_type(axs, np.ndarray)

# Squeeze false
fig, axs = plt.subplots(1, squeeze=False)
assert_type(axs, np.ndarray)

fig, axs = plt.subplots(1, 1, squeeze=False)
assert_type(axs, np.ndarray)

fig, axs = plt.subplots(2, 1, squeeze=False)
assert_type(axs, np.ndarray)

fig, axs = plt.subplots(2, 2, squeeze=False)
assert_type(axs, np.ndarray)