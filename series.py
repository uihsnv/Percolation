#!/usr/bin/env python3
"""
PERCOLATION
A series of lattices with sites added/removed, over a range of 'p'

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

from sys import exit as sys_exit
from matplotlib.pyplot import get_current_fig_manager, imshow, title, pause
from numpy import array, linspace, reshape, nditer, where, logical_not
from numpy.random import choice

POOL = array([True, False])

SIZE = 50
STEPS = 25
P_INIT = 1
P_FINAL = 0

# initial percolation lattice
LATTICE = choice(POOL, SIZE**2, True, [P_INIT, 1-P_INIT])

# list of 'p' values to sample/plot/scan-across
P = linspace(P_INIT, P_FINAL, num=STEPS, endpoint=True)

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
    sys_exit("Error: Check initial and final 'p's")

# to maximise the display
FIGMANAGER = get_current_fig_manager()
FIGMANAGER.full_screen_toggle()

# string to display the p value along with the image
title(f"Percolation on a square lattice : p = {P_INIT:.2f}", fontsize='xx-large')
imshow(reshape(LATTICE, (SIZE, SIZE)), cmap=None, vmin=0, vmax=1)
pause(0.5)

# construct an iterator over the empty-site flip-fraction array
IT = nditer(X, flags=['c_index'])
for fraction in IT:

    if CASE:
        for i in nditer(where(logical_not(LATTICE))):
            LATTICE[i] = choice(POOL, replace=True, p=[fraction, 1-fraction])
    else:
        for i in nditer(where(LATTICE)):
            LATTICE[i] = choice(POOL, replace=True, p=[1-fraction, fraction])

    title(f"Percolation on a square lattice : p = {P[IT.index + 1]:.2f}", fontsize='xx-large')
    imshow(reshape(LATTICE, (SIZE, SIZE)), cmap=None, vmin=0, vmax=1)
    pause(1)
