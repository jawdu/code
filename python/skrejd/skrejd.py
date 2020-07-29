#! /usr/bin/python3

# screw a wav or mp3

import sys
import subprocess
from scipy.io import wavfile

filein = sys.argv[1]

# check if wav or mp3. if mp3:
# subprocess.call(['ffmpeg', '-i', 'audio.mp3', 'audio.wav'])

# read wav
# fs, data = wavfile.read('audio.wav')

