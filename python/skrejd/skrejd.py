#! /usr/bin/python3

# screw a wav or mp3

import sys
import time     # for generating out.filename
import subprocess
import numpy as np
from scipy.io import wavfile
# local modules
import interface

filein = sys.argv[1]

if filein.endswith('.mp3'):
    fileout = filein.rsplit('.', 1)[0] + '.wav'
    subprocess.call(['ffmpeg', '-i', filein, fileout]) # needs -i to work
    filein = fileout
    print()
    print("Converted mp3 to wav \n")
    print()
elif not filein.endswith('.wav'):
    # no compatible file given
    print("not a wav or mp3, exiting...")
    sys.exit()

# read wav. sr = sample rate (/sec), nt ndim (i.e. mono/stereo), audio np array audio[a,b] a=sound, |b| = 1,2 
sr, audioIn = wavfile.read(filein)

# have to make writeable array, audioIn is just pointing at source.
if audioIn.ndim == 1:
    # make stereo
    audio = np.array([audioIn, audioIn])
    audio = np.transpose(audio)
else: audio = audioIn.copy()

ns = len(audio)

print("Ready to process audio... \n")

interface.options(ns, audio)

# done, write to newfile and finish
newfile = filein.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to: ", newfile, " - exiting...\n")
wavfile.write(newfile, sr, audio)

# ideas/todo:

# e.g: modulate/flat noise / reverse bits / chop up / waveify / some quite drastic randomise stuff / use of chaotic systems
# remember on numpy vs just python list, what is efficient in py/np

