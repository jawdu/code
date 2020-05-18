#! /usr/bin/python3

# implemention of Conway's FRACTRAN programming language https://en.wikipedia.org/wiki/FRACTRAN 
# also https://esolangs.org/wiki/Fractran

# A FRACTRAN program is an ordered list of positive fractions together with an initial positive integer input n. The program is run by updating the integer n as follows:

#   for the first fraction a/b in the list for which na/b is an integer, replace n by na/b
#   repeat this rule until no fraction in the list produces an integer when multiplied by n, then halt.


import re
import sys
# for exit

a = []
b = []
k = 0

print("Enter fractions in sequence, in the form 'a/b', or any other expression to finish: ")

while True:
    frac_in = input()
    if re.match('^[0-9]+/[0-9]+$', frac_in):
        t1, t2 = re.split('/', frac_in)
        a.append(int(t1))
        b.append(int(t2))        
        continue
    else:
        print("done")    
        break

while True:
    n = input("Enter positive integer n: ")
    if not n.isdigit():
        print("Not positive integer, sorry.")
        continue
    else:
        n = int(n)
        break

p = 0

while k < len(a):
    if (n*a[k]/b[k]) % 1 == 0:
        n = n * a[k]/b[k]
        k = 0
        print("New n: ", n)
        p += 1
        if p>1000:
            print("early exit new n loop")
            sys.exit()
    else:
        k += 1
        print("Same n: ", n)
        p += 1
        if p>1000:
            print("early exit same n loop")
            sys.exit()

print("Exited safely")

