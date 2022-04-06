group = list()

def exe(prependix,postpendix):
    temp = ""
    for i in range(len(group)):
        temp = temp+""+prependix+group[i]+postpendix
    return temp

answer = input("What is the next word to add to the list? (type \"stop\" to end off the list) ")
while not answer == "stop":
    list.append(answer)
    answer = input("What is the next word to add to the list? (type \"stop\" to end off the list) ")
print("Done setting the list. Use exe(<prependix>,<postpendix>) to generate the list.")
