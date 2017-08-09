def adda():
    return float(raw_input("enter number here:")) + float(raw_input("enter next number :"))
	
def extract():
    return float(raw_input("enter number here:")) - float(raw_input("enter next number :"))	
	
def multiple():
    return float(raw_input("enter number here:")) * float(raw_input("enter next number :"))

def divi():
    try:
       return float(raw_input("enter number here:")) / float(raw_input("enter number here:"))
    except ZeroDivisionError:
        return "Cannot divide by Zero."

def modula():
    return float(raw_input("enter number here:")) % float(raw_input("enter next number :"))

user = raw_input("enter add,subtract,multiply,divide,modulo :")	
if user == "add":
    print float(adda())
elif user == "subtract":	
    print float(extract())
elif user == "multiply":
    print float(multiple())
elif user == "divide":
    print float(divi())
elif user == "modulo":
    print float(modula())
