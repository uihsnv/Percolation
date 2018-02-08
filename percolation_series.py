#!/usr/bin/env python3
"""
Percolation
"""

from time import sleep
from random import choices
import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 50
PEAS = 20

COUNT = 0
P = np.linspace(0.5, 0.7, num=PEAS, endpoint=True)
# (p' - p)/(1 - p)
X = (P[1:] - P[:-1])/(1 - P[:-1])

#LATTICE = np.full((SIZE**2), False, dtype=bool)
LATTICE = choices(POOL, weights=[0.5, 0.5], k=(SIZE**2))

PEA = str(round(P[COUNT],2))
plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
plt.pause(0.5)

for fraction in np.nditer(X):

    COUNT = COUNT + 1
    for i in np.nditer(np.where(np.logical_not(LATTICE))):
        LATTICE[i] = choices(POOL, weights=[fraction, 1-fraction], k=1)[0]

    PEA = str(round(P[COUNT],2))
    plt.title("Percolation on a square lattice : p = "+PEA, fontsize='xx-large')
    plt.imshow(np.reshape(LATTICE, (SIZE, SIZE)))
    plt.draw()
    plt.pause(1)
