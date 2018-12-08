#!/usr/bin/env python3
"""
Percolation

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
from matplotlib.widgets import Slider
from numpy import array, count_nonzero, reshape, nditer, where, logical_not
from numpy.random import choice

POOL = array([True, False])

SIZE = 50
SIZE2 = SIZE**2
P_INIT = 0.3

# initial percolation lattice
LATTICE = choice(POOL, SIZE2, True, [P_INIT, 1-P_INIT])

def update(val):
    """
    lattice with the new 'p'
    """

    pea = count_nonzero(LATTICE)/SIZE2

    if val > pea:
        fraction = (val - pea)/(1 - pea)
        for i in nditer(where(logical_not(LATTICE))):
            LATTICE[i] = choice(POOL, replace=True, p=[fraction, 1-fraction])
    elif pea > val:
        fraction = (pea - val)/pea
        for i in nditer(where(LATTICE)):
            LATTICE[i] = choice(POOL, replace=True, p=[1-fraction, fraction])

    plt.suptitle(f"Percolation on a square lattice : p = {val:.3f}", y=0.95, fontsize='xx-large')
    IM.set_data(reshape(LATTICE, (SIZE, SIZE)))
    plt.draw()

plt.suptitle(f"Percolation on a square lattice : p = {P_INIT:.3f}", y=0.95, fontsize='xx-large')
IM = plt.imshow(reshape(LATTICE, (SIZE, SIZE)), cmap=None, vmin=0, vmax=1)

AXSL = plt.axes([0.2, 0.05, 0.65, 0.03])
PSL = Slider(AXSL, 'p', 0.0, 1.0, valinit=P_INIT)

PSL.on_changed(update)

FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()
plt.show()
