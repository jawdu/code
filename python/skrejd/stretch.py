#! /usr/bin.python3

# stretch/slow segments
# this will also be sorta similar to reverse, in structure..?

import random
import inputs

def stretch(ns, audio):

    lscale = 44100 * inputs.askfunc("Enter length scale in seconds, or 'd' for default: ", "length scale", int, 1, 100, 20)
    dscale =  44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 20)
    cscale = inputs.askfunc("Enter decimal probability of both channel reverse, or 'd' for default: ", "channel reverse", float, 0, 1, 0.4)
    
    # just do one bit for now.
    ch = 0
    p1 = 3*44100
    p2 = 12*44100

    slow(audio, p1, p2, ch) 

    return

def slow(audio, p1, p2, s):
    # slow segments.

    # slow section: start to double samples (like from 1 in 3, to 1/2, to every)
    # or do prob based, so from 0.2 to 1.0, for same 
    # but also to manage transition: keep normal section. but fade that out quickly
    # fade normal back in, and fade out slow as approproach p2
    # also maybe do a 'wobble' so more like turntable variable speed    
    
    tp = []
    for i in range(p1, p2):
        tp.append(audio[i,s])

    j = 0 
    for i in range(p1, p2):
        if random.random() < 0.8:
            j += 1
        audio[i,s] = tp[j]



