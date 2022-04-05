import random

levelRewards={0:{},1:{},2:{'hp':[6]}}
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

def oneReward(rewardName,reward):
    print("")
#if 'hp' in rewards:
#    if isinstance(rewards[hp],int):
#        rewardList

def combineStats(stats):
    print("Yro'ue")

def lvlRewards(level):
    rewards=levelRewards[level]
    rewardList={}
    rewardList['tokens']=tokens[level]

def lvlUp(lowLevel,highLevel,rollTokens=False):
    for i in range(lowLevel+1,highLevel+1):
        lvlRewards(i)

print("lvlUp(<lowLevel>,<highLevel>) allows you to roll random lvlUp rewards for that set of levels. rollDice() uses a list to roll dice automatically.")

