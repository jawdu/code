#! /usr/bin/python3

# screw a wav or mp3

import sys
import time
import subprocess
from scipy.io import wavfile

filein = sys.argv[1]

if filein.endswith('.mp3'):
    fileout = filein.rsplit('.', 1)[0] + '.wav'
    subprocess.call(['ffmpeg', '-i', filein, fileout])
    filein = fileout
elif not filein.endswith('.wav'):
    # no file given
    print("nope")
    sys.exit()

# read wav. sr = sample rate (/sec), audio numpy array with data
sr, audio = wavfile.read(filein)

newfile = filein.rsplit('.', 1)[0] + '.' + time.strftime("%d%H%M%S") + '.wav'
print(newfile)

# change audio

wavfile.write(newfile, sr, audio)


# ideas/todo:

# command line list options. maybe also string of numbers to do multiple processes. random option(s)
# input numeric string? so 642631 = do 6, then 4, then etc etc [but #fx? ]
# if e.g. reverse, start from a wave[n] and find such that wave[n_2] = wave[n] and reverse between
# e.g: modulate/flat noise / reverse bits / chop up / waveify / some quite drastic randomise stuff / use of chaotic systems


