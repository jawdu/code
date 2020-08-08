#! /usr/bin.python3

# stretch/slow segments
# this will also be sorta similar to reverse, in structure..?

def stretch(ns, audio):

    lscale = 44100 * inputs.askfunc("Enter length scale in seconds, or 'd' for default: ", "length scale", int, 1, 100, 20)
    dscale =  44100 * inputs.askfunc("Enter density scale in seconds, or 'd' for default: ", "density scale", int, 1, 100, 20)
    cscale = inputs.askfunc("Enter decimal probability of both channel reverse, or 'd' for default: ", "channel reverse", float, 0, 1, 0.4)
    



    return


def slow(audio, p1, p2, s):
    # slow segments. how to do this:
    # between p1, p2
    # slow section: start to double samples (like from 1 in 3, to 1/2, to every)
    # or do prob based, so from 0.2 to 1.0, for same 
    # but also to manage transition: keep normal section. but fade that out quickly
    # fade normal back in, and fade out slow as approproach p2
    # also maybe do a 'wobble' so more like turntable variable speed    
    k = 1

