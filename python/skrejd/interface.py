#! /usr/bin/python3
# user main menu interface

import sys
# local modules
import elements
import fglitch
import filters
import lofi
import reverb
import reverse
import stretch
import stutter

def options(ns, audio):
    # maybe also write a log, of each option called. use subprocess. or do that in option, w/parameters
    prompt = "\nSelect process, or '0' to write file and exit: \n 0: finish \n 1: reverse \n 2: stretch (slow) \n 3: slow glitch \n 4: stutter \n 5: flatten glitch \n 6: lo-fi \n 7: filter \n 8: reverb \n ........................"

    while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("\nTry again, input type must be integer, 0-8 \n")
            continue
        if not (0 <= result <= 8):
            print("\nTry again, valid options are 0-8")
        elif (result == 0):
            print("\nFinished processing, going to output file and finish...\n")
            return
        elif (result == 1):
            print("\nGoing into reverse...\n")
            reverse.reverse(ns, audio)            
        elif (result == 2):
            print("\nGoing into stretch...\n")        
            stretch.stretch(ns, audio)
        elif (result == 3):
            print("\nGoing into slow glitch...\n")        
            stretch.sglitch(ns, audio)
        elif (result == 4):
            print("\nGoing into stutter...\n")        
            stutter.stutter(ns, audio)
        elif (result == 5):
            print("\nGoing into flatten glitch...\n")        
            fglitch.fglitch(ns, audio)
        elif (result == 6):
            print("\nGoing into lo-fi...\n")        
            lofi.lofi(ns, audio)
        elif (result == 7):
            print("\nGoing into filters...\n")  
            filters.filters(ns,audio)
        elif (result == 8):
            print("\nGoing into reverb...\n")  
            reverb.reverb(ns,audio)
        # something where... I kinda map it onto a sine (or other periodic function?)
        else:
            # don't think it should ever get here? but anyway:
            return
    

