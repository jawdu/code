#! /usr/bin/python3

import random

def test(audio1, audio2, audio3, l):
    # bland test function, to be deleted

    for i in range(l):
        a = random.uniform(0.3, 0.7) 
        audio3[i, 0] = a*audio1[i, 0] + (1-a)*audio2[i, 0]
        audio3[i, 1] = (1-a)*audio1[i, 1] + a*audio2[i, 1]

    return


