#! /usr/bin/python3

#https://codegolf.stackexchange.com/questions/35835/draw-random-black-and-white-forest

# some sort of branching i.e. fractal-ish
# furthest to nearest - so overwrite?
# 
# 800 x 600

# too dense, overwriting. further trees - less black . like pixels spaced.

# got pillow c.f. https://stackoverflow.com/questions/33484244/create-modify-and-save-an-image-in-python-3-x

# define leaf line then apply one pattern above, prob just gaussianish around horizon+150ish
# an array(x) with y values defining the transition pixel
# then algorithm for trunks & partial leaf
# do more like a hollowway - a path snaking to horizon. then fill in trees either side.

from PIL import Image
import time
import numpy as np
import math

fileout = "rForest-" + time.strftime("%H%M%S") + ".png" # timestamped filename so we can run many times
img = Image.new("RGB", (800,600), (255, 255, 255)) #initialise as white

# draw a horizon. s sin parameters, c cube parameters, softly randomised

s1 = 12 + np.random.uniform(-3, 3)
s2 = np.random.uniform(0, 3)

c1 = np.random.uniform(-0.00000006, 0.00000006)
c2 = np.random.uniform(-0.0000008, 0.00000008)
c3 = np.random.uniform(-0.002, 0.002) 

for i in range(800):
    p = 250 + int(s1 * (math.sin((6 * i / 800) + s2)) + (c1*(i**3) + c2*(i**2) + c3*i))

    img.putpixel((i, p), (0, 0, 0))

    #for j in range(2):
        #img.putpixel((i, 300+j), (0, 0, 0))



boundary = np.random.normal(150, 5, size=(1, 800)).astype(int)
# maybe add a gentle curve here, based on path

for i in range(800):
    for j in range(boundary[0,i]):
        # control density of canopy
        if (np.random.uniform(0, 1) < 0.25): img.putpixel((i, j), (0, 0, 0))



img.save(fileout, "PNG")


