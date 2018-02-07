#!/usr/bin/env python3
"""
Percolation
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from random import choices

POOL = np.array([True, False])

SIZE = 200
P = 0.3
im = plt.imshow(np.reshape(choices(POOL, weights=[P, 1-P], k=(SIZE**2)), (SIZE, SIZE)))

AXP = plt.axes([0.25, 0.1, 0.65, 0.03])
P = Slider(AXP, 'p', 0.0, 1.0, valinit=0)

def update():
    plt.imshow(np.reshape(choices(POOL, weights=[P.val, 1-(P.val)], k=(SIZE**2)), (SIZE, SIZE)))

p.on_changed(update)

plt.show()
