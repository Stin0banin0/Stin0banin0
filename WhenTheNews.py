import GenLib
import Tape
import random

print("**Welcome to the belated 12:00 news with When The**")

message="Today's main item: "
subject=random.choice(GenLib.randSubj)
message=message+subject[0]+". "

print(message)

subject=random.choice(GenLib.randSubj)
other=[random.choice(GenLib.randSubj),random.choice(GenLib.randSubj),random.choice(GenLib.randSubj)]
message="[1] [2] on the loose. What that means for [4] is as of yet unclear, but ".format("yo mama",subject[0],subject[1],subject[2],other[0][0],other[0][1],other[0][2],other[1][0],other[1][1],other[1][2])

print(message)