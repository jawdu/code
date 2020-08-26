#! /usr/bin/python3
# reduce bit/sample rate

import inputs

def lofi(ns, audio):
    # over whole duration only so far

    bitrate = 17 - inputs.askfunc("Enter bit rate, or 'd' for default: ", "bitrate", int, 3, 16, 8)
    modval = 2**bitrate

    print("Note, may take over a minute for longer files and higher bitrates.... \n" )

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

    print("Finished lo-fi \n")
    return


