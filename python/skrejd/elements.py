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

def fglitch(ns, audio):
    # periodically (maybe sample from poisson, e.g.?) flatten/modulise out bits
    while (i < (ns-80000)):        # so max length os flatten about 1.2 sec    
        i += random.randint(100, 500000)
    
    print ("Finished flatten glitch\n")
    return





