def addition():
	get_num = int(raw_input("Number : "))
	get_next_num = int(raw_input("Next number : "))
	added  = get_num + get_next_num
	return(added)

def subtraction():
	get_num = int(raw_input("Number : "))
	get_next_num = int(raw_input("Next number : "))
	added  = get_num - get_next_num
	return(added)

def multiplication():
	get_num = int(raw_input("Number : "))
	get_next_num = int(raw_input("Next number : "))
	added  = get_num * get_next_num
	return(added)

def division():
	get_num = int(raw_input("Number : "))
	get_next_num = int(raw_input("Next number : "))
	added  = get_num / get_next_num
	return(added)

def modulo():	
	get_num = int(raw_input("Number : "))
	get_next_num = int(raw_input("Next number : "))
	added  = get_num % get_next_num
	return(added)

def calcy(add , subtract , mult , divide , modul):
	get_op = raw_input("Add or Subtract or Multiply or Divide or Modulo : ")
	
	if get_op.strip() == "Add":
		return(add())
	
	elif get_op.strip() == "Subtract":
		return(subtract())
	
	elif get_op.strip() == "Multiply":
		return(mult())
	
	elif get_op.strip() == "Divide":
		return(divide())
	
	elif get_op.strip() == "Modulo":
		return(modul())
	
	else:
		return("Invalid Input. Try again.")

def exp_calcy():
	try:
		expression = raw_input("Expression : ")
		expressed = eval(expression)
		return(expressed)
	except NameError and TypeError and ValueError:	
		return("Invalid Expression. Try again.")



print("Hello,")
while(True):
	print(" ")
	start_or_end = raw_input("Start or End : ")
	
	if start_or_end.strip() == "Start":
		
		print("Enter help for info.")
		which_calc = raw_input("Calcy or Exp calcy(Exp = Expression) : ")
		
		if which_calc.strip() == "Calcy":
			print(calcy(addition, subtraction, multiplication, division, modulo))
			continue

		elif which_calc.strip() == "Exp calcy":
			print(exp_calcy())
			continue

		elif which_calc.strip() == "help":
			print("Calcy: mode is normal classic two digit calculator which can calculate only two digits.\nExp calcy: (Expression 	Calculator)in this mode you can enter expression and get the desired output.")
			continue
		
		else:
			print("Invalid Input. Try again.")
			continue	

	elif start_or_end.strip() == "End":
		break

	else:
		print("Invalid Input. Try again.")
		continue

