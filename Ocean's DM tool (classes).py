import random

class lvlUp:
    #levelRewards formatting: hp:[definite,die,die,...]
    levelRewards={21:{},20:{'summonSlots':[5],'hp':[0,20,20,20],'mana':[0,4,4,4,4,4],'spellSlots':[2],'defence':[3],'armourPen':[0,8],'damage':[0,4,4]},19:{'hp':[2,10,10],'mana':[0,10]},18:{'damage':[0,2]},17:{'mana':[0,6,6]},16:{'hp':[10],'armourPen':[3]},15:{'damage':[2],'mana':[5]},14:{'spellSlots':[1],'hp':[0,6]},13:{'damage':[0,6],'armourPen':[0,4]},12:{'hp':[0,6],'classUpgrades':[1]},11:{'damage':[1],'mana':[0,4]},10:{'hp':[0,20],'mana':[0,6],'spellSlot':[1],'damage':[0,4],'defence':[2],'armourPen':[1],'summonSlots':[2]},9:{'mana':[0,10]},8:{'damage':[2],'armourPen':[1]},7:{'extraClass':[1],'armourPen':[-1,4]},6:{'defence':[1],'mana':[3],'classUpgrades':[1]},0:{},1:{},2:{'hp':[0,6]},3:{'mana':[0,4],'damage':[1]},4:{'hp':[1,10],'armourPen':[1]},5:{'damage':[0,4],'spellSlots':[1],'summonSlots':[3]}}
    tokens=[0,0,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5]
    stats=['hp','mana','damage','armourPen','spellSlots','summonSlots','defence','classUpgrades','extraClass','spellSlots']
    standardDice={2:[2],4:[4],6:[6],8:[8],10:[0,9],12:[12],20:[20],100:[0,90,10]}

    def regDice(self,dice,diceList=standardDice):
        value=0
        for i in range(len(dice)):
            die=diceList[dice[i]]
            if len(die)==1:
                value=value+random.randint(1,die[0])
            elif len(die)==2:
                value=value+random.randint(die[0],die[1])
            elif len(die)==3:
                value=value+random.randrange(die[0],die[1],die[2])
        return value



#Dice format is [[amount of these dice, die number, optional die interval]]
def rollDice(dice):
    value=0
    for i in range(len(dice)):
        for i2 in range(dice[i][0]):
            if len(dice[1])>2:
                value=value+random.randrange(dice[i][2],dice[i][1],dice[i][2])
            else:
                value=value+random.randint(1,dice[i][1])
    return value

#if 'hp' in rewards:
#    if isinstance(rewards[hp],int):
#        rewardList

def lvlRewards(level):
    rewards=levelRewards[level]
    rewardList={}
    rewardList['tokens']=tokens[level]

def combineStats(stats):
    lib1=stats[0]
    lib2=stats[1]
    libEnd={}
    #stats
    for i in range(len(statPossibilities)):
        lvlStat=statPossibilities[i]
        if lvlStat in lib1 and lvlStat in lib2:
            libEnd[statPossibilities]=lib1[lvlStat]+lib2[lvlStat]
        elif lvlStat in lib1:
            libEnd[lvlStat]=lib1[lvlStat]
        elif lvlStat in lib2:
            libEnd[lvlStat]=lib2[lvlStat]
    return libEnd 

def rollToken(amount):
    print("This rolls for the given amount of tokens")

def lvlUp(lowLevel,highLevel,rollTokens=False):
    for i in range(lowLevel+1,highLevel+1):
        combineStats()
    
    if rollTokens==True:
        rewards="dummy"
        rollTokens(rewards['tokens'])

print("lvlUp(<lowLevel>,<highLevel>) allows you to roll random lvlUp rewards for that set of levels. rollDice() uses a list to roll dice automatically.")

