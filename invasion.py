#!/usr/bin/env python3
"""
Invasion Percolation

Self-organised percolating criticality from the distribution of the weights of
the boundary due to a minimum-weight invasion process

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

np.random.seed(7278)
SIZE = 101
STEPS = 700
PAUSE_TIME = 0.001

# to maximise the display
FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()

LATTICE = np.full((SIZE, SIZE), False)
plt.imshow(LATTICE, cmap=None, vmin=0, vmax=1)
plt.pause(PAUSE_TIME)
plt.clf()
# Random number weights of each site indicating magnitude of the obstacle
WEIGHTS = np.random.rand(SIZE, SIZE)
# A 'dictionary' of the location and weights of boundary sites
BOUNDARY = {}

CENTRE = (SIZE // 2) + 1
LATTICE[CENTRE, CENTRE] = True
plt.imshow(LATTICE, cmap=None, vmin=0, vmax=1)
plt.pause(PAUSE_TIME)
plt.clf()

def update_boundary(loc_x, loc_y):
    """
    Positions of neighbours of a site, not yet wet
    """

    neighbours = [(loc_x, loc_y-1), (loc_x, loc_y+1), (loc_x-1, loc_y), (loc_x+1, loc_y)]

    unwet_neighbours = [position for position in neighbours if not LATTICE[position]]

    for pos in unwet_neighbours:
        BOUNDARY[pos] = WEIGHTS[pos]


update_boundary(CENTRE, CENTRE)

for i in range(STEPS):
    # The location of the site on the boundary with the smallest weight
    wetted = min(BOUNDARY, key=BOUNDARY.get)

    # Remove said site from the dictionary of boundary values
    del BOUNDARY[wetted]

    LATTICE[wetted] = True
    plt.imshow(LATTICE, cmap=None, vmin=0, vmax=1)
    plt.pause(PAUSE_TIME)
    plt.clf()

    update_boundary(wetted[0], wetted[1])

#plt.imshow(LATTICE, cmap=None, vmin=0, vmax=1)
#plt.pause(10)
#print(BOUNDARY.values())
