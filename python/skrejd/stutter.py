#! /usr/bin/python3

# make it stutter
import random
import inputs

def stutter(ns, audio):
    #
    density =  44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 10)

    p1 = 20000 * random.randint(3,12)    

    while (p1 < (ns - 1.5*density)):         
        ch = random.randint(0, 1)       
        if (random.random() < 0.5):
            # do 2nd channel, at similarish position
            p3 = p1 + random.randint(0, 10000)
            ch2 = 1 - ch
            stut(audio, p3, ch2)
        stut(audio, p1, ch)
        p1 += random.randint(density, density*2)                       

    print("Finished stutter \n")
    return

def stut(audio, p1, ch):

    tp = []
    p2 = p1 + 2000 * random.randint(2, 15)
    for i in range(p1, p2):
        tp.append(audio[i,ch])
    # fade in/out edges
    for i in range(10):
        tp[i] *= 0.1*i
        tp[-(i+1)] *= 0.1*i

    nstut = random.randint(2,8)
    j = p1
    for k in range(nstut):
        for i in range(len(tp)):
            audio[j+i, ch] = tp[i]        
        j += len(tp)

    # little fade in
    for i in range(10):
        audio[j+i, ch] *= 0.1*i
    


