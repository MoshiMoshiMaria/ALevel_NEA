import random, time
class Weapon:
    def __init__(self,
                 name,
                 damage,
                 base
                 ):
        self.name = name
        self.damage = damage
        self.base = base
        self.harmonic = random.randint(0,9) #If harmonic is the same as the opponents shield harmonic, all mitigation is cancelled
#GETTERS
    def getName(self):
        return self.name
    def getDamage(self):
        return self.damage
    def getBase(self):
        return self.base
    def getHarmonic(self):
        return self.harmonic
#SETTERS
    def setName(self,value):
        self.name = value
    def setDamage(self,value):
        self.damage = value
    def setBase(self,value):
        self.base = value
    def setHarmonic(self,value):
        self.harmonic = value

def createWeapon(factionChoice):
    high = ["Species 8472","Hirogen","Dominion","Romulan","Borg"]
    mid = ["Klingon","UFP","Ferengi","Allasomorph","Tellarite","Antaran","Nausicaan","Orion Pirates","Breen","Cardassian","Kazon"]
    low = ["Viidian","Bajoran","Aenar","Aaamazzarite","Acamarian","Akritirian","Ocampa","Horta","Berellian"]
    if factionChoice == "Dominion":
        base = base2 = "Polaron"
    else:
        base,base2 = "Energy","Antimatter"
    if factionChoice in high: # Get the faction and change the names accordingly ie DICT{'Romulan':'triphasic emitters'}
        alf = Weapon("{} phasers".format(factionChoice),random.randint(250,300),base)
        dav = Weapon("{} torpedo".format(factionChoice),random.randint(270,320),base2)
    elif factionChoice in mid:
        alf = Weapon("{} phasers".format(factionChoice),random.randint(180,230),base)
        dav = Weapon("{} torpedo".format(factionChoice),random.randint(210,240),base2)
    elif factionChoice in low:
        alf = Weapon("{} phasers".format(factionChoice),random.randint(130,170),base)
        dav = Weapon("{} torpedo".format(factionChoice),random.randint(150,200),base2)
    return alf,dav
