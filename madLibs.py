# my code may not work with python 3.5 cause it is made for 2.7 version
libs =["Dragon Freak","Excuses"]

# precode
def dragonFreak():
    colorDrag = raw_input("Color : ")
    superLatDrag = raw_input("Superlative (ending in est) : ")
    adj1Drag = raw_input("Adjective : ")
    bodyDragPlu = raw_input("Body Part Plural : ")
    bodyDrag = raw_input("Body Part : ")
    nounDrag = raw_input("Noun : ")
    animalDrag = raw_input("Animal(Plural) : ")
    adj2Drag = raw_input("Adjective : ")
    adj3Drag = raw_input("Adjective : ")
    adj4Drag = raw_input("Adjective : ")
    # creating madlib
    fMadLib = '''
    The %s Dragon is the %s Dragon of all. It has %s %s,
    and a %s shaped like a %s. It loves to eat %s,
    although it will feast on nearly anything. It is %s and %s.
    You must be %s around it, or you may end up as it`s meal!
    '''%(colorDrag , superLatDrag , adj1Drag , bodyDragPlu , bodyDrag , nounDrag , animalDrag , adj2Drag , adj3Drag , adj4Drag)

    print(fMadLib)

def excuses():
    place = raw_input("Place : ")
    adjExcuse = raw_input("Adjective : ")
    bodyPart = raw_input("Bodypart : ")

    fMadLib = '''
    I cannot come to %s ,
    because there is %s %s flu
    ''' %(place , adjExcuse , bodyPart)
    print(fMadLib)

# main code for user interaction
while True:
    startOrEnd = raw_input("Start or End : ")
    if startOrEnd.strip() == "Start":
        print(libs)
        whichLib = raw_input("Which one :")
        if whichLib.strip() == "Dragon Freak":
            print(dragonFreak())
            continue
        elif whichLib.strip() == "Excuse":
            print(excuses())
            continue
        else :
            print("Not avaliable")
            continue
    elif startOrEnd.strip() == "End":
        print("Progarm Ended...")
        break
