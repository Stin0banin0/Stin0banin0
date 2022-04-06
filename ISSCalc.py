import math

ISSSpeed=27600/3.6
ISSMass=419725
TotalTimes=0

def accel(mass,speed,times):
    global ISSSpeed
    global ISSMass
    global TotalTimes
    E=0.5*mass*speed*speed
    ISSE=0.5*ISSSpeed*ISSSpeed*ISSMass
    ISSE=ISSE+(E*times)
    ISSSpeed=(ISSE/(0.5*ISSMass))**0.5
    TotalTimes=TotalTimes+times
    print(str(TotalTimes)+" times")
    print(str(ISSSpeed)+"m/s")

def decel(mass,speed,times):
    global ISSSpeed
    global ISSMass
    global TotalTimes
    E=0.5*mass*speed*speed
    ISSE=0.5*ISSSpeed*ISSSpeed*ISSMass
    ISSE=ISSE-(E*times)
    ISSSpeed=(ISSE/(0.5*ISSMass))**0.5
    TotalTimes=TotalTimes+times
    print(str(TotalTimes)+" times")
    print(str(ISSSpeed)+"m/s")
