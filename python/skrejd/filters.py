#! /usr/bin.python3

# filters
# also band pass filter (or generalise...?)

import random
import inputs

def filters(ns, audio):
    result = input("\n Enter 1 for high-pass filter, any other key for low-pass: ")
    if (result == 1):
        hpf(ns, audio)
    else:
        lpf(ns, audio)
    print("Finished filters \n")
    return

def hpf(ns, audio):
    print("\n into hpf...")
    
    return

def lpf(ns, audio):
    # y[i] = b * x[i] + (1-b)y[i-1]  0 < b < 1   y is filtered; x unfiltered. b=1 = filter freq = sample rate (i.e. no change)
    print("\n into lpf...")
    
    b = inputs.askfunc("Enter frequency (0-1), or 'd' for default: ", "frequency", float, 0.0, 1.0, 0.1)

    # ask for degree of variablity? vary it gradually at random, also independent channel?

    audio[0, 0] = 0.0
    audio[0, 1] = 0.0
    for i in range(1, ns):
        audio[i, 0] = b * audio[i, 0] + (1 - b) * audio[i-1, 0] 
        audio[i, 1] = b * audio[i, 1] + (1 - b) * audio[i-1, 1] 
 
    return

