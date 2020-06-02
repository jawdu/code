#! /usr/bin/python3

# https://codegolf.stackexchange.com/questions/62960/simulate-the-universe

import random

# u is the state of the universe
# l is label

u = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l = ["Higgs boson", "W boson", "Z boson", "gluon", "charm quark", "anticharm quark", "strange quark", "strange antiquark", "top quark", "top antiquark", "bottom quark", "bottom antiquark", "up quark", "up antiquark", "down quark", "down antiquark", "muon", "antimuon", "tau lepton", "antitau lepton", "electron", "positron", "neutrino", "antineutrino", "photon"]  
t = 0

u[0] = int(input("Enter initial number of Higgs bosons: "))

while (u[0] + u[1] + u[2] + u[12] + u[13]) != 0:

    t += 0.1
    if (u[0] !=0): #Higgs decay
        for i in range(u[0]):
           if random.random() < 0.000433:
               u[0] -= 1; p = random.random()
               if p<0.648: u[10] += 1; u[11] += 1
               elif p<0.789: u[1] += 2
               elif p<0.8772: u[3] += 2
               elif p<0.9476: u[18] += 1; u[19] += 1
               elif p<0.9803: u[4] += 1; u[5] += 1
               elif p<0.9962: u[2] += 2
               elif p<0.99843: u[24] += 2
               elif p<0.99954: u[2] += 1; u[24] += 1
               elif p<0.999784: u[16] += 1; u[17] += 1
               else: u[8] += 1; u[9] += 1

    if u[1] != 0: #W decay
        for i in range(u[1]):
            if random.random() < 0.5: 
                u[1] -= 1; u[21] += 1; p = random.random()
                if p<0.3333: u[17] += 1
                elif p<0.6666: u[19] += 1
                else: u[20] += 1

    if u[2] !=0: # Z decay
        for i in range(u[2]):
            if random.random() < 0.5:
                u[2] -= 1; p = random.random()
                if p<0.206: u[22] += 1; u[23] +=1 
                elif p<0.24: u[19] += 1; u[20] +=1
                elif p<0.274: u[17] += 1; u[18] += 1
                elif p<0.308: u[15] += 1; u[16] += 1
                elif p<0.46: u[13] += 1; u[14] += 1
                elif p<0.612: u[6] += 1; u[7] += 1
                elif p<0.764: u[10] += 1; u[11] += 1
                elif p<0.882: u[12] += 1; u[13] += 1
                else: u[4] +=1; u[5] += 1

    if u[12] !=0: # top decay
        for i in range(u[12]):
            if random.random() < 0.1295:
                u[12] -= 1; u[1] += 1; p = random.random()
                if p<0.3333: u[6] += 1
                elif p<0.6666: u[10] += 1
                else: u[14] += 1
                
    if u[13] !=0: # antitop decay
        for i in range(u[13]):
            if random.random() < 0.1295: 
                u[13] -= 1; u[1] += 1; p = random.random()
                if p<0.3333: u[7] += 1
                elif p<0.6666: u[11] += 1
                else: u[15] += 1

    update = ""
    for i in range(24, -1, -1):
        if u[i] == 1:
            if sum(u) == u[i]: update = str(u[i]) + " " + l[i] + "."
            elif update == "": update = "and " + str(u[i]) + " " + l[i] + "."
            else: update = str(u[i]) + " " + l[i] + ", " + update
        elif u[i] > 1:
            if sum(u) == u[i]: update = str(u[i]) + " " + l[i] + "s."
            elif update == "": update = "and " + str(u[i]) + " " + l[i] + "s."
            else: update = str(u[i]) + " " + l[i] + "s, " + update
    print("The universe contains " + update)

print("Simulation ended after %.1f yoctoseconds." % (t))

