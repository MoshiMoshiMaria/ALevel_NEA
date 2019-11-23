import random, time, math #import modules needed
from grid import Grid #import Grid class from grid.py 
from enemy import Enemy, createEnemy #import Enemy class from enemy.py
from ship import Ship #import Ship class from ship.py

#had to be renamed to mapFile as map is an inbuilt function
class Map:
    def __init__(self,difficulty):
        #THESE LINES GET THE STARS INTO A RANDOMLY MADE LIST
        #THAT IS SORT OF LIKE A GRID WITH UNEVEN ROW LENGTH
        #IT ACTS MORE LIKE A COMPUTATIONAL MODEL MORE THAN
        #AN ACTUAL LIST TO USE
        with open("stars.txt","rt") as in_file:# open the text file stars.txt
            data = in_file.readlines() #read each line of the text file
            dataStrip = [] #create an empty list to store the stripped lines
            for y in data: #for each line...
                dataStrip.append(y.strip()) #strip the line and append it to dataStrip
        self.quadrant = [] # create empty list for the stars
        used = [] #create an empty list to hold the stars that are used
        for x in range(random.randint(5,10)): #for a random number of lines between 5 and 10 inclusive
            line = [] #create an empty list for the current line
            for y in range(random.randint(10,15)): #for a random length of the line (randomness of each line adds variety)
                star = random.choice(dataStrip) #choose a random star from the dataStrip list
                while star in used: #for as long as the random choice has already been used...
                    star = random.choice(dataStrip) #choose another star
                used.append(star) #add the star to used
                line.append(star) #add the star to the line
            self.quadrant.append(line) #after the line is finished, add the ilne to the whole grid
        
        #THIS LINE FIND THE ADJACENCIES OF EACH STAR AND PUTS THEM INTO A DICT
        self.createAdjacencyList()
        #THIS LINE RANDOMLY CHOOSES A START LOCATION
        self.currentLocation = random.choice(random.choice(self.quadrant)) #choose a random starting location
        self.currentGrid = Grid(self.currentLocation,
                                   random.randint(10,20),
                                   random.randint(15,50)) #create a Grid Object for the current location/star
        #THESE LINES WILL REMEBER THE GRIDS FOR STARS USING THEIR ORDER VISITED
        self.starOrder = [] #a list used to remember the order of stars visited
        self.gridOrder = [] #a list used to hold the grids in order of their creation (index 1 of this list will belong to the star in index 1 of the one above)
        self.starOrder.append(self.currentLocation) #add the first star to the star list
        self.gridOrder.append(self.currentGrid) #add the first grid to the grid list

        #THIS LINE PLACES THE OMEGA PARTICLE (VICTORY CONDITION)
        self.placeOmega()

        #Difficulty needed to change damage and health for enemies accordingly
        self.difficulty = difficulty


    #This function puts the stars in the dictionary to use for noting their
    #adjacent stars
    def setupAdjacencies(self):
        self.adjacencies = {} #create an empty DICT for the adjacency list
        #get stars in dictionary first
        for x in range(len(self.quadrant)): #for every line...
            for y in range(len(self.quadrant[x])): #and every item in a line
                if self.quadrant[x][y] not in self.adjacencies: #if it is not in the adjacency list...
                    self.adjacencies[self.quadrant[x][y]] = "" #add it to the DICT as a key with and empty value
    #This function will note the actually adjacencies of the stars
    def noteAdjacencies(self):
        for x in range(len(self.quadrant)): #for every line in the list
            for y in range(len(self.quadrant[x])): #for every item in the current line
                try:
                    adjacentR = self.quadrant[x][y+1] #if the indexed item does not cause an IndexError then adjacentR = the item at that index
                except IndexError: #if it causes an IndexError
                    adjacentR = None #adjacentR = None
                try:
                    adjacentL = self.quadrant[x][y-1] #if the indexed item does not cause an IndexError then adjacentL = the item at that index
                except IndexError: #if it causes an IndexError
                    adjacentL = None #adjacentL = None
                try:
                    adjacentU = self.quadrant[x-1][y] #if the indexed item does not cause an IndexError then adjacentU = the item at that index                       
                except IndexError: #if it causes an IndexError
                    adjacentU = None #adjacentU = None
                try:
                    adjacentD = self.quadrant[x+1][y] #if the indexed item does not cause an IndexError then adjacentD = the item at that index
                except IndexError: #if it causes an IndexError
                    adjacentD = None #adjacentD = None

                if adjacentL != None: #adjacentL does not equal None (there was an item to the left of the current star)
                    self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";") #add that location to the adjacency list with the current star as the key
                if adjacentU != None: #if adjacentU does not equal None (there was an item to the left of the current star)
                    self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";") #add that location to the adjacency list with the current star as the key
                if adjacentR != None: #if adjacentR does not equal None (there was an item to the left of the current star)
                    self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";") #add that location to the adjacency list with the current star as the key
                if adjacentD != None: #if adjacentD does not equal None (there was an item to the left of the current star)
                    self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";") #add that location to the adjacency list with the current star as the key

    #Calls the previous two functions to create and adjacency list
                    # for a randomly created list
    def createAdjacencyList(self):
        self.setupAdjacencies()
        self.noteAdjacencies()

    def placeOmega(self):
        choice = random.choice(random.choice(self.quadrant)) #choose a random location to place the end point
        self.omegaLocation = choice #assign that choice to the variable self.omegaLocation
    def checkOmega(self):
        return self.currentLocation == self.omegaLocation #if the current location is the same as omegaLocation, return True
    def distanceFromOmega(self): #finds the length of the quickest path to the omegaLocation
        def findPath(graph,start,target): #function to find the actual path; needs parameters of the graph, the start and the end goal
            q = [[start]] #create a list to act as a queue with the start in a list inside it
            visited = [] #create an empty list to record the nodes we have visited
            if start == target: #if the start is the target, then we can return a message to the user
                return "You are on your end goal..."        
            while len(q) > 0: #whilst the length of the q is positive
                path = q.pop(0) #take the first list item from the list
                node = path[-1] #get the last item(node) of that list
                if node not in visited and node != "": #if the node has not been visited, and is not empty
                    adjacent = graph[node].split(";") #get the neighbours of the node
                    for x in adjacent: # for each of the neighbours
                        tempPath = list(path) #make tempPath a list of path to reset tempPath each iteration
                        tempPath.append(x) #add the current neighbour to the tempPath list
                        q.append(tempPath) #and then add that tempPath to the queue
                        if x == target: #if the tempPath ends on the goal...
                            return tempPath #then return the path to the goal

                    visited.append(node) #add the node to visited so we know we have already dealt with its neighbours
        def findNumberOfJumps(self): # finds the length of the path
            path = findPath(self.adjacencies,self.currentLocation,self.omegaLocation) #find out the quickest path to the end goal
            if path != "You are on your end goal...": #if the beginning is not the same as the goal...
                return len(path)-1 #then return the required number of jumps to get to the goal
            else: # if the start is the same and the goal
                return 0 #return 0 number of jumps
        return findNumberOfJumps(self) #return the result
    def getCurrentAdjacencies(self): #get the neighbours of the current star/node(in the self.adjacencies graph)
        print(self.adjacencies[self.currentLocation]) #print the adjacent nodes

    def checkInQuadrant(self,star): #check if a star is in the current quadrant
        return star in self.adjacencies #return True or False

    def checkAdjacency(self,q1,q2): #check if a star is adjacent to another
        """
        q1 = first star,
        q2 = second star
        Please use a capital letter for star names
        """
        if self.checkInQuadrant(q1): # if the star is in the quadrant...
            return str(q2)+";" in self.adjacencies[q1] #check if they are adjacent and return True or False
        return False # in the star is not in the quadrant, return False
            
    def showAllAdjacencies(self): #show all stars and their adjacent nodes/stars
        for x in self.quadrant: #for every line in self.quadrant
            for y in x: #and for every item in the line
                print("{}: {}".format(y,self.adjacencies[y])) #print the star name and its adjacency list value

    def checkIfVisited(self): #check if a star has been visited (used in the warp method) and create enemies if it hasn't
        if self.currentLocation not in self.starOrder: #if it is not in starOrder
            self.starOrder.append(self.currentLocation) #append it to the list and...
            self.gridOrder.append(Grid(self.currentLocation, #create a Grid object for it and append it onto the gridOrder list
                                   random.randint(10,20),
                                   random.randint(15,50)))
        index = self.starOrder.index(self.currentLocation) #get the index of the current location in starOrder
        self.currentGrid = self.gridOrder[index] #the the Grid from the same index in gridOrder and make it the currentGrid
        factions = [ #a list of factions for createEnemy() to use
        "UFP",
        "Klingon",
        "Bajoran",
        "Cardassian",
        "Dominion",
        "Breen",
        "Hirogen",
        "Borg",
        "Romulan",
        "Orion Pirates",
        "Nausicaan",
        "Aaamazzarite",
        "Acamarian",
        "Aenar",
        "Akritirian",
        "Allasomorph",
        "Antaran",
        "Berellian",
        "Ferengi",
        "Horta",
        "Kazon",
        "Ocampa",
        "Species 8472",
        "Tholian",
        "Tellarite",
        "Viidian"
        ]
        factionChoice = random.choice(factions) #choose a faction at random
        for x in range(random.randint(1,3)): #create 1-3 enemies that belong to that faction
            e = createEnemy(factionChoice) # use enemy.py function createEnemy to create an enemy
            if self.checkOmega():#always create borg on the omega system as a sort of boss
                e = createEnemy("Borg") # change e to be an enemy with the borg faction
            if self.difficulty != "709301":
                e.hull, e.shield.hp = e.hull * self.difficulty, e.shield.hp * self.difficulty
                for x in e.weapons:
                    from weapon import Weapon
                    if x.__class__ == Weapon:
                        x.damage *= self.difficulty
            self.placeEnemyOnGrid(e) #put the enemy on the currentGrid
    def checkIfEnemyOnMap(self): #find out if there is an enemy on the currentGrid
        return self.currentGrid.checkIfEnemyOnMap()#returns True if there is

    def warp(self,destination,factor): #used to change between stars and grids
        #destination = destination #maybe useless line but it's here and maybe necessary so...
        if destination + ";" in self.adjacencies[self.currentLocation]: #if the destination is a neighbour of the current star
            if str(factor).isdigit() and int(factor) > 0 and int(factor) < 10: #and the warp factor is between 1 and 10 inclusive
                self.currentLocation = destination #change the current location to the destination
                self.checkIfVisited() #check if the star has been visited
                print("Charging Warp Engines...") #flavour text
                time.sleep(2) #wait to seconds to add "atmosphere"
                print("Going to warp {}".format(factor)) #more flavour text
                print("Travelling...")
                if factor == 1:
                    time.sleep(180)
                if factor == 2:
                    time.sleep(140)
                if factor == 3:
                    time.sleep(110)
                if factor == 4:
                    time.sleep(80)
                if factor == 5:
                    time.sleep(40)
                if factor == 6:
                    time.sleep(15)
                if factor == 7:
                    time.sleep(5)
                if factor == 8:
                    time.sleep(2)
                if factor == 9:
                    time.sleep(0)                    #wait for however long the warp factor decrees
                print("Arrived at {}".format(self.currentLocation)) #tell the user that they are on a new star
                print("Powering down warp engine") #even more flavour text
                if self.checkOmega(): #if the current location is the omegaLocation
                    print("The Omega Particle is in this system!") #tell the user with this semi-flavour text
            else: #if the warp factor is higher than 10 or lower than 1, tell the user they made a mistake
                if int(factor) > 10:
                    print("We can't go faster than warp 9!")
                elif int(factor) < 1:
                    print("We can't go slower than warp 1!")
                elif factor.isDigit() == False:
                    print("Warp faactor must be a number!")
        else:
            print("Invalid Destination") #if the destination is not a neighbour of the current star, tell the user

    def displaySystem(self): #print the currentGrid and tell the user where they are
        print("_"*20) #use macrons (overscores) to box off the star name for style
        print(self.currentLocation,"-"*(19-len(self.currentLocation))) #print the name of the star followed by a varying number of dashes
        print("¯"*20) #use underscores to box off the star name for style
        self.currentGrid.getGrid() #use the Grid object function which displays the actual grid
    def move(self,direction,distance): #used for moving on a grid without need to look at co-ords
        self.currentGrid.move(direction,distance) #call the grid function move()
    def goto(self,x,y): #allows movement to a specific point
        self.currentGrid.goto(x,y) #call the grid function goto()
    def placeEnemyOnGrid(self,enemy): #place enemies on the grid
        self.currentGrid.placeEnemyOnGrid(enemy) #call the grid function placeEnemyOnGrid()
    def removeEnemyOnGrid(self,enemy): #the same as above but it removes them
        self.currentGrid.removeEnemyOnGrid(enemy)
    def checkDistance(self,x,y): #find the distance between two points
        currentLocation = self.currentGrid.getCurrentVector().split(";") #get the players current location as [x,y]
        curX, curY = int(currentLocation[0]),int(currentLocation[1])
        xDiff = (curX - x)
        yDiff = (curY - y)
        mag = (math.sqrt(xDiff**2+yDiff**2))
        return mag
    def enemyCheckDistance(self,enemy):
        currentLocation = self.currentGrid.getCurrentVector().split(";")
        curX, curY = int(currentLocation[0]),int(currentLocation[1])
        def enemyLocation():
            for y in range(len(self.currentGrid.gridList)):
                for x in range(len(self.currentGrid.gridList[y])):
                    if self.currentGrid.gridList[y][x] == enemy:
                        return x,y            #returned as INTs    
                    
        enemyX, enemyY = enemyLocation()
        xDiff = (curX - enemyX)
        yDiff = (curY - enemyY)
        mag = (math.sqrt(xDiff**2+yDiff**2))
        return mag
    def moveEnemy(self,direction,enemy):
        self.currentGrid.moveEnemy(direction,enemy)
    
dave = Map(1) #Class instance for testing

def adjacenciesTest():
    print("ADJACENCIES")
    print("¯¯¯¯¯¯¯¯¯¯¯")
    dave.showAllAdjacencies()
    print("\nLIST OF STARS AS ~GRID")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for x in dave.quadrant:
        print(x)

