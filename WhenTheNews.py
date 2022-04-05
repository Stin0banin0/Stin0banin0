import genLib
import random

print("**Welcome to the belated 12:00 news with When The**")

message="Today's main item: "
subject=capitalise(random.choice(genLib.randSubj))
message=message+subject[0]+". "

print(message)

subject=random.choice(genLib.randSubj)
message=subject[0]+" "+subject[1]+" on the loose. What that means for "+random.choice(randSubj)+" is as of yet unclear, but "+randSubj+
