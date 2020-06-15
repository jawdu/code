#! /usr/bin/python3

#https://codegolf.stackexchange.com/questions/35835/draw-random-black-and-white-forest
# got pillow c.f. https://stackoverflow.com/questions/33484244/create-modify-and-save-an-image-in-python-3-x

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
    if (np.random.uniform(0, 1) < 0.45): img.putpixel((i, p), (0, 0, 0))
    if (np.random.uniform(0, 1) < 0.25): img.putpixel((i, p+1), (0, 0, 0))
    if (np.random.uniform(0, 1) < 0.25): img.putpixel((i, p-1), (0, 0, 0))
    horizon.append(p)

    # try v v v low density shading under horizon?

    for j in range(599, p, -1):
        if (np.random.uniform(0, 1) < 0.01): img.putpixel((i, j), (0, 0, 0))


# make the path.

pStart = int(370 + np.random.uniform(-50, 50))
pEnd = int(430 + np.random.uniform(-50, 50))
pCentre = []
h = 600 - horizon[pEnd]

# add one sin from start, one from end, roughly randomised so they overlap in middle

s1p = np.random.uniform(0.8, 1.2) * h/2 
s2p = np.random.uniform(0.8, 1.2) * h/2 
s1a = np.random.uniform(-25, 25) # more as closer
s2a = np.random.uniform(-15, 15) # less as further

for i in range(599, horizon[pEnd], -1):
        pa = (pStart - pEnd) / h
        pb = pStart - ((pStart - pEnd) / (1 - horizon[pEnd]/600))
        pc = 0

        if ((horizon[pEnd] - i) < s1p): 
            pc = s1a * math.sin(3.14*(600-i)/(s1p))
        if ((horizon[pEnd] - i) > s2p): 
            pc = s2a * math.sin(3.14*(600-i)/(s2p))
                     
        # rough parameter of path width. start: 20 end: 5  -> gradient
        w = int((i * 20 / h) - 8)
        pn = int(i * pa + pb + pc)
        pCentre.append(pn)

        for j in range(-w, w):
            if (np.random.uniform(0, 1) < 0.15):
                img.putpixel((pn+j, i) , (0, 0, 0))    

# canopy & boundary

boundary = np.random.normal(150, 5, size=(1, 800))

b1 = 16 + np.random.uniform(-3, 3)
b2 = 23 + np.random.uniform(-3, 3)
b3 = 360 + np.random.uniform(-20, 20)

for i in range(800):
    # melt boundary a little. maybe also add a bit of a abs|sin| to make it a little bumpy
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

# make averaged boundary

bAv = [(boundary[0,0] + boundary[0,1])/2, (boundary[0,1] + boundary[0,2])/2]

for i in range(796):
    bAv.append(0)
    for j in range (5):
        bAv[i+2] += boundary[0, i+j] / 5

bAv.append((boundary[0,797] + boundary[0,798])/2)
bAv.append((boundary[0,798] + boundary[0,799])/2)

# trees

tx = []; tw = []; ty = []; td = []

# to fix that bug - some sort of averaged canopy value over c. 5 x values. maybe do this at start
# ... define length of tree when created. fade into canopy?
# or change canopy to discrete function, but add noise after

# new algorithm, a tree based on x range 'buckets':

for i in range(49): 

    x = 16 + i*16 + np.random.randint(-5, 5)
    if (i==0): y = np.random.randint(300, 580); j = 0;
    else: y = 300 + (ty[i-j-1] - 120 + np.random.randint(0, 100)) % 290
# ^^^ i think this not quite ideal, tinker

    # check not path before adding to array. j little hack to fix index issue when skipping
    if (abs(pCentre[599-y] - x)) < 16: j += 1
    else:    
        tx.append(x); ty.append(y)
        if x > pCentre[599-y]: td.append(1) # make curl away from path
        else: td.append(-1)
        tw.append(int(0.058 * ty[i-j] + np.random.uniform(10, 16))) 

for i in range(len(tx)): 

    # do the base
    for l in range(int(tw[i]/2)):
        for k in range(int(-tw[i]/2), int(tw[i]/2)):
            t =  0.2 * 2 * l / tw[i]
            if (np.random.uniform(0,1) < t) and ((tx[i]+k) > 0) and ((tx[i]+k) < 799): 
                img.putpixel((tx[i]+k, ty[i]), (0, 0, 0))
        tw[i] -= 1
        ty[i] -= 1

# ^ base bit timid. maybe separate width parameter out, do 3 x width in x to give better spread

    while ty[i] != 0:
        for j in range(int(-tw[i]/2), int(tw[i]/2)):
            if (np.random.uniform(0, 1) < 0.35) and ((tx[i]+j) > 0) and ((tx[i]+j) < 799):
                img.putpixel((tx[i]+j, ty[i]), (0, 0, 0))
        ty[i] -= 1
        if ty[i] < bAv[tx[i]]:
            ty[i] = 0
            # want to maybe do this c.10 pixels before, then spread into canopy
        if (np.random.uniform(0, 1) < 0.2): tx[i] += int(np.random.uniform(-1,  2)) * td[i]


        

img.save(fileout, "PNG")


