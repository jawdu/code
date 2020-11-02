#! /usr/bin/python3

import random
import math

def test(audio, audio1, audio2, l):
    # bland test function, to be deleted
    print("\n ...into test function...")
    for i in range(l):
        a = random.uniform(0.3, 0.7) 
        audio[i, 0] = a*audio1[i, 0] + (1-a)*audio2[i, 0]
        audio[i, 1] = (1-a)*audio1[i, 1] + a*audio2[i, 1]
    print("\n ...done test function...")
    return

def prod1(audio, audio1, audio2, l):
    # some sort of multiplying?
    print("\n ...into product function...")

    for i in range(l):
        # doing it like this to avoid overflow stuff. clumsy, but....
        audio[i, 0] = 32000 * (audio1[i, 0]/32000) * (audio2[i, 0]/32000)
        audio[i, 1] = 32000 * (audio1[i, 1]/32000) * (audio2[i, 1]/32000)
    print("\n ...done product function...")
    return

def prod2(audio, audio1, audio2, l):
    # 2nd product function
    print("\n ...into product function #2...")
    a = random.uniform(3.1, 3.99)
    b = random.uniform(0.2, 0.8)
    for i in range(l):
        b = a * b * (1 - b)
        audio[i, 0] = b * 40000 * (audio1[i, 0]/32000) * (audio2[i, 0]/32000)
        audio[i, 1] = b * 40000 * (audio1[i, 1]/32000) * (audio2[i, 1]/32000)
    print("\n ...done product function #2...")
    return

def habs(audio, audio1, audio2, l):
    # highest abs value
    print("\n ...into highest absolute value...")
    for i in range(l):
        for k in range(0, 2):    
            if (abs(audio1[i, k]) > abs(audio2[i, k])):
                audio[i, k] = audio1[i, k]
            else:
                audio[i, k] = audio2[i, k]
    print("\n ...done highest absolute value...")
    return

def labs(audio, audio1, audio2, l):
    # lowest abs value
    print("\n ...into lowest absolute value...")
    for i in range(l):
        for k in range(0, 2):    
            if (abs(audio1[i, k]) < abs(audio2[i, k])):
                audio[i, k] = audio1[i, k]
            else:
                audio[i, k] = audio2[i, k]
    print("\n ...done lowest absolute value...")
    return

def diff(audio, audio1, audio2, l):
    # take difference as output
    print("\n ...into difference...")
    audio[0, 0] = 0         # prevent overflow dealing with 0s
    audio[0, 1] = 0
    for i in range(1, l):
        #for k in range(0, 2):    
        audio[i, 0] = 0.9 * (abs(audio1[i, 0]) - abs(audio2[i, 0]))
        audio[i, 1] = 0.9 * (abs(audio2[i, 1]) - abs(audio1[i, 1]))

            # think can do better with this

    print("\n ...done difference...")
    return

def matmix(audio, audio1, audio2, l):
    # random mix of the 2 inputs

    # turn this into matrix transformation. input vectors v, w. sum Av + Bw? A, B random (0 < 1)? or...
    # below not really matrix stuff yet. just playing.

    print("\n ...into matrix mix...")
    for i in range(l):
        audio[i,0] = 0.5 * (audio1[i,0] * math.sin(audio1[i,0]/5000) + audio2[i,0] * math.sin(audio2[i,0]/5000))
        audio[i,1] = 0.5 * (audio1[i,1] * math.sin(audio1[i,1]/5000) + audio2[i,1] * math.sin(audio2[i,1]/5000))
    print("\n ...done matrix mix...")
    return

def HOLDING(audio, audio1, audio2, l):
    # weird [?] transform
    print("\n ...into HOLDING...")

    # > Since reverberation is essentially caused by a very large number of echoes, simple reverberation algorithms use several feedback delay circuits to create a large, decaying series of echoes.
#---> do some sort of (complex?) transformation. look up ideas.

    print("\n ...done HOLDING...")
    return

def fade(audio, l):
    # fade end of audio out. done automatically after user-directed function
    print("\n ...adding fade...")
    for i in range(l-10000, l):
        audio[i,0] *= (i / l-10000)
        audio[i,1] *= (i / l-10000)
    return

