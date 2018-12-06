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

from random import choices
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

POOL = np.array([True, False])

SIZE = 200
P_INIT = 0.3

def update(val):
    """
    lattice with the new 'p'
    """
    plt.suptitle(f"Percolation on a square lattice : p = {val:.3f}", fontsize='xx-large')
    IM.set_data(np.reshape(choices(POOL, weights=[val, 1-val], k=(SIZE**2)), (SIZE, SIZE)))
    plt.draw()

plt.suptitle(f"Percolation on a square lattice : p = {P_INIT:.3f}", fontsize='xx-large')
IM = plt.imshow(np.reshape(choices(POOL, weights=[P_INIT, 1-P_INIT], k=(SIZE**2)), (SIZE, SIZE)),
                cmap=None, vmin=0, vmax=1)

AXSL = plt.axes([0.2, 0.05, 0.65, 0.03])
PSL = Slider(AXSL, 'p', 0.0, 1.0, valinit=P_INIT)

PSL.on_changed(update)

FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()
plt.show()
