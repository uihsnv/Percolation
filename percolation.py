#!/usr/bin/env python3
"""
Percolation
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from random import choices

pool = np.array([True, False])

size = 200
p= 0.3

lattice = choices(pool, weights=[p,1-p], k=size**2), (size,size)

plt.imshow(np.reshape(lattice))
plt.show()
