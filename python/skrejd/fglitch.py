#! /usr/bin/python3

# flatten glitch

import random
import inputs

def fglitch(ns, audio):
    # periodically flatten/modulise out bits
    density = inputs.askfunc("Enter relative density for glitches (0.1-100), or 'd' for default: ", "glitch density", float, 0.1, 100, 10)
    maxlen = inputs.askfunc("Enter max glitch length in seconds (0-2), or 'd' for default: ", "glitch maxlen", float, 0.1, 2.0, 1.0)
    i = 0
    while (i < (ns-100000)):         
        i += random.randint(100, 10000)
        if (random.uniform(0, 1) < (0.01 * density)):
            ch = random.randint(0, 1)
            glen = int(44100 * random.uniform(0.001, maxlen))
            if (random.random() < 0.5):
                j = i + random.randint(0, 100)
                ch2 = 1 - ch
                #stut(audio, j, glen, ch2)
            #stut(audio, i, glen, ch)
        
            i += glen # length of glitch
        
    print ("Finished flatten glitch\n")
    return



