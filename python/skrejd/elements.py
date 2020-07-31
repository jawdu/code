#! /usr/bin/python3

# some elementary functions for skrejd

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

def reverse(ns, audio):
    # do some selective reversing
        # if e.g. reverse, start from a wave[n] and find such that wave[n_2] = wave[n] and reverse between
        # sometime 1 channel; sometimes superposition of rev & normal (normalised obv)...
        # ask user for some input parameters now?
        # -32768 to 32767 assume 16bit....
        # limit to say < |10000| to ensure will find match value
        
    a = audio[40000, 0]
    b = 0
    k = 40100
    while (k < ns): #(a != b) and
        b = audio[k, 0]
        k+=1
  
    print(k, b)  

