import random

levelRewards={0:{},1:{},2:{'hp':[6]},3:{[]}}
tokens=[0,0,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5]
stats=['hp','mana','damage']
standardDice={4:[4],6:[6],8:[8],10:[0,9],12:[12],20:[20],100:[0,90,10]}

def regDice(dice):
    value=0
    for i in range(len(dice)):
        die=standardDice[dice[i]]
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
    statPossibilities=['hp','mp','strength','intelligence','constitution','wisdom','dexterity','charisma']
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
