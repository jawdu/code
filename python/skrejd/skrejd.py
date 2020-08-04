#! /usr/bin/python3

# screw a wav or mp3

import sys
import time
import subprocess
import numpy as np
from scipy.io import wavfile
# local modules
import elements
import reverse

filein = sys.argv[1]

if filein.endswith('.mp3'):
    fileout = filein.rsplit('.', 1)[0] + '.wav'
    #subprocess.call(['ffmpeg', '-i', filein, fileout])
    subprocess.call(['ffmpeg', filein, fileout])
    filein = fileout
    print()
    print("Converted mp3 to wav")
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

reverse.reverse(ns, audio)
sys.exit()

# done, write to newfile and finish
newfile = filein.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print("Written to ", newfile)
wavfile.write(newfile, sr, audio)



# ideas/todo:

# sample-wise multiply (and normalise) 2 x files???!! [maybe this as separate one] [as an attractor, even?]
# input numeric string? so 642631 = do 6, then 4, then etc etc [but #fx? ]
# e.g: modulate/flat noise / reverse bits / chop up / waveify / some quite drastic randomise stuff / use of chaotic systems
# slow/speed up: add duplicate values (or just for l or r, then take away later on to conserve length)

# remember on numpy vs just python list, what is efficient in py/np

