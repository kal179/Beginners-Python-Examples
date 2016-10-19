#pre-code
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

# MAIN code
print(" ")
print("--------------------Start-------------------")
user = raw_input("Start or End : ")

if user.strip() == "End" :
        print(" ")
        print("------------------Program Ended--------------")
        print(" ")
elif user.strip() == "Start" :
    print(testDivisibility())
    print(" ")

    while True:
    
        get = raw_input("Start again or End : ")
        if get.strip() == "Start again":
            print("---------------Start Again----------------")
            print(" ")
            print(testDivisibility())
            continue
        elif get.strip() == "End" :
            print(" ")
            print("------------------Program Ended--------------")
            print(" ")
            break
