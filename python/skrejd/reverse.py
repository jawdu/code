#! /usr/bin/python3

# reverse operations
import random
import inputs

def reverse(ns, audio):
    # main reverse function

    lscale = 44100 * inputs.askfunc("Enter length scale in seconds, or 'd' for default: ", "length scale", int, 1, 100, 2)
    dscale =  44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 5)
    cscale = inputs.askfunc("Enter decimal probability of both channel reverse, or 'd' for default: ", "channel reverse", float, 0, 1, 0.4)
    
    p1 = random.randint(lscale, 4*lscale)
    while (p1 < (ns - 4*lscale)):         # bit clumsy
        ch = random.randint(0, 1)       
        while (audio[p1, ch] != 0):
            p1 += 1        
        p2 = p1 + random.randint(lscale, lscale*4)                
        while (audio[p2, ch] != 0):
            p2 += 1
        if (random.random() < cscale):
            # do 2nd channel, at similarish position
            p3 = p1 + random.randint(0, int(lscale/50))
            p4 = p2 + random.randint(0, int(lscale/50))
            ch2 = 1 - ch
            while (audio[p3, ch2] != 0):
                p3 += 1
            while (audio[p4, ch2] != 0):
                p4 += 1
            revseg(audio, p3, p4, ch2)        
        revseg(audio, p1, p2, ch)
        p1 = p2 + random.randint(dscale, dscale*3)                       

def revseg(audio, p1, p2, s):
    # reverse a segment in 1 channel
    tp = []
    for i in range(p1, p2):
        tp.append(audio[i,s])
 
    # print(p1/44100, p2/44100, len(tp)/44100) 
    for i in range(p1+1, p2):
        audio[i,s] = tp[p2-i]
   



