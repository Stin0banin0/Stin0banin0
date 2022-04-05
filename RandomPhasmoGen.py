import random

items={"Light":["Flashlight","Strong Flashlight","Candle"],"Evidence":["Thermometer","D.O.T.S.","UV Light","EMF Reader","Spirit Box","Ghost Writing Book","Video Camera"],"Safety":["Sanity Pills","Crucifix","Smudge Stick"],"Other":["Parabolic Microphone","Motion Sensor","Sound Sensor","Salt","Photo Camera","Tripod","Glowstick","Head Mounted Camera"],"All":["Parabolic Microphone","Motion Sensor","Sound Sensor","Salt","Photo Camera","Tripod","Glowstick","Head Mounted Camera","Flashlight","Strong Flashlight","Candle","Thermometer","D.O.T.S.","UV Light","EMF Reader","Spirit Box","Ghost Writing Book","Video Camera","Sanity Pills","Crucifix","Smudge Stick"]}

def fullRoll():
    Roll=[]
    Roll.append(items["Light"][random.randint(0,2)])
    Roll.append(items["Evidence"][random.randint(0,6)])
    Roll.append(items["Evidence"][random.randint(0,6)])
    Roll.append(items["Safety"][random.randint(0,2)])
    Roll.append(items["Other"][random.randint(0,7)])
    Roll.append(items["All"][random.randint(0,20)])
    return Roll

def singleRoll():
    category=input("Categories are: Light, Evidence, Safety, Other, All.  ")
    return(random.choice(items[category]))

