#!/usr/bin/env python3
"""
Percolation
Finding the infinite cluster, and isolating the finte ones too.

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

from matplotlib.pyplot import get_current_fig_manager, title, imshow, pause
from numpy import array, reshape
from numpy.random import choice

POOL = array([True, False])

SIZE = 100
P = 0.7

PERK = reshape(choice(POOL, SIZE**2, True, [P, 1-P]), (SIZE, SIZE))

CLUSTERS = []

for i in range(SIZE):
    PERK[i]

FIGMANAGER = get_current_fig_manager()
FIGMANAGER.full_screen_toggle()

title(f"Percolation on a square lattice : p = {P:.3f}", fontsize='xx-large')
imshow(PERK)
pause(1)
