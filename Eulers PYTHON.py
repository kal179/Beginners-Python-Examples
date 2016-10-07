while("Euler" != "Pythagoras"):
    print("--------------------------------------------------")
    print("CASE 1: F + V = E+2")
    print("CASE 2: V = E+2 - F")
    print("CASE 3: F = E+2 - V")
    print("--------------------------------------------------")
    get_again_again = raw_input("Enter CASES for calculation:")
    if get_again_again == "CASE 1":
        get = int(input("Enter faces of the Figure:"))
        print("--------------------------------------------------")
        get_again = int(input("Enter Vertices of the figure:"))
        print("--------------------------------------------------")
        print("Edges are ",(get + get_again)-2)
        print("--------------------------------------------------")
    elif get_again_again == "CASE 2":
        get = int(input("Enter Edges of the Figure:"))
        print("--------------------------------------------------")
        get_again = int(input("Enter Faces of the figure:"))
        print("--------------------------------------------------")
        print("Vertices are ",(get + 2) - get_again)
        print("--------------------------------------------------")
    elif get_again_again == "CASE 3":
        get = int(input("Enter Edges of the Figure:"))
        print("--------------------------------------------------")
        get_again = int(input("Enter Vertices of the figure:"))
        print("--------------------------------------------------")
        print("Vertices are ",(get + 2) - get_again)
        print("--------------------------------------------------")
    feature = raw_input("Start again or End:")
    if feature == "Start again":
        print("Starting again...")
        print(" ")
        continue
    elif feature == "End":
        print("Ending program...")
        print("Finished")
        print(" ")
        print("--------------------------------------------------")
        break
