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
from matplotlib import animation
import numpy as np

np.random.seed(7278)
SIZE = 101
STEPS = 500
INTERVAL = 20
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
    plt.cla()
    IMG.append([AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)])
    #IMG.append([AX.hist(BOUNDARY.values(), bins=50, range=(0, 1))])

    # Indicator for when the wetness hits a boundary
    #if any(coord in [wetted[0], wetted[1]] for coord in [0, SIZE-1]):
    #    GAM = str(i)
    #    print("Hit lattice edge at "+GAM)
    #    print(wetted)
        #break

    update_boundary(wetted[0], wetted[1])


# The un-wet lattice
LATTICE = np.full((SIZE, SIZE), False)
# Random number weights of each site indicating magnitude of the obstacle
WEIGHTS = np.random.rand(SIZE, SIZE)
# A 'dictionary' of the location and weights of boundary sites
BOUNDARY = {}

# Initialise figure
FIG = plt.figure(figsize=(19.2, 10.8))
AX = plt.axes()

# Choice of initial wetting
if INIT_TYPE == 0:
    FIG.suptitle(f"Invasion Percolation from a point, run for {STEPS} steps",
                 fontsize='xx-large')
    CENTRE = (SIZE // 2) + 1
    LATTICE[CENTRE, CENTRE] = True
    update_boundary(CENTRE, CENTRE)
elif INIT_TYPE == 1:
    FIG.suptitle(f"Invasion Percolation from a line, run for {STEPS} steps",
                 fontsize='xx-large')
    for j in range(SIZE):
        LATTICE[0, j] = True
        BOUNDARY[(1, j)] = WEIGHTS[1, j]
        BOUNDARY[(SIZE-1, j)] = WEIGHTS[SIZE-1, j]


# Initialise an empty list to store the images
IMG = []

# First image of the lattice with the initial condition wetness
IMG.append([AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)])
#AX.xticks(np.arange(0, 1, 0.05))
#IMG.append([AX.hist(BOUNDARY.values(), bins=50, range=(0, 1))])

for _ in range(STEPS):
    invade()

## To plot an image, instead of the animation, uncomment this,
## and comment-out all lines with 'IMG' and 'ANIM'
#AX.matshow(LATTICE, cmap=None, vmin=0, vmax=1)
#FIG.savefig("line_invasion.png", dpi=300, transparent=True, bbox_inches='tight')

ANIM = animation.ArtistAnimation(FIG, IMG, interval=INTERVAL, blit=True)

## Comment-out the 'plt.cla()' in line 66 if you want to save to a file
#ANIM.save('Figures/invasion-percolation_point.gif', writer='imagemagick', fps=30, dpi=45,
#ANIM.save('invasion-percolation_point.mp4', extra_args=['-vcodec libx264'],
#          metadata=dict(title=FIG._suptitle.get_text(), artist='Vishnu V. Krishnan',
#                        subject='Statistical Physics', copyright='CC BY-SA 4.0'))

plt.show()
