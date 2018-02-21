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
P = 0.3
IM = plt.imshow(np.reshape(choices(POOL, weights=[P, 1-P], k=(SIZE**2)), (SIZE, SIZE)))

AXP = plt.axes([0.25, 0.1, 0.65, 0.03])
P = Slider(AXP, 'p', 0.0, 1.0, valinit=0)

def update():
    """
    lattice with the new 'p'
    """
    plt.imshow(np.reshape(choices(POOL, weights=[P.val, 1-(P.val)], k=(SIZE**2)), (SIZE, SIZE)))

P.on_changed(update)

plt.show()
