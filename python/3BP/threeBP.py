#! /usr/bin/python3

# do a 3 body problem
# after this, do a js one but with some stupid images as the 3 bodies

import matplotlib.pyplot as mpl
import numpy as np
from inDU import inputDeck
from inDU import inputUser

# get inputs

if input("y to use defaults, any other key to input new: ") == "y":
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, m1, m2, m3 = inputDeck()

else:
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, m1, m2, m3 = inputUser()






# plot initial positions

mpl.plot(x1, y1, 'bo', x2, y2, 'ro', x3, y3, 'go')
mpl.show()









