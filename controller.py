import random, time, threading

##Controller controls elements of the Game class
##these values wiil be passed to the ship to help create its interactions with the world and its inhabitants
## also acts as the bridge between the user and the program. no longer wiill they have to type commands in python (thank god)

class Controller:
    def getAction(self):
        return input(">>> ")

    def sanitiseAction(self,action,commandDict,operandCounts):
        exceptions = ['show adjacent stars','repeat','change weapons','change weapon harmonic','change shield harmonic',
                      'find omega','lower shields', 'raise shields','self destruct','h','/h','/?','?','show system',
                      'cargo hold','change weapons','report','help']
        if action not in exceptions:
            parsed = action.split(" ")
            for x in range(len(parsed)):
                if x.__class__ == str:
                    parsed[x] = parsed[x].lower()
            if parsed[0] in commandDict and len(parsed[1:]) == operandCounts[parsed[0]]:
                if not parsed[1].isdigit():
                    if "_" in parsed[1]:
                        capitalised = ""
                        splitter = parsed[1].split("_")
                        for x in splitter:
                            capitalised += x.capitalize()
                            capitalised += "_"
                        capitalised = capitalised[0:-1]
                        parsed[1] = capitalised
                    else:
                        parsed[1] = parsed[1].capitalize()
                for x in range(len(parsed)):
                    if parsed[x].isdigit():
                        parsed[x] = int(parsed[x])
                return parsed
            else:
                print("Command syntax incorrect")
                return None

        else:
            return [action]
        #we can check if each word is in a set of lists
        #and which one, so we can capitalise where necessary, change it to a synonym if we have to
        #we will have to ensure there are no repeating commands/words in other lists or create a priority order

#create a dictionary like this:
    # commands = {'print': print}
#then we can take an input as a string and do this:
    #dave = input("FUNCTION >>> ")
    #FUNCTION >>> print
    # commands[dave]("12")
#commands[dave] = commands['print'] which the program
#recognises as print (the function) so commands[dave]("12")
#will produce print("12") which is 12
#this is how we can do in game commands

#to take string inputs as parameters, they have to be turned into a tuple
    #this is not enough. it must also be expanded using *
    # function(*tuple(listOfParameters))


#use a function to make sure parameters are in the correct format
#for example: capitalise the first letter of star names (code to do so is above)

## This is the new and improved threading-based implementation of enemies and battles
## this borrows ideas from threadingTest2.py
##class EnemyThread(threading.Thread):
##    def __init__(self,ship):
##        threading.Thread.__init__(self)
##        self.ship = ship
##        self.name = self.ship.getName()
##        self.stop = False
##        self.timer = 0
##    def action(self):
##        actions = ["attack"]
##        action = random.choice(actions)
##        if actions == 'attack':
##            wep = ""
##            while wep.__class__ != Weapon
##                wep = random.choice(self.ship.weapons)
##            return ['receiveDamage',wep]
##    def run(self):
##        while self.ship.getHull() > 0:
##            while self.timer < 10:
##                time.sleep(1)
##                self.timer += 1
##            self.timer = 0
##            
##    def stopThread(self):
##        self.stop = True
##
##may not use this method but it was designed to be a class that would manage
##        #enemyThreads and notify Game when it had to do things for the enemy
##class BattleThread(threading.Thread):
##    def __init__(self):
##        threading.Thread.__init__(self)
##        self.threads = {}
##        self.stop = False
##    def run(self):
##        while not self.stop:
##            for x in threads:
##                if x.timer == 10:
##                    return
##    def addThread(self,thread):
##        self.threads[thread.ship.name] = thread
##    def stopThread(self):
##        self.stop = True








##The thread idea is coming to a halt about its implementation
##changes made to gameMap in the class must be returned to a single variable
##so if the function takes gameMap everytime it is called and we don't put the objects into the class upon
    ##initialisation then it should work but it will take dedication - a lot of modifications to be made in game, controller

##class playerThread(threading.Thread): - look in playGame(game.py) this idea is pretty much dead but enemy thread is still going
##    """Pass an OBJ(Ship) into the thread"""
##    def __init__(self):
##        threading.Thread.__init__(self)
##        self.controller = Controller()
##    def checkAttributes(self):
##        print("Status")
##        print("Name: {}".format(self.name))
##        print("OBJ: {}".format(self.ship))
##        print("OBJ Name: {}".format(self.ship.getName()))
##        print("isAlive?: {}".format(self.isAlive()))
##    def run(self):
##        print("~~~STARTED~~~")
##        #this is where the player will give commands
##        while True:
##            action = self.controller.getAction()
##            self.controller.sanitiseAction(action)
##        print("~~~ENDED~~~")

## - Not doing it like this anymore -   
##class EnemyThread(threading.Thread):
##    def __init__(self,enemy,playerFaction,factionList):
##        self.enemy = enemy
##        threading.Thread.__init__(self)
##        self.playerFaction = playerFaction
##        self.factionList = factionList
##        self.stop = False
##
##    def attackChance(self):
##        attack = random.uniform(0,1)
##        if attack > 0.15:
##            return None
##
##    def run(self):
##        if not self.stop:               
##            self.enemy.updateShields()
##            self.enemy.checkHostile(self.playerFaction,self.factionList)
##            time.sleep(random.randint(3,10))
##
##    def stop(self):
##        self.stop = True
##
