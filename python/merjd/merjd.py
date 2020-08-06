#! /usr/bin/python3

# merge 2 mp3/wavs in unpredictable noise ways

import sys
import time
import subprocess
import numpy as np
from scipy.io import wavfile


files = sys.argv[1:]

for i in files:
    if i.endswith('.mp3'):
        fileout = i.rsplit('.', 1)[0] + '.wav'
        subprocess.call(['ffmpeg', '-i', i, fileout])       # needs -i to work this time?
        i = fileout

sr1, audio1 = wavfile.read(files[0])
sr2, audio2 = wavfile.read(files[1])

# unlike skrejd, no need to make writeable copy of audio, as will create a 3rd file.

# at the moment, test with 2 x glijd [same size]

sys.exit()

# done, write to newfile and finish

nfile=input("Enter name for fileout: ")

newfile = nfile.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to ", newfile)
wavfile.write(newfile, sr, audio)

