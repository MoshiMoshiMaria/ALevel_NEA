## this is an updated version of the adjacency list test
## the only difference is that I changed 184 lines into about 30
## well played m8
## this new version has been renamed map (previously called mapV2)
## the old, inefficient version has been renamed to map(oldVersionDontUseTooInefficient)

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
        try:
            adjacentR = alf[x][y+1]
        except IndexError:
            adjacentR = None
        try:
            if y > 0: #You've checked if these lines are necessary and they are they prevent the wraparound caused by indexing a list with -1
                adjacentL = alf[x][y-1]
            else:
                adjacentL = None
        except IndexError:
            adjacentL = None
        try:
            if x > 0: #You've checked if these lines are necessary and they are they prevent the wraparound caused by indexing a list with -1
                adjacentU = alf[x-1][y]
            else:
                adjacentU = None
                
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
