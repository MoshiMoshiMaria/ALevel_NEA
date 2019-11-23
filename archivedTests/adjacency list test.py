##It went perfectly - and it only took 5 hours
## unfortunately, I achieved the same result in over 150 lines less work
## the map with this version has been renamed map(oldVersionDontUseTooInefficient)
## congratulations on completing the task but honestly m8, 184 fuckin' lines!

import random
alf = []
count = 0
for x in range(random.randint(1,6)):
    gay = []
    for y in range(random.randint(4,6)):
        gay.append(count)
        count += 1
    alf.append(gay)
adj = {}
for x in range(len(alf)):
    for y in range(len(alf[x])):
        adj[alf[x][y]] = ""

#This is where we find the adjacencies                
for x in range(len(alf)):
    for y in range(len(alf[x])):
        if x == 0:
            #don't check above
            if y == 0:
                #don't check left
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
            if y == len(alf[x])-1:
                #don't check right
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
            if y != 0 and y != len(alf[x])-1:
                #check left and right
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
        elif x == len(alf)-1:
            #don't check below
            if y == 0:
                #don't check left
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
            
            if y == len(alf[x])-1:
                #don't check right
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
            if y != 0 and y != len(alf[x])-1:
                #check left and right
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
        else:
            #check above and below
            if y == 0:
                #don't check left
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
            if y == len(alf[x])-1:
                #don't check right
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
            if y != 0 and y != len(alf[x])-1:
                #check left and right
                try:
                    adjacentR = alf[x][y+1]
                except IndexError:
                    adjacentR = None
                try:
                    adjacentL = alf[x][y-1]
                except IndexError:
                    adjacentL = None
                try:
                    adjacentU = alf[x-1][y]
                except IndexError:
                    adjacentU = None
                try:
                    adjacentD = alf[x+1][y]
                except IndexError:
                    adjacentD = None
                if adjacentL != None:
                    adj[alf[x][y]] += (str(adjacentL)+";")
                if adjacentU != None:
                    adj[alf[x][y]] += (str(adjacentU)+";")
                if adjacentR != None:
                    adj[alf[x][y]] += (str(adjacentR)+";")
                if adjacentD != None:
                    adj[alf[x][y]] += (str(adjacentD)+";")
