#! /usr/bin/python3

#https://codegolf.stackexchange.com/questions/35835/draw-random-black-and-white-forest

# some sort of branching i.e. fractal-ish
# furthest to nearest - so overwrite?
# 
# 800 x 600
#
# horizon at limit say 300

# too dense, overwriting. further trees - less black . like pixels spaced.

# got pillow c.f. https://stackoverflow.com/questions/33484244/create-modify-and-save-an-image-in-python-3-x

# define leaf line then apply one pattern above, prob just gaussianish around horizon+150ish
# an array(x) with y values defining the transition pixel
# then algorithm for trunks & partial leaf


from PIL import Image
import time
import numpy as np

fileout = "rForest-" + time.strftime("%H%M%S") + ".png" # timestamped filename so we can run many times

img = Image.new("RGB", (800,600), (255, 255, 255)) #initialise as white

# define transition.  maybe need to make this smooth ones day

boundary = np.random.normal(450, 5, size=(1, 800)).astype(int)



img.save(fileout, "PNG")


