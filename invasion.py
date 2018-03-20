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
STEPS = 100
PAUSE_TIME = 0.0001
"""
Initialisation type:
    0 -> Single point, centre of lattice
    1 -> Line spanning a lattice side, edge of lattice
"""
INIT_TYPE = 1

def update_boundary(loc_x, loc_y):
    """
    Positions of neighbours of a site, not yet wet
    """

    # List of all neighbours, with periodic boundaries
    neighbours = [(loc_x, ((loc_y - 1) % SIZE)), (loc_x, ((loc_y + 1) % SIZE)),
                  (((loc_x - 1) % SIZE), loc_y), (((loc_x + 1) % SIZE), loc_y)]

    # List of those neighbours that aren't already wet
    unwet_neighbours = [position for position in neighbours if not LATTICE[position]]

    for pos in unwet_neighbours:
        BOUNDARY[pos] = WEIGHTS[pos]

def invade():
    """
    Perform a wetting invasion
    """
    # The location of the site on the boundary with the smallest weight
    wetted = min(BOUNDARY, key=BOUNDARY.get)

    # Remove said site from the dictionary of boundary values
    del BOUNDARY[wetted]

    LATTICE[wetted] = True
    AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)
    #plt.xticks(np.arange(0, 1, 0.05))
    #plt.hist(BOUNDARY.values(), bins=50, range=(0, 1))
    plt.pause(PAUSE_TIME)
    plt.cla()

    # Indicates if wetness hits the boundary
    #if any(coord in [wetted[0], wetted[1]] for coord in [0, SIZE-1]):
    #    GAM = str(i)
    #    print("Hit lattice edge at "+GAM)
    #    print(wetted)
        #break

    update_boundary(wetted[0], wetted[1])

# Initialise figure
FIG = plt.figure()
AX = plt.axes()
# to maximise the display
FIGMANAGER = plt.get_current_fig_manager()
FIGMANAGER.window.showMaximized()

# Convert numbers to strings, for use in the title
ALF = str(SIZE)
BET = str(STEPS)

# The un-wet lattice
LATTICE = np.full((SIZE, SIZE), False)
# Random number weights of each site indicating magnitude of the obstacle
WEIGHTS = np.random.rand(SIZE, SIZE)
# A 'dictionary' of the location and weights of boundary sites
BOUNDARY = {}

# Choice of initial wetting
if INIT_TYPE == 0:
    FIG.suptitle("Invasion Percolation from a point, run for "+BET+" steps",
                 fontsize='xx-large')
    CENTRE = (SIZE // 2) + 1
    LATTICE[CENTRE, CENTRE] = True
    update_boundary(CENTRE, CENTRE)
elif INIT_TYPE == 1:
    FIG.suptitle("Invasion Percolation from a line, run for "+BET+" steps",
                 fontsize='xx-large')
    for j in range(SIZE):
        LATTICE[0, j] = True
        BOUNDARY[(1, j)] = WEIGHTS[1, j]
        BOUNDARY[(SIZE-1, j)] = WEIGHTS[SIZE-1, j]

AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)
plt.pause(PAUSE_TIME)
plt.cla()


for i in range(STEPS):
    invade()

# to maximise the display
#FIGMANAGER = plt.get_current_fig_manager()
#FIGMANAGER.window.showMaximized()

AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)
#plt.xticks(np.arange(0, 1, 0.03))
#plt.hist(BOUNDARY.values(), bins=100, range=(0, 1))
plt.show()
