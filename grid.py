import random, math
from enemy import Enemy, Weapon, Shield
from ship import Ship
class Grid:
    def __init__(self,star,height,width):
        self.star = star
        self.width = width
        self.height = height
        self.gridList = []
        self.formGrid()
        self.placeShipOnGrid()

    def drawStarGrid(self):
        for x in range(self.height):
            print(x,end = " ")
            print((2-len(str(x)))*" ",end = "")
            for y in range(self.width):
                if x < 10:
                    print("*",end = (3-len(str(x)))*" ")
                else:
                     print("*",end = (4-len(str(x)))*" ")
            print()
        print("  ",end = "")
        for y in range(self.width):
            #print(str(y)[-1],end = " ")
            #print(y,end = (3-len(str(y)))*"  ")
            print((2-len(str(y)))*" ",end = "")
            print(y,end = " ")
        print() # this is here to make sure we start on the next line
    def formGrid(self):
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append("*")
            self.gridList.append(row)            

    def getGrid(self):
        row = 0
        for x in self.gridList:
            print(row,end = " ")
            print((2-len(str(row)))*" ",end = "")
            for y in x:
                if y.__class__ == Enemy:
                    if len(str(row)) < 2:
                        print("E",end = (3-len(str(row)))*" ")
                    else:
                        print("E",end = (4-len(str(row)))*" ")
                elif y.__class__ == Weapon or y.__class__ == Shield:
                    if len(str(row)) < 2:
                        print("I",end = (3-len(str(row)))*" ")
                    else:
                        print("I",end = (4-len(str(row)))*" ")
                elif y == "S":
                    if len(str(row)) < 2:
                        print("S",end = (3-len(str(row)))*" ")
                    else:
                        print("S",end = (4-len(str(row)))*" ")
                else:
                    if len(str(row)) < 2:
                        print(y,end = (3-len(str(row)))*" ")
                    else:
                        print(y,end = (4-len(str(row)))*" ")
            print()
            row += 1
        print("  ",end = "")
        for y in range(len(self.gridList[0])):
            print((2-len(str(y)))*" ",end = "")
            print(y,end = " ")
        print() # this is here to makesure we start on the next line

    def returnGrid(self):
        return self.gridList
    def placeShipOnGrid(self):
        self.gridList[round(len(self.gridList)/2)][round(len(self.gridList[0])/2)] = "S"
    def placeEnemyOnGrid(self,enemy):
        randomX = random.randint(0,len(self.gridList[0])-1)
        randomY = random.randint(0,len(self.gridList)-1)
        if self.gridList[randomY][randomX] != "S":
            self.gridList[randomY][randomX] = enemy
    def removeEnemyOnGrid(self,enemy):
        for y in range(len(self.gridList)):
            for x in range(len(self.gridList[0])):
                if self.gridList[y][x] == enemy:
                           self.gridList[y][x] == "*"
                           
    def getCurrentVector(self):
        yValue = 0
        for y in self.gridList:
            xValue = 0
            for x in y:
                if x == "S":
                    return (str(xValue)+";"+str(yValue))
                xValue += 1
            yValue += 1
            
    def move(self,direction,distance):
        direction = direction.lower()
        location = self.getCurrentVector().split(";")
        xPos, yPos = int(location[0]),int(location[1])
        y2Pos, x2Pos = yPos, xPos
        self.gridList[yPos][xPos] = "*"
        if direction == "up" or direction == "u":
            y2Pos -= distance
        elif direction == "down" or direction == "d":
            y2Pos += distance
        elif direction == "right" or direction == "r":
            x2Pos += distance
        elif direction == "left" or direction == "l":
            x2Pos -= distance
        else:
            print("Command Syntax is incorrect")

        if (y2Pos >= 0 and y2Pos < len(self.gridList) and x2Pos >= 0 and x2Pos < len(self.gridList[0])) and self.gridList[y2Pos][x2Pos] == "*":
            self.gridList[y2Pos][x2Pos] = "S"
            self.gridList[yPos][xPos] = "*"
        else:
            self.gridList[yPos][xPos] = "S"
            print("Move is invalid")
            
    def goto(self,x,y):
        if isinstance(x,int) and isinstance(y,int):
            if (y >= len(self.gridList) or y < 0 or x >= len(self.gridList[0]) or x < 0) or self.gridList[y][x] != "*":
                print("Invalid location")
            else:
                location = self.getCurrentVector().split(";")
                xPos, yPos = int(location[0]), int(location[1])
                self.gridList[yPos][xPos] = "*"
                self.gridList[y][x] = "S"
        else:
            print("Invalid Input")
    def checkIfEnemyOnMap(self):
        for x in self.gridList:
            for y in x:
                if y.__class__ == Enemy:
                    return True
        return False
    def moveEnemy(self,direction,enemy):
        for y in range(len(self.gridList)):
            for x in range(len(self.gridList[0])):
                if self.gridList[y][x] == enemy:
                    newX, newY = curX, curY = x,y
                    
                    if direction == "l":
                        newX = curX - random.randint(1,curX)
                    elif direction == "r":
                        newX = curX + random.randint(1,5)
                    elif direction == "u":
                        newY = curY - random.randint(1,curY)
                    elif direction == "d":
                        newY = curY + random.randint(1,5)
                    try :
                        self.gridList[newY][newX] = enemy
                        self.gridList[curY][curX] = "*"
                    except IndexError:
                        pass
            

alf = Grid("Caph",15,30)
##alf.drawStarGrid()
##alf.formGrid()
##alf.placeShipOnGrid()
##alf.getGrid()
