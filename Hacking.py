import time
import random

firstNames=["Mark","Peter","Frank","Alice","Sandra","Carl","Phill","Shawn","Dean","Dan","Sharon","Billie","Mary","Jane"]
lastName=["Fredrics","Caulton","]
cities={"England, UK":["London","Southampton","Winchester","Croydon","Gloucester","Northampton","Cambridge","Ipswitch","Canterbury","Coventry","Sheffield","Leeds","Bath"],"Scotland, UK":["Edinburgh","Inverness","Aberdeen","Stirling","Glasgow","Dumfries"],"Wales, UK":["Holyhead","Wrexham","Llandudno","Aberystwyth","Fishguard","Milford Haven","Swansea"],"Northern Ireland, UK":["Belfast","Enniskillen","Coleraine","Londonderry","Strabane"],"Ireland":["Dublin","Cork","Galway","Castlebar","Mullingar","Navan"],"US":{"Alabama":["Montgomery","Huntsville","Birmingham","Tuscaloosa","Mobile"],"Alaska":["Fairbanks","Anchorage","Seward","Valdez","Horner","Kodiak","Nome","Kotzebue","Barrow","Dutch Harbor","Tok"],"Arizona":["Page","Kingman","Flagstaff","Springerville","Holbrook","Phoenix","Yuma","Tucson","Nogales"],"Arkansas":["Texarkana","Ft. Smith","Hoxie","Little Rock"],"California":["Crescent City","Redding","Eureka","Red Bluff","Santa Rosa","Alturas","Sacramento","San Francisco","Oakland","Stockton","San Jose","Fresno","Salinas","San Luis","Obispo","Bakersfield","Los Angeles","San Bernadino","Long Beach","Riverside","Blyhte","San Diego"],"Colorado":["Grand Jct.","Colorado Springs"," Salida","Pueblo","Trinidad","Ft. Collins","Julesburg"],"Conneticut":["Hartford","Bridgeport","New Haven"],"Delaware":["Newark","Trenton","Atlantic City","Dover"],"Florida":["Tallahassee","Lake City","Jacksonville","Panama City","Daytona Beach","Orlando","Tampa","St. Petersburg","Ft. Pierce","Ft. Myers","Fort Lauderdale","Miami","Key West"],"Georgia":["Atlanta","Augusta","Macon","Columbus","Trifton","Savannah","Brunswich","Valdosta"],"Hawaii":["Honolulu"],"Idaho":["Sandpoint","Boise","Idaho Falls","Pocatello"],"Illinois":["Rockford","Chicago","Peoria","Bloomington","Springfield","Cairo"],"Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minessota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"}},"Canada":[],"Australia":[],"Austria":[],"France":[],"Germany":[],"Switzerland":[],"Denmark":[],"The Netherlands":["Amsterdam"],"Spain":[],"Portugal":[],"Italy":[],"China":[],"Japan":[],"Russia":[],"Ukraine":[]}

def firstName():
    

def lastName():
    

root = "C:\\"
while 1==1:
    command=input("\n"+">>> "+root)
    if command=="System.reset":
        for i in range(3):
            time.sleep(1)
            print(str(3-i))
        time.sleep(1)
        print("System has been reset")
        
    elif command=="System.rewind":
        print("system rewound to last state")

    elif command=="System.getTime":
        print(str(time.time())+" hours elapsed")

    elif command=="changeRoot":
        oldRoot=root
        newRoot=input("setNewRoot=")
        if not newRoot[len(newRoot)-1]=="\\":
            newRoot=newRoot+"\\"
        root=newRoot

    elif command=="
    
    else:
        binary=""
        for i in range(random.randint(30,50)):
            binary=binary+str(random.randint(0,1))
        print(binary)
    
