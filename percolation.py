#!/usr/bin/env python3
"""
Percolation
"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 100
P = 0.41

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.imshow(np.reshape(np.random.choice(POOL, SIZE**2, True, [P, 1-P]), (SIZE, SIZE)))
plt.show()
