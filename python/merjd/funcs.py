#! /usr/bin/python3

import random

def test(audio, audio1, audio2, l):
    # bland test function, to be deleted
    print("\n ...into test function...")
    for i in range(l):
        a = random.uniform(0.3, 0.7) 
        audio[i, 0] = a*audio1[i, 0] + (1-a)*audio2[i, 0]
        audio[i, 1] = (1-a)*audio1[i, 1] + a*audio2[i, 1]
    print("\n ...done test function...")
    return



def fade(audio, l):
    # fade end of audio out
    print("\n ...adding fade...")
    for i in range(l-50000, l):
        audio[i,0] *= (l-i / l-50000)
        audio[i,1] *= (l-i / l-50000)
    return

