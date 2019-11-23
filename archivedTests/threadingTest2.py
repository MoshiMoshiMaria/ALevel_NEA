#testing the threading for fights - to see if it's viable
##~~CONCLUSION~~##
"""
Build the threading module into controller.py and create a Controller
for the player inside it to get actions and deal with them
Enemies get their own thread.
Enemies that get created are kept track of when they should be active
ie when the player is out of the system, the enemy should do nothing but
when they're there, they can move attack, etc.
use the DICT command method you described in controller and create a way
for the player to issue commands
"""
"""
Second conclusion; it was too complicated to get it to work.
The UI ets clustered and the threads have to encompass the Game class,
and be within them at the same time without needing and extra 10 people to
both get it to work and keep track of the threads.
"""
##~~CONCLUSION~~##

import threading, random, time
from ship import Ship
from enemy import Enemy, voy, nx

player = voy
activeShips = {'nx':nx}
class myThread(threading.Thread):
    """pass the ship/enemy class that the thread belongs to"""
    def __init__(self,ship):
        threading.Thread.__init__(self)
        self.ship = ship
        self.name = self.ship.name
    #allow the player to give 'NX' or the like and parse the gridList for
        #an OBJ(enemy) for the name attribute equal to the input
        #then pass the obj to this function
    def attack(self):
        if self.ship.__class__ == Ship:
            enemy = input("Choose an enemy: ")
            try:
                activeShips[enemy].receiveDamage(self.ship.chooseAttack())
            except KeyError:
                print("Invalid Target")
        elif self.ship.__class__ == Enemy:
            player.receiveDamage(random.choice(self.ship.weapons))
            time.sleep(random.randint(10,20))
    def run(self):
        print("Starting Thread for {}".format(self.ship.name))
        while self.ship.hull > 0:
            #usually the program will take a command here rather than just
            #performing attack over and over
            self.attack()
        print("Ended Thread for {}".format(self.ship.name))
def threadTest():
    dave = myThread(voy)
    alf = myThread(nx)

    dave.start()
    alf.start()
