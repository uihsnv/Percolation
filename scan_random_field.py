#!/usr/bin/env python3
"""
RANDOM FIELD
Scanning the random field of a percolation process, across values to find the
percolation threshold

    Copyright (C) 2018  Vishnu V. Krishnan : vishnugb@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import matplotlib.pyplot as plt
import numpy as np

POOL = np.array([True, False])

SIZE = 50
SCAN = 25
F_INIT = 0
F_FINAL = 1

# Random number weights of each site indicating magnitude of the obstacle
WEIGHTS = np.random.rand(SIZE, SIZE)
# The lattice of 0 weights
LATTICE = np.full((SIZE, SIZE), False)

# list of 'f' values to sample/plot/scan-across
F = np.linspace(F_INIT, F_FINAL, num=SCAN, endpoint=True)

# to maximise the display
FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()


for i in range(SCAN):

    for j in np.nditer(np.where((LATTICE > F[i]) & (LATTICE < F[i+1]))):
        LATTICE[j] = True

    WEIGHT = str(round(F[i], 2)) + ' - ' + str(round(F[i+1], 2))
    plt.title("Random Weights on a square lattice : "+WEIGHT, fontsize='xx-large')
    plt.imshow(LATTICE, cmap=None, vmin=0, vmax=1)
    plt.pause(1)
