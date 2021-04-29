#! /usr/bin/python3
# reverbs???

import inputs
import random

def reverb(ns, audio):

    # 1: reverb only (as option)
    # 2: care to avoid feedback loop, do reverbs normally do reverbs of reverbs?
    # 3: create naive model before looking up what people do (i.e. model point source in a circular room?
    # 4: will have to make audio(2, ns) longer because of reverb.
    # --- maybe ... audio[t] += reflected m-b ish hump-tail of previous t interval


    # for i = 0:ns
    #       audio += calculateReverb(i, audio, parameters)
    # for i > ns until audio(i-1) < epsilon
    #       audio.append.calculateReverb

    #print("Note, reverb may take over a minute for longer files, whole-file, and higher bitrates.... \n" )
    
    print("Finished reverb \n")
    return

def simpleReverb(ns, audio, tparam):
    # tparam a timeparameter

    print(" - ")
    return


