#Tape.py is for software engineers what normal tape is for engineers

'''
def getLibraryKeyPosition(item,library):
    print("This will find the position of a key in a library")

def getLibraryValuePosition(key,library):
    print("This will find the position of a value in a library")

def getLibraryPositionKey(position,library):
    print("This will find the key on a position in a library")

def getLibraryPositionValue(position,library):
    print("This will find the value on a position in a library")
'''

def addUpLibraries(lib1,lib2):
    for key in lib2:
        if key in lib1:
            lib1[key]=lib1[key]+lib2[key]
        else:
            lib1[key]=lib2[key]
    return lib1

def capitalise(string):
    character=string[0]
    return character.upper()+string[1:]