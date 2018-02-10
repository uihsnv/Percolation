#!/usr/bin/env python3
"""
Percolation
"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 50
PEAS = 20
P_INIT = 0
P_FINAL = 1

# list of 'p' values to sample/plot/scan-across
P = np.linspace(P_INIT, P_FINAL, num=PEAS, endpoint=False)

# fraction of empty sites to flip = (p' - p)/(1 - p)
X = (P[1:] - P[:-1])/(1 - P[:-1])

# initial percolation lattice
LATTICE = np.random.choice(POOL, SIZE**2, True, [P_INIT, 1-P_INIT])

# to maximise the display
FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()

# string to display the p value along with the image
PEA = str(round(P_INIT, 2))
plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
plt.pause(0.5)

# construct an iterator over the empty-site flip-fraction array
IT = np.nditer(X, flags=['c_index'])
for fraction in IT:

    for i in np.nditer(np.where(np.logical_not(LATTICE))):
        LATTICE[i] = np.random.choice(POOL, SIZE**2, True, [fraction, 1-fraction])[0]

    PEA = str(round(P[IT.index + 1], 2))
    plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
    plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
    plt.draw()
    plt.pause(1)
