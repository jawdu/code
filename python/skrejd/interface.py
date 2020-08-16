#! /usr/bin/python3
# user main menu interface

import sys
# local modules
import elements
import reverse
import stretch
import stutter

def options(ns, audio):
    # maybe also write a log, of each option called. use subprocess. or do that in option, w/parameters
    prompt = "\nSelect process, or '0' to write file and exit: \n 0: finish \n 1: reverse \n 2: stretch (slow) \n 3: slow glitch \n 4: stutter \n ........"

    while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("Try again, input type must be integer, 0-4")
            continue
        if not (0 <= result <= 4):
            print("Try again, valid options are 0-4")
        elif (result == 0):
            print("Finished processing, going to output file and finish")
            return
        elif (result == 1):
            print("Going into reverse...\n")
            reverse.reverse(ns, audio)            
        elif (result == 2):
            print("Going into stretch...\n")        
            stretch.stretch(ns, audio)
        elif (result == 3):
            print("Going into slow glitch...\n")        
            stretch.sglitch(ns, audio)
        elif (result == 4):
            print("Going into stutter...\n")        
            stutter.stutter(ns, audio)
        # option 4: some whole-audio transformation - modest, preserve but mutate. *** HOW??? ***

        else:
            # don't think it should ever get here? but anyway:
            return
    

