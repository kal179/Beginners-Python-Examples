class human: # object human to declare a person
    def __init__(self,gender,name,age,skills,password):
        self.gender = gender    #gender attribute of object human
        self.name = name    #name attribute of object human
        self.age = age      #age attribute of obj. human
        self.skills = skills    # skills attribute of obj.
        self.password = password    # password attribute of obj. human(necessary for logIn function)
    def sayHello(self) :     # function to say hello to obj. human
        print("Hello",self.name," Welcome to tunestore.com")
    def profile(self) : # function to view profile of obj. human
        print("--------------------------------------------------------")
        print("Profile")
        print("--------------------------------------------------------")
        print("User  :  ",self.name) # to show attribute name
        print("Gender  :  ",self.gender)  # to show attribute gender
        print("Age  :  ",self.age)  # to show attribute age
        print("Likes  :  ",self.skills)  # to show attribute skills
        print("--------------------------------------------------------")

#user interacion section
# following variable will set username
get_name = str(input("Username : "))
# following variable will set password
get_password = str(input("password : "))
# following variable will set gender
get_gender = str(input("Gender : "))
# following variable will set age
get_age = int(input("Age : "))
# following variable will set likes
get_skill = str(input("Likes : "))

print("                 ")

# setting attributes to variables
kalpak = human(get_gender, get_name, get_age, get_skill,get_password)

# printing functions from class
print(kalpak.sayHello()) # say hello function
print("                              ")
print(kalpak.profile()) # view profile function

# this a log in function
# this function authorises user to data
def logIn():
    while True : # loop is for try again
        print("Log In :")
        getUsername = str(input("username  :  "))
        getPassword = str(input("password  :  "))
        if (getUsername == kalpak.name) and (getPassword == kalpak.password) :
            print("Log in successful")
            print(kalpak.profile())
            break # break will break loop and print next function if username or password is wrong
        else :
            print("Invalid username or password")
            print("Try again...")
            print("--------------------------------------------------------")
            continue # continue is to try logging in again if user name or password is wrong
print(logIn()) # calling function
# telling user that he is authorised to access the passwords
print("Access granted")
print("Now you have complete access to the data")

# the data the user has to access in a form of dictionary called passwords
passwords = {"facebook" : "charlieat" ,
             "ubuntu" : "charlieAT12345" ,
             "windows" : "qwertyqwerty" ,
             "gmail" : "charlieat" ,
             "outlook" : "charlieat12345" }

while True : # a loop
    # asking user what to access
    userAccess = str(input("site of password : "))

    # checking what user asked in conditionals
    if (userAccess.strip() == "facebook") :
        print(passwords["facebook"])
        break # allowing user for one time access

    # probablity of input
    elif (userAccess.strip() == "ubuntu") :
        print(passwords["ubuntu"])
        break # allowing user for one time access

    # another probablity of input
    elif (userAccess.strip() == "windows") :
        print(passwords["windows"])
        break # allowing user for one time access

    # another probablity of input
    elif (userAccess.strip() == "gmail") :
        print(passwords["gmail"])
        break # allowing user for one time access

    # another probablity of input
    elif (userAccess.strip() == "outlook") :
        print(passwords["outlook"])
        break # allowing user for one time access

    # probablity of input if input was wrong
    else :
        print("The data you are trying to access is not in the database.")
        continue # allowing user to try finding data again if input was wrong
