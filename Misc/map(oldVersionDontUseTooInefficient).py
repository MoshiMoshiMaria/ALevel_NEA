import random
class Map:
    def __init__(self):
        with open("stars.txt","rt") as in_file:
            data = in_file.readlines()
            dataStrip = []
            for y in data:
                dataStrip.append(y.strip())
        self.quadrant = []
        used = []
        for x in range(random.randint(5,10)):
            line = []
            for y in range(random.randint(10,15)):
                star = random.choice(dataStrip)
                while star in used:
                    star = random.choice(dataStrip)
                used.append(star)
                line.append(star)
            self.quadrant.append(line)

    #This function puts the stars in the dictionary to use for noting their
    #adjacent stars
    def setupAdjacencies(self):
        self.adjacencies = {}
        #get stars in dictionary first
        for x in range(len(self.quadrant)):
            for y in range(len(self.quadrant[x])):
                if self.quadrant[x][y] not in self.adjacencies:
                    self.adjacencies[self.quadrant[x][y]] = ""
    #This function will note the actually adjacencies of the stars
    #hopefully, we can just use this one function to call setupAdjacencies
    def noteAdjacencies(self):
        for x in range(len(self.quadrant)):
            for y in range(len(self.quadrant[x])):
                if x == 0:
                    #don't check above
                    if y == 0:
                        #don't check left
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
                    if y == len(self.quadrant[x])-1:
                        #don't check right
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
                    if y != 0 and y != len(self.quadrant[x])-1:
                        #check left and right
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                elif x == len(self.quadrant)-1:
                    #don't check below
                    if y == 0:
                        #don't check left
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                    
                    if y == len(self.quadrant[x])-1:
                        #don't check right
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                    if y != 0 and y != len(self.quadrant[x])-1:
                        #check left and right
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                else:
                    #check above and below
                    if y == 0:
                        #don't check left
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                    if y == len(self.quadrant[x])-1:
                        #don't check right
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
                    if y != 0 and y != len(self.quadrant[x])-1:
                        #check left and right
                        try:
                            adjacentR = self.quadrant[x][y+1]
                        except IndexError:
                            adjacentR = None
                        try:
                            adjacentL = self.quadrant[x][y-1]
                        except IndexError:
                            adjacentL = None
                        try:
                            adjacentU = self.quadrant[x-1][y]
                        except IndexError:
                            adjacentU = None
                        try:
                            adjacentD = self.quadrant[x+1][y]
                        except IndexError:
                            adjacentD = None
                        if adjacentL != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentL)+";")
                        if adjacentU != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentU)+";")
                        if adjacentR != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentR)+";")
                        if adjacentD != None:
                            self.adjacencies[self.quadrant[x][y]] += (str(adjacentD)+";")
    def showAllAdjacencies(self):
        for x in self.quadrant:
            for y in x:
                print("{}: {}".format(y,self.adjacencies[y]))

