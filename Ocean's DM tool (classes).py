import random
import Tape

class LvlUp:
    #levelRewards formatting: hp:[definite,die,die,...]

    def __init__(self):
        self.hp=0
        self.mana=0
        self.damage=0
        self.armourPen=0
        self.spellSlots=0
        self.summonSlots=0
        self.defence=0
        self.classUpgrades=0
        self.extraClass=0
        self.spellSlots=0
        levelRewards={21:{},20:{'summonSlots':[5],'hp':[0,20,20,20],'mana':[0,4,4,4,4,4],'spellSlots':[2],'defence':[3],'armourPen':[0,8],'damage':[0,4,4]},19:{'hp':[2,10,10],'mana':[0,10]},18:{'damage':[0,2]},17:{'mana':[0,6,6]},16:{'hp':[10],'armourPen':[3]},15:{'damage':[2],'mana':[5]},14:{'spellSlots':[1],'hp':[0,6]},13:{'damage':[0,6],'armourPen':[0,4]},12:{'hp':[0,6],'classUpgrades':[1]},11:{'damage':[1],'mana':[0,4]},10:{'hp':[0,20],'mana':[0,6],'spellSlot':[1],'damage':[0,4],'defence':[2],'armourPen':[1],'summonSlots':[2]},9:{'mana':[0,10]},8:{'damage':[2],'armourPen':[1]},7:{'extraClass':[1],'armourPen':[-1,4]},6:{'defence':[1],'mana':[3],'classUpgrades':[1]},0:{},1:{},2:{'hp':[0,6]},3:{'mana':[0,4],'damage':[1]},4:{'hp':[1,10],'armourPen':[1]},5:{'damage':[0,4],'spellSlots':[1],'summonSlots':[3]}}
        tokens=[0,0,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5]
        stats=['hp','mana','damage','armourPen','spellSlots','summonSlots','defence','classUpgrades','extraClass','spellSlots']
        standardDice={2:[2],4:[4],6:[6],8:[8],10:[9,0],12:[12],20:[20],100:[90,0,10]}
        tokenStats={{"easter egg":"This"},{'health':[1,10],'mana':[0,4,4],'gold':[50]},{'defence':[1],'damage':[1],'strength':[1],'wisdom':[1],'intelligence':[1],'charisma':[1],'dexterity':[1],'constitution':[1],'armourPen':[1],'spellSlots':[1]}}


    def rollRegularDice(self,dice,diceList=standardDice):
        value=0
        for i in range(len(dice)):
            die=diceList(dice[i])
            if len(die)==1:
                value+random.randrange(die[0])
            elif len(die)==2:
                value+random.randrange(die[0],die[1])
            elif len(die)==3:
                value+random.randrange(die[0],die[1],die[2])
        return value
    
    #Dice format is [[amount of these dice, die number, optional die interval]]
    def rollDice(self,dice):
        value=0
        for i in range(len(dice)):
            for i2 in range(dice[i][0]):
                if len(dice[1])>2:
                    value=value+random.randrange(dice[i][2],dice[i][1],dice[i][2])
                else:
                    value=value+random.randint(1,dice[i][1])
        return value
    
    def rollList(self,dice):
        value=dice[0]
        del dice[0]
        value=value+self.rollRegularDice(dice)

    def rollTokens(self,amount):
        rewards={}
        while amount>0:
            print("Rolls things")
        return rewards

    '''def lvlRewards(self,level):
        potentialRewards=self.levelRewards[level]
        rewards={}
        rewards['tokens']=self.tokens[level]'''
    
    def oneLevelReward(self,level):
        concerningRewards=self.levelRewards[level]
        if 'hp' in concerningRewards:
            self.hp=self.rollList(concerningRewards['hp'])
        if 'mana' in concerningRewards:
            self.mana=self.rollList(concerningRewards['mana'])
        if 'damage' in concerningRewards:
            self.damage=self.rollList(concerningRewards['damage'])
        if 'armourPen' in concerningRewards:
            self.armourPen=self.rollList(concerningRewards['armourPen'])
        if 'spellSlots' in concerningRewards:
            self.spellSlots=self.rollList(concerningRewards['spelllSlots'])
        if 'summonSlots' in concerningRewards:
            self.summonSlots=self.rollList(concerningRewards['summonSlots'])
        if 'defence' in concerningRewards:
            self.defence=self.rollList(concerningRewards['defence'])
        if 'classUpgrades' in concerningRewards:
            self.classUpgrades=self.rollList(concerningRewards['classUpgrades'])
        if 'extraClass' in concerningRewards:
            self.extraClass=self.rollList(concerningRewards['extraClass'])
        if 'spellSlots' in concerningRewards:
            self.spellSlots=self.rollList(concerningRewards['spellSlots'])
    
    def lvlUp(self,lowLevel,highLevel,rollTokens=False):
        for i in range(lowLevel+1,highLevel+1):
            lvlUp.oneLevelReward(i)
        
        if rollTokens==True:
            rewards="dummy"
            rollTokens(rewards['tokens'])
        return rewards

def getLevelRewards():
    return LvlUp.levelRewards

def getTokens():
    return LvlUp.tokens

def getStats():
    return LvlUp.stats

def getStandardDice():
    return LvlUp.standardDice

#if 'hp' in rewards:
#    if isinstance(rewards[hp],int):
#        rewardList



while 1==1:
    lvlUp=LvlUp()
    answer=input("Choose: ROLL: roll dice, LVL UP: roll level up rewards")

    del lvlUp