
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
    spam=int(raw_input("enter number here:"))
    eggs=int(raw_input("enter next number :"))
    print(spam/eggs)
 
def modula():
    spam=int(raw_input("enter number here:"))
    eggs=int(raw_input("enter next number :")) 
    print(spam%eggs)

def calculas():
    multiverse=raw_input("enter add,subtract,multiply,divide,modulo :")	
    if multiverse==add:
            adda()
    elif multiverse==subtract:	
	        extract()
    elif muliverse==multiply:
            multiple()
    elif multiverse==divide:
	       divi()
    elif multiverse==modulo:
	     modula()
	
    calculas()