# pre code
# main list of contacts
contacts = {}

# funcs of pre code
# func to add new contact
def newContact():
    while True:
        newContact = raw_input("Name for new Contact : ")
        numForNewContact = raw_input("Number for Contact : ")
        add = raw_input("Add or Try again :")
        if add.strip() == "Add":
            contacts[newContact] = numForNewContact
            print("Contact Successfully added.")
            break
        elif add.strip() == "Try again":
            continue
        else :
            print("Invalid Input.try again")
            continue
        startAgain = raw_input("Add more or continue : ")
        if startAgain.strip() == "Add more":
            print(" ")
            continue
        elif startAgain.strip() == "continue":
            print(" ")
            break

# func to search for a contact
def searchContact():
    while True:
        search = raw_input("Search for contact : ")
        toShow = str(search) + contacts[search]
        print(toShow)
        startAgain = raw_input("Search more or continue : ")
        if startAgain.strip() == "Search more":
            print(" ")
            continue
        elif startAgain.strip() == "continue":
            print(" ")
            break

# func to edit a contact
def editContact():
    while True:
        whichToEdit = raw_input("Name of Contact of which Number to Edit : ")
        contacts[whichToEdit] = raw_input("Number to add : ")
        startAgain = raw_input("Edit more or continue : ")
        if startAgain.strip() == "Edit more":
            print(" ")
            continue
        elif startAgain.strip() == "continue":
            print(" ")
            break

# main code to interact
while True:
    print("hello,".title())
    # part of main code to start or end
    startOrEnd = raw_input("Start or End : ")
    if startOrEnd.strip() == "Start":
        # part of main code to control functions
        addSearchEdit = raw_input("Add or Search or Edit : ")
        if addSearchEdit.strip() == "Add":
            print(newContact())
        elif addSearchEdit.strip() == "Search":
            print(searchContact())
        elif addSearchEdit.strip() == "Edit":
            print(editContact())
        else :
            print("Invalid Input . Try Again")
            continue
    elif startOrEnd.strip() == "End":
        print("Ending...")
        break
    else :
        print("Invalid Input . Try Again")
        continue
    # part of main code to start again or end
    startAgain = raw_input("Start again or End : ")
    if startAgain.strip() == "Start again":
        print("Starting  again...")
        continue
    elif startAgain.strip() == "End":
        print("Ending program...")
        break
    else :
        break
