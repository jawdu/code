#! /usr/bin/python3

# merge 2 mp3/wavs in unpredictable noise ways

import sys
import random
import time
import subprocess
import numpy as np
from scipy.io import wavfile
import funcs

files = sys.argv[1:]

for i in files:
    if i.endswith('.mp3'):
        fileout = i.rsplit('.', 1)[0] + '.wav'
        subprocess.call(['ffmpeg', '-i', i, fileout])       # needs -i to work
        i = fileout

# could make > 2 files, really... eventually...

# unlike skrejd, no need to make writeable copy of audio, as will create a 3rd file.
sr1, audio1 = wavfile.read(files[0])
sr2, audio2 = wavfile.read(files[1])

sr = min(sr1, sr2)                                  # sr for output. if different SRs, then... will be weird
l = min(len(audio1), len(audio2))
audio3 = np.empty(shape=(l, 2), dtype=np.int16)       

prompt = "\nEnter method you want to apply: \n1: test function \n"
while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("\nTry again, input type must be integer, 1-1 \n")
            continue
        if not (1 <= result <= 1):
            print("\nTry again, valid options are 1-1")
        elif (result == 1):   
            funcs.test(audio1, audio2, audio3, l)
            break
        else:
            # should never get here :)
            print("huh")
            break
  
# done, write to newfile and finish
nfile=input("Enter name for fileout: ")
newfile = nfile.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to ", newfile)
wavfile.write(newfile, sr, audio3)

