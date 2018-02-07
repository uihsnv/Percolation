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
im = plt.imshow(np.reshape(choices(pool, weights=[p,1-p], k=size**2), (size,size)))

axp = plt.axes([0.25, 0.1, 0.65, 0.03])
p = Slider(axp, 'p', 0.0, 1.0, valinit=0)

def update(val):
    plt.imshow(np.reshape(choices(pool, weights=[p.val,1-(p.val)], k=size**2), (size,size)))

p.on_changed(update)

plt.show()
