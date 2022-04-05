import random
insult=("");
#def ins1():
    
#def ins2():
    
#def ins3():
    
#Use ins1, ins2, etc. to call insadds
def insadd(a):
    global insult
    insult=(insult+(a));
def arbadd(a):
    global insult
    insult=(insult+random.choice(a));
def possadd(insert,low,high):
    if random.randint(low,high):
        insadd(insert);



verb=(["est"]);
auxverb=(["dev"])
adj=(["bona","bela","granda","mola","grava"]);
noun=(["la vero","hundo","banano","malseka pano","pantaso","cxokolada supo","la ikto de Heldero","la vetero en la somero"]);
#First failed attempt: Vi devas adj malvi estas kial vi estas.
#First successful attempt: Vi devas adj malmola kial pantaso.
#Add more variety of insults
#You can use random.choice(["1","2"]); or random.choice of variable a=(["a","b"]);
#You can also add []s inside of more []s
def ins1():
    global insult
    insult=("Vi ");
    arbadd(verb);
    insadd("as ");
    possadd("mal",0,1)
    arbadd(adj);
    insadd(" kial ")
    arbadd(noun);
    insadd(".")
    print(insult);

def ins2():
    global insult
    insult=("Vi ");
    arbadd(verb)
    insadd("as kial ")
    arbadd(noun)
    insadd(".");
    print(insult);

def ins3():
    global insult
    insult=("Mi vi ");
