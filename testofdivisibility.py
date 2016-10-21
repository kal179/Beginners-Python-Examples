# pre code
def testDivisibility():
    print(" ")
    toTest = int(raw_input("Enter number of which you want to test Divisibility : "))
    print(" ")
    test = int(raw_input("Enter number by which you want to test : "))
    if toTest % test == 0 :
        print("-------------Answer---------------- ")
        print(str(toTest) + " is divisible by " + str(test))
    else :
        print(str(toTest) + " is not divisible " + str(test))

print(" ")
print("--------------------Start-------------------")
user = raw_input("Start or End : ")

if user.strip() == "Start" :
        print(testDivisibility())
        print(" ")        
# MAIN code
while True:
        get = raw_input("Start again or End : ")
        if get.strip() == "Start again":
            print("---------------Start Again----------------")
            print(" ")
            continue
        elif get.strip() == "End" :
            print(" ")
            print("------------------Program Ended--------------")
            print(" ")
            break
        else :
            break

    elif user.strip() == "End" :
        print(" ")
        print("------------Program Ended-----------")
        print(" ")
        break

    else :
        print(" ")
        print("Invalid Input. Try again")
        continue
