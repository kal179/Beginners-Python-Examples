

class Calculator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		added = self.num1 + self.num2
		return(added)

	def subtract(self):
		subtracted = self.num1 - self.num2
		return(subtracted)

	def multiply(self):
		multiplied = self.num1 * self.num2	
		return(multiplied)

	def divide(self):
		divided = self.num1 / self.num2
		return(divided)

	def modulo(self):
		mod = self.num1 % self.num2
		return(mod)	

	def exponent(self):
		power = self.num1 ** self.num2
		return(power)

class Expression:
	def __init__(self, expression):
		self.expression = expression

	def evaluate_expression(self):
		evaluated = eval(self.expression)
		return(evaluated)		

while(True):
	start_or_end = str(input("Start or End : "))
	if start_or_end.strip() == "Start":
		
		calc_or_exp = str(input("Calc or Expression Calc : "))
		if calc_or_exp in ["Calc", "calc"]:

			get_op = str(input("Add or Subtract or Multiply or Divide or Exponent or Modulo : "))

			if get_op == "Add":
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				add = Calculator(num, next_num)
				print(add.add())

			elif get_op == "Subtract":	
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				subtract = Calculator(num, next_num)
				print(subtract.subtract())

			elif get_op == "Multiply":	
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				multiply = Calculator(num, next_num)
				print(multiply.multiply())

			elif get_op == "Divide":	
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				divide = Calculator(num, next_num)
				print(divide.divide())
				
			elif get_op == "Exponent":	
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				exponent = Calculator(num, next_num)
				print(exponent.exponent())
				
			elif get_op == "Modulo":	
				num = float(input("Number : "))
				next_num = float(input("Next Number : "))
				modulo = Calculator(num, next_num)
				print(modulo.modulo())

			else:
				print("Invalid Input.Try again!")

		elif calc_or_exp in ["Expression calc", "expression calc","expression"]:
			get_expression = str(input("Expression : "))
			expressed = Expression(get_expression)
			print(expressed.evaluate_expression())		

		else:
			print("Invalid Input.Try again!")		

		continue		

	else:
		break	