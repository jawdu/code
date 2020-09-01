#! /usr/bin/python3

# merge 2 mp3/wavs in unpredictable noise ways

import sys
import random
import time
import subprocess
import numpy as np
from scipy.io import wavfile

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

sr = min(sr1, sr2)                                  # sr for output. prob this is... iffy
l = min(len(audio1), len(audio2))
audio3 = np.empty(shape=(l, 2), dtype=np.int16)       # use zeros if empty gives any weirdness....

for i in range(l):
    a = random.uniform(0.3, 0.7) 
    audio3[i, 0] = a*audio1[i, 0] + (1-a)*audio2[i, 0]
    audio3[i, 1] = (1-a)*audio1[i, 1] + a*audio2[i, 1]
    

# done, write to newfile and finish

nfile=input("Enter name for fileout: ")

newfile = nfile.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to ", newfile)
wavfile.write(newfile, sr, audio3)

