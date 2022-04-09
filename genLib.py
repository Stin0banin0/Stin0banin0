import random

firstName={"English":{"Male":["Marc","Ben","Peter"],"Female":["Alice","Diana"]}}
lastName={"English":["Stephenson",""]}
researchInst=["RIVM","CIA","FBI","Fox News","The Guardian","Individual researchers","David Attenborough"]
randSubj=[["a man",'is','he'],["the biggest bicycle of England","is","it"],["a gigantic horn","is","it"],["pie in a cup","is","it"],["geese","are","they"],["a parkinson's sufferer","is","they"],["a ghastly toll","is","it"],["belated albondigas","are","they"],["Captain Jack Sparrow","is","he"],["racism","is","it"],["Elongated Musk","is","he"],["Oolong Musk","is","he"],["cool diabetes","is","it"],["gastric juices","is","it"],["the river Tonga","is","it"],["the Polish polka","is","it"],["your gay mother","is","she"],["the pasteurisation process of milk","is","it"],["meatball warriors","are","they"],["the only Meatball Man","is","He"],["discriminatory nigger circus","is","it"],["sexy toupee man","is","he"],["a funny news message","is","it"],["porridge","is","it"]]

noun=[['ape','an','apes']]
verb={'be':['be',['am','are','is'],['was','were','was']]}
add=[['happy','happily']]

def randName():
    rand=random.randint(0,1)
    #return(name[rand][random.randint(0,(len(name[ran]-1)))])