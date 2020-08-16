#! /usr/bin/python3
# general input function

def askfunc(prompt, info, type_, min_, max_, default):
    # info deprecated, not removed yet in case
    while True:
        result = input(prompt)
        if (result == 'd'):
            return default        
        try:
            result = type_(result) 
        except ValueError:
            print("Input type must be {0}.".format(type_.__name__))
            continue
        if (result < min_):
            print("Try again, minimum value is {0}.".format(min_))
        elif (result > max_):
            print("Try again, maximum value is {0}.".format(max_))
        else:
            return result

