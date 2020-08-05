#! /usr/bin/python3

# merge 2 mp3/wavs in unpredictable noise ways

import sys
import time
import subprocess
import numpy as np
from scipy.io import wavfile


file1 = sys.argv[1]
file2 = sys.argv[2]

if file1.endswith('.mp3'):
    fileout = file1.rsplit('.', 1)[0] + '.wav'
    subprocess.call(['ffmpeg', file1, fileout])
    file1 = fileout

if file2.endswith('.mp3'):
    fileout = file2.rsplit('.', 1)[0] + '.wav'
    subprocess.call(['ffmpeg', file2, fileout])
    file2 = fileout

# all above: 2 x as much as i need :)

sr1, audio1 = wavfile.read(file1)
sr2, audio2 = wavfile.read(file2)

# unlike skrejd, no need to make writeable copy of audio, as will create a 3rd file.

