#!/usr/bin/env python3
"""
Percolation
"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 100
P = 0.41
fig,ax = plt.subplots(figsize=(12,12))
ax.imshow(np.reshape(np.random.choice(POOL, SIZE**2, True, [P, 1-P]), (SIZE, SIZE)))
plt.show()
