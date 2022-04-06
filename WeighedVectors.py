vector = list()

def add(mass,x,y,z):
    vector.append([mass,x,y,z])

def calc():
    massTot = 0
    xTot = 0
    yTot = 0
    zTot = 0
    
    for i in range(len(vector)):
        xTot = xTot + vector[i][0]*vector[i][1]
        yTot = yTot + vector[i][0]*vector[i][2]
        zTot = zTot + vector[i][0]*vector[i][3]
        massTot = massTot + vector[i][0]
    xW = xTot/massTot
    yW = yTot/massTot
    zW = zTot/massTot
    return "("+str(round(xW,3))+","+str(round(yW,3))+","+str(round(zW,3))+"), total mass: "+str(round(massTot,4))

def void():
    vector.clear()
