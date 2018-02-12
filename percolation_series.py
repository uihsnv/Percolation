#!/usr/bin/env python3
"""
PERCOLATION
A series of lattices with sites added/removed, over a range of 'p'
"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 50
PEAS = 20
P_INIT = 1
P_FINAL = 0

# list of 'p' values to sample/plot/scan-across
P = np.linspace(P_INIT, P_FINAL, num=PEAS, endpoint=False)

# Say we need to go from a lattice of p -> p'
if 0 <= P_INIT < P_FINAL <= 1:
    CASE = True
    # fraction of empty sites to flip = (p' - p)/(1 - p)
    X = (P[1:] - P[:-1])/(1 - P[:-1])
elif 1 >= P_INIT > P_FINAL >= 0:
    CASE = False
    # fraction of filled sites to flip = (p - p')/(p)
    X = (P[:-1] - P[1:])/P[:-1]
else:
    raise ValueError("Check initial and final 'p's")

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

    if CASE:
        for i in np.nditer(np.where(np.logical_not(LATTICE))):
            LATTICE[i] = np.random.choice(POOL, replace=True, p=[fraction, 1-fraction])
    else:
        for i in np.nditer(np.where(LATTICE)):
            LATTICE[i] = np.random.choice(POOL, replace=True, p=[1-fraction, fraction])

    PEA = str(round(P[IT.index + 1], 2))
    plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
    plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
    plt.draw()
    plt.pause(1)
