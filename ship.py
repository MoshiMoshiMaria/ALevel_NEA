import random, time
from weapon import Weapon
from shield import Shield

class Ship:
    """name STR, fact STR, hull INT,shield OBJ(shield),weapons LIST of OBJ(weapons), AntiM INT,crew DICT"""
    def __init__(self,
                 name,
                 faction,
                 hull,
                 shield,
                 weapons,
                 antimatter
                 #crew #see self.crew = crew below for explanation
                 ):
#BASIC ATTRIBUTES
        self.alive = True
        self.name = name
        self.faction = faction
        self.hull, self.maxHull = hull,hull
        self.shield = shield
        self.shieldState = False
        self.weapons = weapons
        self.weaponSlots = len(weapons)+random.randint(1,2)
        while len(self.weapons) < self.weaponSlots:
            self.weapons.append("Empty")
        self.antimatter = antimatter # antimatter used for special weapons
        self.cargoHold = []
        self.maxCargoHold = random.randint(6,16)
        while len(self.cargoHold) < self.maxCargoHold:
                self.cargoHold.append("Empty")
        #self.crew = crew #extension goal of crew death leading to areas becoming less effective
    
#GETTERS        
    def printAll(self):
        shields = "Lowered"
        if self.shieldState:
            shields = "Raised"
        print("____________________")
        print("Name: {}".format(self.name))
        print("Faction: {}".format(self.faction))
        print("Hull: {}".format(self.hull))
        print("Shield: {}, {}{}, {}".format(self.shield.getName(),self.shield.getPercent(),"%",shields))
        print("Weapons:")
        for x in self.weapons:
            if x.__class__ == Weapon:
                print("\t{}, Avg Damage: {}, {} Based".format(x.getName(),x.getDamage(),x.getBase()))
            else:
                print("\t"+x)
        print("Antimatter: {}".format(self.antimatter))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")#i think this is called a macron (the "overscore")

    def getName(self):
        return self.name
    def getFaction(self):
        return self.faction
    def getShield(self):
        """"This will return an OBJ(shield)"""
        return self.shield
    def getWeapons(self):
        """This will return a list of OBJ(weapon), use appropriate methods on each item"""
        return self.weapons
    def printWeapons(self):
        print("______________________")
        for x in self.weapons:
            if x.__class__ == Weapon:
                print("Name: {0}\nDamage: {1}\nBase: {2}".format(x.getName(),x.getDamage(),x.getBase()))
                print()
            else:
                print("Empty Slot")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    def getHull(self):
        return self.hull
    def getAntimatter(self):
        return self.antimatter
    #def getCrew(self):
     #   return self.crew
    def isAlive(self):
        return self.alive
#SETTERS
    def setHull(self,value):
        self.hull = value
    def setShield(self,value):
        """value must be and OBJ(shield)"""
        self.shield = value
    def setAntimatter(self,value):
        self.anitmatter = value
    #def setCrew(self,value):
     #   self.crew = value
    def raiseShields(self):
        if not self.shieldState:
            if self.__class__ == Ship:
                print("Raising shields")
        else:
            if self.__class__ == Ship:
                print("Shields are raised")
        self.shieldState = True
    def lowerShields(self):
        if self.shieldState:
            print("Lowering shields")
        else:
            print("Shields are lowered")
        self.shieldState = False
    def addToCargoHold(self,value):
        if "Empty" in self.cargoHold:
            self.cargoHold[self.cargoHold.index("Empty")] = value
        else:
            print("There's no room for that")
    def dropFromCargoHold(self):
        for x in range(len(self.cargoHold)):
            if self.cargoHold[x].__class__ == Weapon or self.cargoHold.__class__ == Shield:
                print("{}: {}".format(x,self.cargoHold[x].getName()))
            else:
                print("{}: {}".format(x,self.cargoHold[x]))
        try:
            self.cargoHold[int(input("Remove which item?: "))] = "Empty"
        except: # Just catch everything as this could raise a number of errors such as IndexError and ValueError
            print("Invalid Selection")
    def showCargoHold(self):
        print("_____________________")
        print("Cargo Hold: ")
        for x in range(len(self.cargoHold)):
            if self.cargoHold[x].__class__ == Weapon or self.cargoHold[x].__class__ == Shield:
                print("{}: {}".format(x,self.cargoHold[x].getName()))
            else:
                print("{}: {}".format(x,self.cargoHold[x]))
        print("Antimatter: {}".format(self.antimatter))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    def changeShield(self):
        shieldsInCargo = []
        counter = 0
        for x in range(len(self.cargoHold)):
            if self.cargoHold[x].__class__ == Shield:
                print("{}: {}".format(counter,self.cargoHold[x].getName()))
                shieldsInCargo.append(self.cargoHold[x])
                counter += 1
        try:
            choice = int(input("Replace with what?: "))
            oldShield = self.shield
            newShield = shieldsInCargo[choice]
            self.cargoHold[self.cargoHold.index(newShield)] = oldShield
            self.shield = newShield
        except: # Just catch everything as this could raise a number of errors such as IndexError and ValueError
            print("Invalid Selection")

    def chooseAttack(self):
        def displayChoices():
            print("____________________")
            for x in range(len(self.weapons)):
                if self.weapons[x].__class__ == Weapon:
                    print("{}: {}".format(x,self.weapons[x].getName()))
                else:
                    print("{}: {}".format(x,self.weapons[x]))
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        def makeChoice():
            fire = input("Which weapon do you wish to fire?: ")
            while not fire.isdigit():
                print("Choice must be an INTEGER")
                fire = input("Which weapon do you wish to fire?: ")
            fire = int(fire)
            try:
                if self.weapons[fire] == "Empty":
                    print("There is no weapon in that slot")
                    return makeChoice()
                return self.weapons[fire]
            except IndexError:
                      print("Invalid Selection")
                      return makeChoice()
        displayChoices()
        return makeChoice()
        
        
    def setActiveWeapons(self):
        weaponNames = []
        for x in self.weapons:
            weaponNames.append(x.getName())
        print("____________________")
        for x in weaponNames:
            print("{}:{}".format(weaponNames.index(x),x))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        change = input("Which weapon do you wish to change?: ")
        while not change.isdigit():
            print("Choice must be an INTEGER")
            change = input("Which weapon do you wish to change?: ")
        change = int(change)
        if change < 0 or change >= len(weaponNames):
            print("Weapon not attached.")
        else:
            print("____________________")
            count = [0]
            choices = []
            for y in self.cargoHold:
                if y.__class__ == Weapon:
                    print("{}:{}".format(count[-1],y.getName()))
                    choices.append(y)
                    count.append(count[-1] + 1)
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            choice = input("Which do you wish to replace it with?: ")
            while not choice.isdigit():
                print("Choice must be an INTEGER")
                choice = input("Which do you wish to replace it with?: ")
            choice = int(choice)
            if choice in count and y.__class__ == Weapon:
                toRemove = self.weapons[change]
                self.weapons[change] = self.cargoHold[self.cargoHold.index(choices[choice])]
                self.cargoHold[self.cargoHold.index(choices[choice])] = toRemove
            else:
                print("Weapon not in cargo hold.")
    def receiveDamage(self,weapon):
        if weapon.__class__ == Weapon:
            """weapon OBJ(weapon)"""
            damage = round(random.uniform(weapon.getDamage()*0.8,weapon.getDamage()*1.2),2)
            if (self.shield.getHp() > 0 and self.shield.getHarmonic() != weapon.getHarmonic() and self.shieldState == True and weapon.getBase() != "Polaron") or weapon.getBase() == "Drain":
                if weapon.getBase() != "Drain":
                    self.shield.setHp( self.shield.getHp()-(damage*(1-(self.shield.getMitigation()/100))) )
                    print("\n{} took {} damage to its shields".format(self.name,(damage*(1-(self.shield.getMitigation()/100)))))
                else:
                    self.shield.setHp( self.shield.getHp()-weapon.getDamage() )
                    print("\n{} had {} health drained from its shields".format(self.name,damage))
            elif (self.shield.getHp() <= 0) or (self.shield.getHarmonic() == weapon.getHarmonic()) or (self.shieldState == False) or (weapon.getBase() == "Polaron"):
                self.setHull(self.getHull()-damage)
                print("\n{} took {} damage to its hull".format(self.name,damage))
            if self.hull <= 0:
                print("\n{} has been destroyed...".format(self.name))
                self.alive = False
        else:
            pass
    def selfDestruct(self):
        print("Self destruct activated! This process is not reversible!")
        timer = 10
        while timer > 0:
            print("Warp core breach in {} seconds.".format(timer))
            time.sleep(1)
            timer-=1
        self.hull = 0
        



def testShip():
    alf = Shield("Standard Shield",500,12)
    w1 = Weapon("Standard Issue Phaser Array",132,"Directed Energy")
    w2 = Weapon("Standard Issue Photon Torpedoes",179,"Antimatter")
    ship = Ship("VOY","UFP",2000,alf,[w1,w2],200)
    ship.addToCargoHold(ship.weapons[0])
    ship.addToCargoHold(ship.weapons[1])
    return ship
voy = testShip()
