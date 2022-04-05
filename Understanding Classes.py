import random

logToggle=True

def log(data):
    if logToggle==True:
        print(data)

class fighter:

    def __init__(self,name,race):
        self.name=name
        self.race=race
        self.maxHP=15
        self.currentHP=self.maxHP
        
        self.status="alive"

    def attack(self,target,attack):
        
        target.getDmg(self,dmg)
        log("")

    def getDmg(self,by,dmg):
        self.currentHP=self.currentHP-trueDmg
        if self.currentHP<1:
            log("{name} has been killed by {by}.".format(name=self.name,by=by))
            self.status="dead"
        else:
            log("{name} has {health} health left.".format(name=self.name,health=self.currentHP))

    def heal(self,Hp,overHeal=True):
        self.currentHP=self.currentHP+trueHP
        if self.currentHP>self.maxHP and overHeal==False:
            self.currentHP=self.maxHP
        log(self.name+" now has "+currentHP+" HP.")

    def consume(self,food):
        print("Your mother has a case of homophilia")

flan=fighter("Flantrix","Flantrophians")

class enemy:

    def __init__(self,name,race):
        self.name=name
        self.race=race

        self.status="alive"

    def attack(self,target,attack):
        
        target.getDmg(self,dmg)
        log("")
    
    def getDmg(self,by,dmg):
        self.currentHP=self.currentHP-trueDmg
        if self.currentHP<1:
            log("{name} has been killed by {by}.".format(name=self.name,by=by))
        else:
            log("{name} has {health} health left.".format(name=self.name,health=self.currentHP))

seb=enemy("Sebastian","ogre")
