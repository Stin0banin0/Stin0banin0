import random

#Here will come a few lists of words that can have a certain intention.
yes=["yes","yeah","yea","y","true","I am","I do","affirmative","ye","yeh","ya","yah","yup","yep","Yes","Yeah","Yea","Y","True","Affirmative","Ye","Yeh","Ya","Yah","Yup","Yep"]
no =["no","nope","not","false","negative","nada","I am not","I'm not","I aren't","I do not","I don't"]

def interpret(interpret):
    if interpret in yes:
        return "y"
    if interpret in no:
        return "n"

currentRoom=[0,0]
#The rooms will be stored in a list grid, where the list currentroom keeps track of the room the player is currently in. N+/S- is y, E+/W- is x.
#The form of room storage

#printRoom will tell the player what the room around them looks like
def printRoom(doors,enemies,items,puzzles):
    roomDesc=""
    if doors==false:
        roomDesc=roomDesc+"The room has no doors, "

    if enemies==false:
        roomDesc=roomDesc+"contains no lurking dangers for as far as you can see, "

    if items==false:
        roomDesc=roomDesc+"doesn't have anything to loot, "

    if puzzles==false:
        roomDesc=roomDesc+"and yields no brain work

def genRoom(doors,enemies,items,puzzles):
    if doors==false:
        
        
    if none in doors:

    if doors{}
        
        

input("Welcome traveler. Are you ready for a story that will puzzle your mind? ")
print("Well, it doesn't really matter much. You're stuck here anyway.")
