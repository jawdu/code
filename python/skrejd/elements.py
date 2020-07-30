#! /usr/bin/python3

# some elementary functions for skrejd

def random1(ns, audio):
    for i in range(ns):
        audio[i, 0] = 0
        audio[i, 1] = 0

