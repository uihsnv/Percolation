#!/usr/bin/env python3
"""
Percolation
"""

from random import choices
import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 200
P = 0.3

LATTICE = choices(POOL, weights=[P, 1-P], k=(SIZE**2))

plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
plt.show()
