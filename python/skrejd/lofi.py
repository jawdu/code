#! /usr/bin/python3
# reduce bit/sample rate

import inputs
import random

def lofi(ns, audio):

    print("Note, lo-fi may take over a minute for longer files, whole-file, and higher bitrates.... \n" )
    bitrate = 17 - inputs.askfunc("Enter bit rate, or 'd' for default: ", "bitrate", int, 3, 16, 8)
    modval = 2**bitrate
    choice = input("Enter 'y' for whole-file lo-fi, any other key for partial lo-fi: \n")
    if choice == "y":
       whole_lofi(ns, audio, bitrate, modval)         
    else:
        dscale=44100*inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 10)
        lscale=44100* inputs.askfunc("Enter length scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 5)

        p1 = random.randint(0, dscale)
        while (p1 < (ns - lscale)):
            p2 = p1 + random.randint(0.6*lscale, 1.4*lscale)
            p2 -= p2 % bitrate          # make sure [p1, p2] interval is sound
            ch = random.randint(0, 1)       
            if (random.random() < 0.5):
                # do 2nd channel, at similarish position
                p2 = p1 + random.randint(0, 10000)
                ch2 = 1 - ch
                part_lofi(ns, audio, bitrate, modval, p1, p2, ch2)
            part_lofi(ns, audio, bitrate, modval, p1, p2, ch)
            p1 += random.randint(0.8*dscale, 2*dscale)    

    print("Finished lo-fi \n")
    return

def part_lofi(ns, audio, bitrate, modval, p1, p2, ch):

    if (p2 > ns):
        return

    while (p1 < p2):
        if (audio[p1, ch] > 0):
            audio[p1, ch] -= audio[p1, ch] % modval
        else:
            audio[p1, ch] += audio[p1, ch] % modval
        for i in range(1, bitrate):
            audio[p1+i, ch] = audio[p1, ch]
        p1 += bitrate        
    return

def whole_lofi(ns, audio, bitrate, modval):
    # whole-file lo-fi
    i = 0
    while (i < (ns-bitrate-1)):
        for j in [0, 1]:
            if (audio[i,j] > 0):
                audio[i,j] -= audio[i,j] % modval                
            else:                  # negative
                audio[i,j] += audio[i,j] % modval
            for k in range(1, bitrate):
                audio[i+k,j] = audio[i,j]
        i += bitrate
    return


