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

for (i, v) in enumerate(files):
    if v.endswith('.mp3'):
        fileout = v.rsplit('.', 1)[0] + '.wav'
        subprocess.call(['ffmpeg', '-i', v, fileout])       # needs -i to work
        files[i] = fileout

# could make > 2 files, really... eventually...

# unlike skrejd, no need to make writeable copy of audio, as will create a 3rd file.
sr1, audio1 = wavfile.read(files[0])
sr2, audio2 = wavfile.read(files[1])

sr = min(sr1, sr2)                                  # sr for output. if different SRs, then... will be weird
l = min(len(audio1), len(audio2))
audio = np.empty(shape=(l, 2), dtype=np.int16)       

t = l / 2000000          # rough time estimate

print("\nDepending on method chosen and your machine, expect to wait ~ %1.1f minutes" % (t))

prompt = "\n Available methods: \n  0: test function \n  1: product function \n Enter method you want to apply: "
while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("\nTry again, input type must be integer, 0-1 \n")
            continue
        if not (0 <= result <= 1):
            print("\nTry again, valid options are 1-1")
        elif (result == 0):             # delete this one once sorted
            funcs.test(audio, audio1, audio2, l)
            break
        elif (result == 1):
            funcs.prod(audio, audio1, audio2, l)
            break
        else:
            # should never get here :)
            print("huh")
            break

funcs.fade(audio, l)                # add in a ~1 sec fade at end, 
  
# done, write to newfile and finish
nfile=input("\n Enter name for fileout: ")
newfile = nfile.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print(" Written to ", newfile)
wavfile.write(newfile, sr, audio)

