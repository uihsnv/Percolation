#!/usr/bin/env python3
"""
Percolation
Finding the infinite cluster,
and isolating the finte ones too.
"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 100
P = 0.7

FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()

PEA = str(round(P, 3))
plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
plt.imshow(np.reshape(np.random.choice(POOL, SIZE**2, True, [P, 1-P]), (SIZE, SIZE)))
plt.show()
