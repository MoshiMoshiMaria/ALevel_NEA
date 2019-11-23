import random, time
class Shield:
    def __init__(self,
                 name,
                 hp,
                 mitigation,
                 ):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.mitigation = mitigation
        self.harmonic = random.randint(0,9) #If harmonic is the same as the opponents weapon harmonic, all mitigation is cancelled
#GETTERS
    def getName(self):
        return self.name
    def getHp(self):
        return round(self.hp,2)
    def getMitigation(self):
        return self.mitigation
    def getHarmonic(self):
        return self.harmonic
    def getPercent(self):
        if self.maxHp != 0:
            return round((self.hp/self.maxHp)*100,2)
        return "N/A"
#SETTERS
    def setName(self,value):
        self.name = value
    def setHp(self,value):
        self.hp = value
    def setMitigation(self,value):
        self.mitigation = value
    def setHarmonic(self,value):
        self.harmonic = value
    def regenShield(self):
        
        if self.hp == self.maxHp:
            print("Shields are already at max")
        else:
            if random.randint(1,10) == 1:#one in ten chance of full regen
                self.hp = self.maxHp
            else:
                self.hp += (self.maxHp/10)
                if self.hp > self.maxHp:
                    self.hp = self.maxHp

def createShield(factionChoice):
    high = ["Species 8472","Hirogen","Dominion","Romulan"]
    mid = ["Klingon","UFP","Ferengi","Allasomorph","Tellarite","Antaran","Nausicaan","Orion Pirates","Breen","Cardassian","Kazon"]
    low = ["Viidian","Bajoran","Aenar","Aaamazzarite","Acamarian","Akritirian","Ocampa","Horta","Berellian"]
    if factionChoice in high:
        alf = Shield("{} shield".format(factionChoice),random.randint(700,1000),random.randint(40,55))
    elif factionChoice in mid:
        alf = Shield("{} shield".format(factionChoice),random.randint(300,600),random.randint(20,35))
    elif factionChoice in low:
        alf = Shield("{} shield".format(factionChoice),random.randint(100,300),random.randint(0,15))
    else:
        alf = Shield("No shield",0,0)
    return alf
