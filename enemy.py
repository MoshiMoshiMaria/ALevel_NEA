import random, time
from ship import Ship
from weapon import Weapon,createWeapon
from shield import Shield,createShield

class Enemy(Ship):
    def __init__(self,name,
                 faction,
                 hull,
                 shield,
                 weapons):
        Ship.__init__(self,name,faction,hull,shield,weapons,200)
        self.hostile = False
        for x in self.weapons:
            if x == "Empty":
                self.weapons.remove(x)
    def updateShields(self):
        if self.hull < self.maxHull:
            self.shieldState = True
        else:
            self.shieldState = False
    def receiveDamage(self,weapon):
        super(Enemy,self).receiveDamage(weapon)
        self.hostile = True
        self.raiseShields()
    def checkHostile(self,playerFaction,factionList):
        if self.faction+";" in factionList[playerFaction]:
            return False
        return True
    def isHostile(self):
        return self.hostile
    def displayScanInfo(self):
        self.printAll()#function in ship, it was made at the start to check attributes of the Ship objects, guess i can use it for this though

    def dropItem(self):
        chance = random.randint(1,15)
        if chance == 1 or chance == 2:
            item = createWeapon(self.faction)
            item.damage *= round(random.uniform(1,1.5),2)
            return item
        else:
            return None

def createEnemy(factionChoice):
    s = createShield(factionChoice)
    w1,w2 = createWeapon(factionChoice)
    shipNames = {"Borg":["Borg Cube","Borg Sphere","Borg Diamond","Borg Pyramid"],
                 "Dominion":["Jem'Hadar Cruiser","Dominion Battlecruiser"],
                 "Klingon":["B'rel Class","K'vort Class","Korotinga Class","D7 Class"],
                 "Species 8472":["Bioship","Damaged Bioship"],
                 "Ferengi":["Ferengi Marauder"],
                 "Romulan":["D'deridex Warship","D7 Class","Taravore Warbird"],
                 "Cardassian":["Galor Class","Hideki Class"],
                 "UFP":["Galaxy Class","Excelsior Class",
                        "Ambassador Class","Miranda Class",
                        "Vulcan Science Vessel","Cargo Vessel"],
        }
    high = ["Species 8472","Hirogen","Dominion","Romulan","Borg"]
    mid = ["Klingon","UFP","Ferengi","Allasomorph","Tellarite","Antaran","Nausicaan","Orion Pirates","Breen","Cardassian","Kazon"]
    low = ["Viidian","Bajoran","Aenar","Aaamazzarite","Acamarian","Akritirian","Ocampa","Horta","Berellian","Tholian"]
    if factionChoice in high:
        hull = random.randint(2000,2600)
    elif factionChoice in mid:
        hull = random.randint(1300,1900)
    elif factionChoice in low:
        hull = random.randint(800,1200)
    if factionChoice in shipNames:
        nameChoice = random.choice(shipNames[factionChoice])
        alf = Enemy(nameChoice,factionChoice,hull,s,[w1,w2])
    else:
        alf = Enemy("{} ship".format(factionChoice),factionChoice,hull,s,[w1,w2])
    return alf
    





#----------TESTS----------#
#from enemy import Enemy
#from ship import Ship, voy
##nx = Enemy("Enterprise NX","UFP",1500,voy.shield,voy.weapons)
##
weyWep1 = Weapon("Phased Polaron Beam",213,"Polaron")
weyWep2 = Weapon("Polaron Torpedo",297,"Polaron")
weyShield = Shield("Polaron Shield",1000,12)
weyoun = Enemy("Hydra Battlecruiser","Dominion",4000,weyShield,[weyWep1,weyWep2])
##
##
##def fightNX():
##    voy.raiseShields()
##    while voy.alive and nx.alive:
##        choice = random.randint(0,1)
##        nx.receiveDamage(voy.weapons[choice])
##        voy.receiveDamage(nx.weapons[choice])
##        nx.updateShields()
##        
##    if voy.alive:
##        print("Voy won")
##    else:
##        print("NX won")
##
##def fightWey():
##    voy.raiseShields()
##    while voy.alive and weyoun.alive:
##        choice = random.randint(0,1)
##        weyoun.receiveDamage(voy.weapons[choice])
##        voy.receiveDamage(weyoun.weapons[choice])
##        weyoun.updateShields()
##    if voy.alive:
##        print("Voy won")
##    else:
##        print("Weyoun won")
##
##def nxAndVoyVsWeyoun():
##    while (voy.alive or nx.alive) and weyoun.alive:
##        if voy.hull > 0 and nx.hull > 0:
##            weyoun.receiveDamage(voy.weapons[random.randint(0,1)])
##            weyoun.receiveDamage(nx.weapons[random.randint(0,1)])
##            attack = random.choice([voy,nx])
##            attack.receiveDamage(weyoun.weapons[random.randint(0,1)])
##        elif voy.alive and not nx.alive:
##            weyoun.receiveDamage(voy.weapons[random.randint(0,1)])
##            voy.receiveDamage(weyoun.weapons[random.randint(0,1)])
##
##        elif not voy.alive and nx.alive:
##            weyoun.receiveDamage(nx.weapons[random.randint(0,1)])
##            nx.receiveDamage(weyoun.weapons[random.randint(0,1)])
##
##    if weyoun.alive:
##        print("Weyoun won")
##    else:
##        print("NX and Voy Won")
