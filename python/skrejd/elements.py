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

# try a sort of map onto a sin
# here first, before make a file for these sorta things?


def slow(ns, audio):
    # slow segments. how to do this:
    # between p1, p2
    # slow section: start to double samples (like from 1 in 3, to 1/2, to every)
    # or do prob based, so from 0.2 to 1.0, for same 
    # but also to manage transition: keep normal section. but fade that out quickly
    # fade normal back in, and fade out slow as approproach p2
    k = 1

