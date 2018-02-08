#!/usr/bin/env python3
"""
Percolation
"""

from random import choices
import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 100
P = 0.41
fig,ax = plt.subplots(figsize=(12,12))
ax.imshow(np.reshape(choices(POOL, weights=[P, 1-P], k=(SIZE**2)), (SIZE, SIZE)),cmap=plt.cm.tab20b)
plt.show()
