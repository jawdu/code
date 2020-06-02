#! /usr/bin/python3

# do a 3 body problem
# after this, do a js one but with some stupid images as the 3 bodies

import matplotlib.pyplot as mpl
import numpy as np
from inDU import inputDeck
from inDU import inputUser

#G = 6.6741 * (10**-11)
#dt = 0.001    # timestep

# get inputs

if input("y to use defaults, any other key to input new: ") == "y":
    rx, ry, vx, vy, m = inputDeck()

else:
    rx, ry, vx, vy, m = inputUser()






# plot initial positions

mpl.plot(rx[0], ry[0], 'bo', rx[1], ry[1], 'ro', rx[2], ry[2], 'go')
mpl.show()









