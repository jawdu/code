#! /usr/bin.python3

# stretch/slow segments
# this will also be sorta similar to reverse, in structure..?

import random
import inputs

def stretch(ns, audio):

    lscale = 44100 * inputs.askfunc("Enter length scale in seconds, or 'd' for default: ", "length scale", int, 1, 100, 10)
    dscale =  44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 10)
    cscale = inputs.askfunc("Enter decimal probability of both channel reverse, or 'd' for default: ", "channel reverse", float, 0, 1, 0.4)
    
    # so this is just same as in reverse, only different function call (slow, not revseg). will rationalise 
    # when I have tidied up lscale/dscale stuff, and stick in elements. c.f. how i did it for sglitch? better?
   
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
            slow(audio, p3, p4, ch2, 0.8)        
        slow(audio, p1, p2, ch, 0.8)
        p1 = p2 + random.randint(dscale, dscale*3)                       

    print("Finished stretch \n")
    return

def slow(audio, p1, p2, s, rate):
    # slow segments.
    # also maybe do a 'wobble' so more like turntable variable speed?
    
    tp = []
    for i in range(p1, p2):
        tp.append(audio[i,s])
    j = 0 
    for i in range(p1, p2):
        if random.random() < rate:       # use of like under 0.5 good for short noisey messed up bits - spin off?
                                    # set up so exponential from say 0.95-0.3 at end of range
            j += 1
        audio[i,s] = tp[j]
    # make sure no discontinuity
    for i in range(-10, 10):
        audio[p2+i,s] = audio[p2+i,s] * 0.1 * abs(i)

def sglitch(ns, audio):
    # slowglitch
    # do v small. now need to add more (user input density, if nothing else)

    density = 44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 5)
    p1 = 20000 * random.randint(3,12)    

    while (p1 < (ns - density)):         
        ch = random.randint(0, 1)       
        p2 = p1 + 40000 + 2000 * random.randint(1, 20)                
        if (random.random() < 0.4):
            # do 2nd channel, at similarish position
            p3 = p1 + random.randint(0, 10000)
            p4 = p2 + random.randint(0, 10000)
            ch2 = 1 - ch
            rate = random.uniform(0.1, 0.5)
            slow(audio, p3, p4, ch2, rate)
        rate = random.uniform(0.1, 0.5)        
        slow(audio, p1, p2, ch, rate)
        p1 = p2 + random.randint(density, density*2)                       

    print("Finished slow glitch \n")
    return

