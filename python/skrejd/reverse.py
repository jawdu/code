#! /usr/bin/python3

# reverse operations
import random

def reverse(ns, audio):
    # main reverse function
    lscale, dscale, cscale = revinput(ns)
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
 
    print(p1/44100, p2/44100, len(tp)/44100) 
    for i in range(p1+1, p2):
        audio[i,s] = tp[p2-i]
   
def revinput(ns):
    # get user inputs, or defaults
    # max in relation to ns: upper limit for lscale. dscale irrelevant (means just 1 reverse)
    lscale = int(ns/120)        #input("Enter length scale in seconds, or '0' for default: ")
    dscale = int(ns/80)         #input("Enter density scale in seconds, or '0' for default: ")
    cscale = 0.4                #float(input("Enter decimal probability of both channel reverse, or '0' for default: "))

# ___>> issues here. return to defaults, sort out input in seperate test programs
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# want for lscale = f_name("message", type, min, max, default)
# also put this elsewhere for use in other functions

    return lscale, dscale, cscale




