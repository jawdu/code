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

# try a sort of map onto a sin
# here first, before make a file for these sorta things?

def reverse(ns, audio):
    # do some selective reversing
        # if e.g. reverse, start from a wave[n] and find such that wave[n_2] = wave[n] and reverse between
        # sometime 1 channel; sometimes superposition of rev & normal (normalised obv)...
        # ask user for some input parameters now?
        # -32768 to 32767 assume 16bit....
        # limit to say < |10000| to ensure will find match value
        # alt method: make array of given value over whole wav, then use this is create reversal
        # want robust for short and long files though        

    a = audio[417770, 0] # interim
    b = 0                           # kinda interim?
    k = 40100                   # interim
    tp = []
    while (k < ns): #(a != b) and
        if audio[k, 0] == a:
            b += 1
        k+=1
        if b == 30:
            p1 = k
        if b == 50:
            p2 = k

    print(p1/44100, p2/44100) # handy to get seconds so know when stuff will happen
    # getting order 100 < # < 1000 for 7 million NS
    # reverses nicely! just ned more

    for i in range(p1, p2):
        tp.append(audio[i,0])
 
    print(p1, p2, len(tp)) 
    for i in range(p1+1, p2):
        audio[i,0] = tp[p2-i]



