#! /usr/bin/python3

# user interface

import sys
# local modules
import elements
import reverse
import inputs

def options(ns, audio):
    # an interface here, where displays list of options, and each time call one or write to newfile and/or exit
    # maybe also write a log, of each option called. use subprocess
    prompt = "Select process, or '0' to write file and exit: \n 1: reverse \n 2: "

    while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("Input type must be integer")
            continue
        if not (0 <= result <= 2):
            print("Try again, valid options are 0-2")
        elif (result == 0):
            print("Finished processing, going to output file and finish")
            return
        elif (result == 1):
            reverse.reverse(ns, audio)            
        elif (result == 2):
            print("will be option 2, for now just exit")        
            sys.exit()
        else:
            # don't think it should ever get here? but anyway:
            return
    

