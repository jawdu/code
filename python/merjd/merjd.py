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

prompt = "\n Available methods: \n  0: test function \n  1: basic product function \n  2: 2nd product function \n  3: highest abs value function \n  4: lowest abs value function \n  5: difference function \n  6: matrix mix \n  7: UNTITLED \n Enter method you want to apply: "
while True:
        result = input(prompt)
        try:
            result = int(result) 
        except ValueError:
            print("\nTry again, input type must be integer, 0-7 \n")
            continue
        if not (0 <= result <= 10):
            print("\nTry again, valid options are 1-7")
        elif (result == 0):             # delete this one once sorted
            funcs.test(audio, audio1, audio2, l)
            break
        elif (result == 1):
            funcs.prod1(audio, audio1, audio2, l)
            break
        elif (result == 2):
            funcs.prod2(audio, audio1, audio2, l)
            break
        elif (result == 3):
            funcs.habs(audio, audio1, audio2, l)
            break
        elif (result == 4):
            funcs.labs(audio, audio1, audio2, l)
            break
        elif (result == 5):
            funcs.diff(audio, audio1, audio2, l)
            break
        elif (result == 6):
            funcs.matmix(audio, audio1, audio2, l)
            break
        elif (result == 7):
            funcs.HOLDING(audio, audio1, audio2, l)
            break
        else:
            # sneaky exit 
            print("huh")
            break

funcs.fade(audio, l)                # add in a ~1 sec fade at end, 
  
# done, write to newfile and finish
nfile=input("\n Enter name for fileout: ")
newfile = nfile.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print(" Written to ", newfile)
wavfile.write(newfile, sr, audio)

