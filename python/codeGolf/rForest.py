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

fileout = "Forest-" + time.strftime("%H%M%S") + ".png" # timestamped filename so we can run many times
img = Image.new("RGB", (800,600), (255, 255, 255)) #initialise as white
horizon = []

# draw a horizon. s sin parameters, c cube parameters, softly randomised

s1 = 12 + np.random.uniform(-3, 3)
s2 = np.random.uniform(0, 3)

c1 = np.random.uniform(-0.00000006, 0.00000006)
c2 = np.random.uniform(-0.0000008, 0.00000008)
c3 = np.random.uniform(-0.002, 0.002) 

for i in range(800):
    p = 250 + int(s1 * (math.sin((6 * i / 800) + s2)) + (c1*(i**3) + c2*(i**2) + c3*i))
    if (i % 2 == 0): 
        img.putpixel((i, p-1), (0, 0, 0))
    else:
        img.putpixel((i, p+1), (0, 0, 0))
    horizon.append(p)
# provisional, stil bit clean

# path: do a sin, but need to kinda log it? also to keep to about 2pi range. maybe solve for randomish start, end


pStart = 300

pEnd = 500


for i in range(0, horizon[pEnd]):
    img.putpixel((int(pStart + i * ((pEnd - pStart) / horizon[pEnd])), i), (0, 0, 0))


boundary = np.random.normal(150, 5, size=(1, 800))



# boundary parameters 
b1 = 16 + np.random.uniform(-3, 3)
b2 = 23 + np.random.uniform(-3, 3)
b3 = 360 + np.random.uniform(-20, 20)

for i in range(800):
    # melt boundary a little 
    if (i < pEnd):
        boundary[0, i] = boundary[0, i] + np.random.uniform(b1, b2)*math.exp((pEnd-i)/b3)
    else:
        boundary[0, i] = boundary[0, i] + np.random.uniform(b1, b2)*math.exp((i-pEnd)/b3)

boundary = boundary.astype(int)

# maybe add a gentle curve here, based on path

for i in range(800):
    for j in range(boundary[0,i]):
        # fill in canopy; if to control density of canopy
        if (np.random.uniform(0, 1) < 0.25): img.putpixel((i, j), (0, 0, 0))






# to do a tree. start with centre, thickness, #branch. random to add branch, then add centre, thickness




img.save(fileout, "PNG")


