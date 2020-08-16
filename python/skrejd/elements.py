#! /usr/bin/python3

# some elementary functions for skrejd
#  -32768 to 32767 assume 16bit....

import random

def rand1(ns, audio):
    for i in range(ns):
        if random.random() < 0.1:
            audio[i, 0] = 0
        if random.random() < 0.1:
            audio[i, 1] = 0
        if random.random() < 0.1:
            audio[i, 0] = random.uniform(-0.7, 0.7)
        if random.random() < 0.1:
            audio[i, 1] = random.uniform(-0.7, 0.7)



# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
# https://stackoverflow.com/questions/4431216/python-function-call-with-variable
# ^ need
# because reverse, stretch have basically same thing, only difference on function
# once I've resolved lscale etc, stick them here



