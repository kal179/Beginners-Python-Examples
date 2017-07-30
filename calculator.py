def addition():
	return float(raw_input("Number: ")) + float(raw_input("Next number: "))

def subtraction():
	return float(raw_input("Number: ")) - float(raw_input("Next number: "))

def multiplication():
	return float(raw_input("Number: ") * raw_input("Next number: "))

def division():
	return float(raw_input("Number: ")) / float(raw_input("Next number: "))

def modulo():	
	return float(raw_input("Number: ")) % float(raw_input("Next number: "))

def exp_calcy():
	try:
		return eval(raw_input("Expression: "))
	except Exception as e:
		return e
	
def calcy(a, b, c, d, e):
	dispatch = {"add":a, "subtract":b, "multiplication":c, "division":d, "modulo":e}
	try:
		return dispatch[raw_input("Operation: ")]()
	except Exception as e:
		return e
		
print("Hello,")
while(True):
	start_or_end = raw_input("start or end: ")
	if start_or_end.strip().lower() == "start":
		which_calc = raw_input("calcy or exp_calcy(Exp = Expression): ")
		if which_calc.strip().lower() == "calcy":
			print(calcy(addition, subtraction, multiplication, division, modulo))
		elif which_calc.strip().lower() == "exp_calcy":
			print(exp_calcy())
		else:
			print("Invalid Input. Try again.\n")
		continue
	else:
		break
