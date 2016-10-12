

def adda():
    spam=raw_input("enter number here:")
    eggs=raw_input("enter next number :")
    print(int(spam)+int(eggs))	
	
def extract():
    spam=int(raw_input("enter number here:"))
    eggs=int(raw_input("enter next number :"))
    print(spam-eggs)	
	
def multiple():
    spam=int(raw_input("enter number here:"))
    eggs=int(raw_input("enter next number :"))
    print(spam*eggs)	

def divi():
    spam = int(raw_input("enter number here:"))
    eggs = int(raw_input("enter next number :"))
    try:
       print(spam/eggs)
    except ZeroDivisionError:
        print("Cannot divide by Zero.")   
 
def modula():
    spam=int(raw_input("enter number here:"))
    eggs=int(raw_input("enter next number :"))
    print(spam%eggs)

user = raw_input("enter add,subtract,multiply,divide,modulo :")	
if user == "add":
    print(adda())
elif user == "subtract":	
    print(extract())
elif user == "multiply":
    print(multiple())
elif user == "divide":
    print(divi())
elif user == "modulo":
    print(modula())
	

