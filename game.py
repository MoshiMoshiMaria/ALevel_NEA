#enemy drops
import random,time,sys,threading,os,math
from ship import Ship# import Ship class
from weapon import Weapon# import Weapon class
from shield import Shield# import Shield class
from enemy import Enemy# import Enemy
from controller import Controller# import Controller class#,EnemyThread - no longer exists
from mapFile import Map# import Map class


####IMPORTANT - MAKE A variable player to hold the player's OBJ(SHIP) and then use it in Grid.placeShipOnGrid instead of an "0"
            #   then just check it's a Ship class and then you have it place an s on the grid(Already implemented, just needs the player OBJ passed)

class Game:
    def __init__(self):
##THESE LINES JUST HOLD HARDCODED LISTS AND DICTS SO TO FIND OTHER ATTRS SCROLL DOWN FOR THE NEXT UNINDENTED COMMENT
        #list of classes with ships in them for the player to play
        #use the players faction as a DICT key to view the list of playable ships
        self.playerShips = {
            "UFP":[ #Could add the warship voyager
            Ship("Enterprise A","UFP",1000,Shield("Standard Issue Shield",150,12),[Weapon("Standard Phasers",100,"Energy"),Weapon("Photon Torpedo",150,"Antimatter")],100),
            Ship("Enterprise B","UFP",1400,Shield("Standard Issue Shield",300,24),[Weapon("Standard Phasers",140,"Energy"),Weapon("Photon Torpedo",190,"Antimatter")],125),
            Ship("Enterprise C","UFP",1750,Shield("Standard Issue Shield",450,36),[Weapon("Standard Phasers",180,"Energy"),Weapon("Photon Torpedo",230,"Antimatter")],200),
            Ship("Enterprise D","UFP",2000,Shield("Standard Issue Shield",600,48),[Weapon("Standard Phasers",215,"Energy"),Weapon("Photon Torpedo",255,"Antimatter")],220),
            Ship("Enterprise E","UFP",3200,Shield("Standard Issue Shield",900,60),[Weapon("Standard Phasers",280,"Energy"),Weapon("Photon Torpedo",320,"Antimatter"),
                                                                                    Weapon("Quantum Torpedo",570,"Special")],260),
            Ship("Voyager","UFP",2200,Shield("Standard Issues Shield",650,32),[Weapon("Standard Phasers",245,"Energy"),Weapon("Photon Torpedo",260,"Antimatter")],200),
            Ship("Defiant","UFP",3000,Shield("Standard Issues Shield",900,60),[Weapon("Pulse Phasers",250,"Energy"),Weapon("Photon Torpedo",320,"Antimatter"),
                                                                                    Weapon("Quantum Torpedo",570,"Special")],200),
            Ship("Polaris","UFP",4000,Shield("Standard Issues Shield",1100,60),[Weapon("Standard Phasers",280,"Energy"),Weapon("Photon Torpedo",350,"Antimatter"),
                                                                                    Weapon("Quantum Torpedo",630,"Special")],250)
            ],
            "Cardassian":[
            Ship("Galor Class","Cardassian",1800,Shield("Standard Shield",550,22),[Weapon("Phaser Array",200,"Energy"),Weapon("Antimatter Torpedo",245,"Antimatter")],200),
            Ship("Hideki Class","Cardassian",1400,Shield("Standard Shield",250,15),[Weapon("Phaser Array",150,"Energy"),Weapon("Antimatter Torpedo",230,"Antimatter")],140),
            Ship("Kutet Class","Cardassian",2200,Shield("Standard Shield",900,30),[Weapon("Phasr Array",340,"Energy"),Weapon("Antimatter Torpedo",270,"Antimatter")],250),
            ],
            "Klingon":
            [
            Ship("B'rel","Klingon",1200,Shield("Standard Shield",250,26),[Weapon("Disruptors",135,"Energy"),Weapon("Photon Torpedo",245,"Antimatter")],100),
            Ship("Vor'cha","Klingon",1600,Shield("Standard Shield",400,26),[Weapon("Disruptors",180,"Energy"),Weapon("Photon Torpedo",300,"Antimatter")],150),
            Ship("K'vort","Klingon",2000,Shield("Standard Shield",550,32),[Weapon("Disruptors",215,"Energy"),Weapon("Photon Torpedo",330,"Antimatter")],175),
            Ship("Negh'Var","Klingon",2400,Shield("Standard Shield",700,38),[Weapon("Disruptors",260,"Energy"),Weapon("Photon Torpedo",360,"Antimatter")],200),
            Ship("Sword of Kahless","Klingon",3000,Shield("Standard Shield",900,50),[Weapon("Disruptors",300,"Energy"),Weapon("Photon Torpedo",400,"Antimatter")],250)
            ],
            "Romulan":
            [
            Ship("D7 Class","Romulan",1250,Shield("Standard Shield",300,20),[Weapon("Tri-Phasic Emitters",180,"Energy"),Weapon("Plasma Torpedo",245,"Plasma")],110),
            Ship("Valdore","Romulan",2000,Shield("Standard Shield",500,38),[Weapon("Tri-Phasic Emitters",225,"Energy"),Weapon("Plasma Torpedo",300,"Plasma")],250),
            Ship("D'deridex","Romulan",2500,Shield("Standard Shield",800,56),[Weapon("Tri-Phasic Emitters",270,"Energy"),Weapon("Plasma Torpedo",360,"Plasma")],250),
            Ship("Scimitar","Romulan",3600,Shield("Standard Shield",1100,73),[Weapon("Tri-Phasic Emitters",330,"Energy"),Weapon("Plasma Torpedo",400,"Plasma"),
                                                                             Weapon("Thalaron Pulse",700,"Special")],250)
            ],
            "Dominion":[
            Ship("Jem'Hadar Cruiser","Dominion",1250,Shield("Polaron Shield",300,20),[Weapon("Phased Polaron Beam",180,"Polaron"),Weapon("Polaron Torpedo",245,"Polaron")],110),
            Ship("Chimera Battlecruiser","Dominion",2200,Shield("Polaron Shield",700,30),[Weapon("Phased Polaron Beam",250,"Polaron"),Weapon("Polaron Torpedo",260,"Polaron")],110),
            Ship("Hydra Dreadnought","Dominion",3000,Shield("Polaron Shield",700,40),[Weapon("Phased Polaron Beam",320,"Polaron"),Weapon("Polaron Torpedo",280,"Polaron")],110)
            ],
            "Borg":[
            Ship("Borg Sphere","Borg",2500,Shield("No Shield",0,0),[Weapon("Borg Cutting Beam",300,"Energy"),Weapon("Shield Drain Torpedo",400,"Drain")],100),
            Ship("Borg Cube","Borg",5000,Shield("No Shield",0,0),[Weapon("Borg Cutting Beam",700,"Energy"),Weapon("Shield Drain Torpedo",800,"Drain")],150),
            Ship("Borg Diamond","Borg",3300,Shield("No Shield",0,0),[Weapon("Borg Cutting Beam",500,"Energy"),Weapon("Shield Drain Torpedo",600,"Drain")],125),
            Ship("Progenitor","Borg",92000,Shield("No Shield",0,0),[Weapon("Borg Cutting Beam",20000,"Energy"),Weapon("Ragnarok Torpedo",50000,"Dark Matter"),
                                                                    Weapon("Reaper Beam",90000,"Polaron")],500)
            ]                                                       #Reaper beam is not actually Polaron based, just needs it here to bypass shields
            }

        #The Keys in this list also double up as the playable factions
        #as well as the keys in playerShips
        self.alliances = {
            "UFP":"UFP;Bajoran;",
            "Klingon":"Klingon;",
            "Cardassian":"Cardassian;Dominion;",
            "Dominion":"Dominion;Cardassian;Breen;",
            "Romulan":"",
            "Borg":""
            }
        #These will be possible factions for other ships
        self.factions = [
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
            "Nausicaans",
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
            "Viidians"
            ]
## THIS IS WHERE OTHER ATTRS WILL BE STORED SUCH AS THE PLAYER AND MAP OBJECTS
        self.player = self.setupPlayer() # sets up the player object
        self.setupGame() # sets up the game difficulty and creates the gameMap
        self.lastAction = None # a variable to hold the last action the player performed
        self.activeShips = {}#holds dict of active Enemy objects as {name STR:OBJ(Enemy)}
        self.enemyThreads = []
        
    def setupPlayer(self):
        print("Choose a faction:") ##allows player to choose faction
        listed = []
        for x in self.playerShips:
            listed.append(x)
        for x in listed:
            print("{}: {}".format(listed.index(x),x))
        choice = input(">>> ")
        while choice.isdigit() == False or int(choice) < 0 or int(choice) > len(listed)-1:
            print("Choose a valid option")
            choice = input(">>> ")
        choice = listed[int(choice)]

        print("Choose a ship:") ## allows player to choose their ship
        listed = []
        for x in self.playerShips[choice]:
            listed.append(x)
        for x in listed:
            print("{}: {}".format(listed.index(x),x.getName()))
        choice = input(">>> ")
        while choice.isdigit() == False or int(choice) > len(listed)-1 or int(choice) < 0:
            print("Choose a valid option")
            choice = input(">>> ")

        player = listed[int(choice)]
        if player.faction == "Borg":
            if player.name == "Borg Sphere":
                print("Would you like a Tactical Sphere or 7of9 refit?")
                option = input("0: No\n1: Tactical Sphere\n2: 7of9\n>>> ")
            elif player.name == "Borg Cube":
                print("Would you like a Tactical Cube or Locutus refit?")
                option = input("0: No\n1: Tactical Cube\n2: Locutus\n>>> ")
            elif player.name == "Borg Diamond":
                print("Would you like a Borg Queen refit?")
                option = input("0: No\n1: Yes\n>>> ")

            if player.name != "Borg Diamond" and player.name !="Progenitor":
                if option == "1":
                    player.hull *= 1.3
                    player.shield.hp *= 1.3
                    for x in player.weapons:
                        if x.__class__ == Weapon:
                            x.damage *= 1.3
                elif option == "2":
                    player.hull *= 1.6
                    player.shield.hp *= 1.6
                    for x in player.weapons:
                        x.damage *= 1.6
            elif player.name != "Progenitor":
                if option == "1":
                    player.hull *= 1.6
                    player.shield.hp *= 1.6
                    for x in player.weapons:
                        if x.__class__ == Weapon:
                            x.damage *= 1.6
        
        return player

    def setupGame(self):
        self.gameController = Controller() #create a controller
        self.difficulty = self.chooseDifficulty() #get user to choose difficulty
        self.gameMap = gameMap = Map(self.difficulty) #create a map
    def chooseDifficulty(self):
        print("Choose a difficulty:")
        print("0: Walk through the park")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        print("4: Literally Impossible")
        choice = input("Choice: ")
        valid = ["0","1","2","3","4","709301"]
        while choice not in valid:
            print("Choose a valid option")
            choice = input("Choice: ")
        #Doesn't do anything yet
        if int(choice) == 0: # return difficulty multipliers - enemy hp, damage,etc will all be multiplied by this number
            return 0.25
        if int(choice) == 1:
            return 0.70
        if int(choice) == 2:
            return 1
        if int(choice) == 3:
            return 1.4
        if int(choice) ==4:
            return 2.2
        if int(choice) == 709301:
            os.system("echo -------------------START SESSION-------------------- >> inputanderrorlog.txt")
            return "dev"
    def checkIfEnemyOnMap(self):
        return self.gameMap.checkIfEnemyOnMap()# returns True if there is
    #use threadingTest2.py to give insight into how battles should be done
        #for now, battles are turn based
    def updateActiveShips(self):
        self.activeShips = {}
        if self.checkIfEnemyOnMap():
            for y in range(len(self.gameMap.currentGrid.gridList)):
                for x in range(len(self.gameMap.currentGrid.gridList[0])):
                    if self.gameMap.currentGrid.gridList[y][x].__class__ == Enemy:
                        ship = self.gameMap.currentGrid.gridList[y][x]
                        self.activeShips[ship.getName()] = ship
    def removeDead(self):
        for y in range(len(self.gameMap.currentGrid.gridList)):
                for x in range(len(self.gameMap.currentGrid.gridList[0])):
                    if self.gameMap.currentGrid.gridList[y][x].__class__ == Enemy and self.gameMap.currentGrid.gridList[y][x].getHull() != "*" and self.gameMap.currentGrid.gridList[y][x].getHull() <= 0:
                        item = self.gameMap.currentGrid.gridList[y][x].dropItem()
                        if item == None:
                            self.gameMap.currentGrid.gridList[y][x] = "*"
                        else:
                            self.gameMap.currentGrid.gridList[y][x] = item
    def enemyTurn(self):
        for x in self.activeShips:
            currentEnemy = self.activeShips[x]
            if currentEnemy.isAlive() and (currentEnemy.checkHostile(self.player.faction,self.alliances) or currentEnemy.isHostile()):
                if self.gameMap.enemyCheckDistance(currentEnemy) < 5:
                    self.playerReceiveDamage(currentEnemy)
                else:
                    playerLocation = self.gameMap.currentGrid.getCurrentVector().split(";")
                    playX,playY = int(playerLocation[0]),int(playerLocation[1])
                    def enemyLocation(enemy):
                        for y in range(len(self.gameMap.currentGrid.gridList)):
                            for x in range(len(self.gameMap.currentGrid.gridList[0])):
                                if self.gameMap.currentGrid.gridList[y][x] == enemy:
                                    return x,y                
                    
                    enemyX, enemyY = enemyLocation(currentEnemy)
                    if playX < enemyX:
                        self.gameMap.moveEnemy("l",currentEnemy)
                    elif playX > enemyX:
                        self.gameMap.moveEnemy("r",currentEnemy)
                    if playY < enemyY:
                        self.gameMap.moveEnemy("u",currentEnemy)
                    elif playY > enemyY:
                        self.gameMap.moveEnemy("d",currentEnemy)
                        
    def checkEnemies(self):
        self.removeDead()# take all dead enemies off the board
        self.updateActiveShips()# update the list of ships that will have a turn
        self.enemyTurn()# let the ships on the board actually take a turn
        #print(self.activeShips)# testing the list of active ships

    def playerReceiveDamage(self,enemy):
        wep = None
        while wep.__class__ != Weapon:
            wep = random.choice(enemy.weapons)
        self.player.receiveDamage(wep)
    def playerIsAlive(self):
        return self.player.getHull() > 0
    def checkWin(self):
        if self.gameMap.checkOmega() and not self.gameMap.checkIfEnemyOnMap():
            return True
        return False
    def setWeaponHarmonic(self):
        for x in range(len(self.player.weapons)):
            if self.player.weapons[x].__class__ == Weapon:
                print("{}: {}".format(x,self.player.weapons[x].getName()))
            else:
                print("{}: {}".format(x,self.player.weapons[x]))
        choice = input("Which weapon?: ")
        while not choice.isdigit() or choice < 0 or choice > len(self.player.weapons):
            print("Invalid Option")
            choice =  input("Which weapon?: ")
        choice = int(choice)
        self.player.weapons[choice].setHarmonic(input("Set harmonic to: "))
    def setShieldHarmonic(self):
        self.player.shield.setHarmonic(input("Set harmonic to: "))
    def scan(self,x,y):
        if self.gameMap.currentGrid.gridList[y][x].__class__ == Enemy:
            self.gameMap.currentGrid.gridList[y][x].displayScanInfo()
        else:
            print("\nThere is no target there...")

    def attackEnemy(self,x,y):
        try:
            if self.gameMap.currentGrid.gridList[y][x].__class__ == Enemy:
                if self.gameMap.checkDistance(x,y) < 5:
                    attack = self.player.chooseAttack()
                    self.gameMap.currentGrid.gridList[y][x].receiveDamage(attack)
                    if attack.getBase() == "Special":
                        self.player.antimatter -= random.randint(20,50)
                    if self.gameMap.currentGrid.gridList[y][x].hull <= 0:
                        self.gameMap.removeEnemyOnGrid(self.gameMap.currentGrid.gridList[y][x])
                else:
                    print("\nTarget is out of range.")
            else:
                print("There is no target there...")
        except IndexError:
            print("That is an invalid location...")
    def pickUpItem(self,x,y):
        space = self.gameMap.currentGrid.gridList[y][x]
        if space.__class__ != Enemy and space != "*":
            self.player.addToCargoHold(space)
            self.gameMap.currentGrid.gridList[y][x] = "*"
        else:
            print("There is nothing there...")
    def findOmega(self):
        if self.gameMap.checkOmega():
            print("\nThe Omega Particle is in this system!")
        else:
            print("\nThe Omega Particle is {} jumps away.".format(self.gameMap.distanceFromOmega()))
    def checkDistance(self,x,y):
        print(self.gameMap.checkDistance(x,y))
    def getAction(self):
        commandDict = {'warp':self.gameMap.warp,
                       'attack':self.attackEnemy,
                       'show adjacent stars':self.gameMap.getCurrentAdjacencies,
                       'goto':self.gameMap.goto,
                       'move':self.gameMap.move,
                       'raise shields':self.player.raiseShields,
                       'lower shields':self.player.lowerShields,
                       'change weapons':self.player.setActiveWeapons,
                       'self destruct':self.player.selfDestruct,
                       'find omega':self.findOmega,
                       'change weapon harmonic':self.setWeaponHarmonic,
                       'change shield harmonic':self.setShieldHarmonic,
                       "scan":self.scan,
                       'range':self.checkDistance,
                       'h':self.help,
                       '/h':self.help,
                       '?':self.help,
                       '/?:':self.help,
                       'help':self.help,
                       'show system':self.gameMap.displaySystem,
                       'cargo hold':self.player.showCargoHold,
                       'change weapons':self.player.setActiveWeapons,
                       'report':self.player.printAll
                       }
        operandCounts = {'warp':2,
                         'attack':2,
                         'show adjacent stars': 0,
                         'goto': 2,
                         'move': 2,
                         'raise shields':0,
                         'lower shields':0,
                         'repeat':0,
                         'change weapons':0,
                         'find omega':0,
                         'change weapon harmonic': 0,
                         'change shield harmonic': 0,
                         'scan':2,
                         'range':2,
                         'h':0,
                         '/h':0,
                         '?':0,
                         '/?':0,
                         'help':0,
                         'show system':0,
                         'cargo hold':0,
                         'changeWeapons':0,
                         'report':0,
                         }
        action = self.gameController.getAction()
        action = self.gameController.sanitiseAction(action,commandDict,operandCounts)
        if self.difficulty == "dev":
            os.system("echo Date: {0}; Time: {1}; Action:{2} >> inputAndErrorLog.txt".format(str(time.localtime()[0])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[2]),str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5]),action)) 
        try: #Tested on warp and attack - both worked, just expand the command list and make necessary adjustments to sanitiseAction()(in controller.py)
            if action[0] != 'repeat':
                self.lastAction = action

            if action[0] == 'repeat':
                commandDict[self.lastAction[0]](*tuple(self.lastAction[1:]))               
            else:
                commandDict[action[0]](*tuple(action[1:]))
        except Exception as e:
            print("I cannot do that, Captain.")
            #print(e)#hash after testing
            if self.difficulty == "dev":
                os.system("echo Date: {0}; Time: {1}; Error: {2} >> inputAndErrorLog.txt".format(str(time.localtime()[0])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[2]),str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5]),e))
    def help(self):
        import os
        os.system("notepad.exe .commands.txt")
    def checkTwoLists(self,list1,list2):
        if len(list1) == len(list2):
            for x in range(len(list1)):
                if list1[x] != list2[x]:
                    return False
        return True

    def flavourText(self):
        filename = self.player.faction.lower()+".bat"
        os.system("cd flavourText && start {}".format(filename))
    def playGame(self):
        gameInAction = True
        self.flavourText()
        input("\t\tPress enter to begin\n")
        self.gameMap.displaySystem()
        while gameInAction:
            if not self.playerIsAlive():
                gameInAction = False
                break
            temp_currentStar = self.gameMap.currentLocation
            temp_currentGrid = self.gameMap.currentGrid.gridList
            self.getAction()
            self.checkEnemies()
            if self.checkTwoLists(temp_currentGrid,self.gameMap.currentGrid.gridList) == False or temp_currentStar != self.gameMap.currentLocation:#doesn't work for some reason
                self.gameMap.displaySystem()
            if self.checkWin():
                self.gameInAction = False
        if self.checkWin():
            os.system("cd flavourText & start {}Win.bat".format(self.player.faction.lower()))
        else:
            os.system("cd flavourText & start {}Loss.bat".format(self.player.faction.lower()))
        if self.difficulty == "dev":
            os.system("echo --------------------END SESSION-------------------- >> inputanderrorlog.txt")
            os.system("notepad.exe InputAndErrorLog.txt")
        if self.difficulty != "dev":
            print("Thanks for playing!")
            input("Enter to exit...")
            print("Exiting...")
            time.sleep(2)

if __name__ == '__main__':
    game = Game() # includes methods setupPlayer() and setupGame() in __init__
    game.playGame()
    sys.exit()

def tAll(): #test-all function
    g = Game() #setup game
    g.playGame() #start game
    m = g.gameMap #give gameMap a variable so it can be returned
    print("Finish") #tell user it has finished
    return g,m #return game class "g" and map class "m" so attributes can be exanimed
#g,m = tAll() # actually run the function
    


