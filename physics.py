# physics calcy

operations = [ "Preassure" , "Force" , "Speed" , "Velocity" , "Accelaration" , "Momentum" ]

#pre code sector I
# preassure function to calculate preassure
def preassure():
    print(" ")
    force = int(raw_input("Enter force : "))
    print(" ")
    area = int(raw_input("Enter area : "))
    preassure = force / area
    print(" ")
    print("Preassure is " + str(preassure) + "pascal")

# force function to calculate force
def force():
    print(" ")
    mass = int(raw_input("Enter mass : "))
    print(" ")
    accelaration = int(raw_input("Enter accelaration : "))
    force = mass * accelaration
    print(" ")
    print("Force is " + str(force) + "newton")

# speed func to calculate speed of object
def speed():
    print(" ")
    distance = int(raw_input("Enter distance : "))
    print(" ")
    time = int(raw_input("Enter time taken : "))
    speed = distance / time
    print(" ")
    print("Speed of object is " + str(speed))

# velocity func to calculate velocity of object
def velocity():
    print(" ")
    displacement = int(raw_input("Enter displacement : "))
    print(" ")
    time = int(raw_input("Enter time taken : "))
    velocity = displacement / time
    print(" ")
    print("Velocity of object is " + str(velocity))

# accelaration func to calculate accelaration
def accelaration():
    print(" ")
    initialV = int(raw_input("Enter initial velocity : "))
    print(" ")
    finalV = int(raw_input("Enter final velocity : "))
    print(" ")
    time = int(raw_input("Enter time taken : "))
    acce = (finalV - initialV) / time
    print(" ")
    print("Accelaration is " + str(acce) + "m/s sq.")

# monentum func to calculate momentum
def moment():
    print(" ")
    mass = int(raw_input("Enter mass : "))
    print(" ")
    velocity = int(raw_input("Enter velocity : "))
    print(" ")
    momentum = mass * velocity
    print(" ")
    print("Momentum is " + str(momentum))

# CLI code sector II

while True:
    print(" ")
    print("Hello")
    print(" ")
    startOrEnd = raw_input("Start or End : ")
    print(" ")
    if startOrEnd.strip() == "Start" :
        for op in operations:
            print(op)
            print(" ")

        main = raw_input("Which operation : ")
        if main.strip() == "Preassure":
            print(preassure())
            continue
        elif main.strip() == "Force":
            print(force())
            continue
        elif main.strip() == "Speed":
            print(speed())
            continue
        elif main.strip() == "Velocity":
            print(velocity())
            continue
        elif main.strip() == "Accelaration":
            print(accelaration())
            continue
        elif main.strip() == "Momentum":
            print(moment())
            continue
        else :
            print("Invalid operation")
            continue
    elif startOrEnd.strip() == "End":
        print("...Progarm Ended...")
        break
