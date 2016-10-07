"""this program asks person to guess a number if the number is correct the code breaks
otherwise it runs continously as it is in infinite loop"""
while(2==2):
   print("Welcome to the Guessing Game")
   print("Hint:number is in range 10")
   start = raw_input("Enter Start or End:")
   if start == "Start":
       get = int(input("Guess the number:"))
       if get == 5:
           print("You Win")
           break
       elif get <= 4:
             print("Number you entered is Too Low")
       elif  get >= 6:
              print("Number you enetred is Too High")
   elif start == "End":
       print("Game Ended")
   else :
       print("You Lose Sorry!")
       print("Game Ended")
           
