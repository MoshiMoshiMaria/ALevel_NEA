import threading, time

class myThread(threading.Thread):
    def __init__(self,boiID,name,value):
        threading.Thread.__init__(self)
        self.boiID = boiID
        self.name = name
        self.value = value
    def doStuff(self):
        value = self.value
        while True:
            if value > 15:
                break
            else:
                print(value,end="\n")
                value+= 1
                time.sleep(1)
            
    def run(self):
        print("Thread {}({}): Starting...\n".format(self.boiID,self.name))
        self.doStuff()
        print("Thread {}({}): Ended.".format(self.boiID,self.name))

dave = myThread(1,"Dave",1)
alf = myThread(2,"Alf",6)

dave.start()
alf.start()
while True:
    if alf.value > 10:
        alf.value = 1

