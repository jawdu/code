#! /usr/bin/python3

# screw a wav or mp3

import sys
import time
import subprocess
import numpy as np
from scipy.io import wavfile

filein = sys.argv[1]

if filein.endswith('.mp3'):
    fileout = filein.rsplit('.', 1)[0] + '.wav'
    subprocess.call(['ffmpeg', '-i', filein, fileout])
    filein = fileout
elif not filein.endswith('.wav'):
    # no compatible file given
    print("not a wav or mp3, exiting...")
    sys.exit()

# read wav. sr = sample rate (/sec), nt ndim (i.e. mono/stereo), audio np array audio[a,b] a=sound, |b| = 1,2 
sr, audioIn = wavfile.read(filein)
ns = audioIn.ndim

# have to make copy, audio is just pointing at source. check if stereo
if audioIn.ndim == 1: # make stereo
    print("yes")
    audio = np.array([audioIn, audioIn])
    audio = np.transpose(audio)
else: audio = audioIn.copy()

ns = len(audio)
for i in range(ns):
    audio[i, 0] = 0.
# ^ test - start adding stuff now


# done, write to newfile and finish
newfile = filein.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to ", newfile)
wavfile.write(newfile, sr, audio)

# ideas/todo:

# input numeric string? so 642631 = do 6, then 4, then etc etc [but #fx? ]
# if e.g. reverse, start from a wave[n] and find such that wave[n_2] = wave[n] and reverse between
# e.g: modulate/flat noise / reverse bits / chop up / waveify / some quite drastic randomise stuff / use of chaotic systems
# slow/speed up: add duplicate values (or just for l or r, then take away later on to conserve length)

