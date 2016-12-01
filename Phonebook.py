

phone = {}

class Phonebook:

	def __init__ ( self, fname, lname, phone_number, email, address ):
		
		self.fname = fname
		self.lname = lname
		self.phone_number = phone_number
		self.email = email
		self.address = address


	def view_info( self ):
		
		print( "Name : {} {}".format( self.fname, self.lname ) )
		print( "Phone number : {}".format( self.phone_number ) )
		print( "Email : {}".format( self.email ) )
		print( "Address : {}".format( self.address ) )

	def show_number( self ):
		
		return( "Phone number : {}".format( self.phone_number ) )
	
	def show_email ( self ):
		
		return( "Email : {}".format( self.email ) )		

def add():
	while (True):

		get_fname = str(input( "First name : " ))
		get_lname = str(input( "Last name : " ))
		get_phone_number = int(input( "Phone number : " ))
		get_email = str(input( "Email address : " ))
		get_address = str(input( "Home address : " ))

		full_name = get_fname + " " + get_lname

		phone[full_name] = Phonebook( get_fname, get_lname, get_phone_number, get_email, get_address )

		more = str(input("Do you want to add more [Y/n] : "))
		if more.strip() == "Y":
			print(" ")
			continue
		
		else:
			print(" ")
			break


def update():
	# still working here
	pass 	


def view_all():
	while (True):

                name = str(input( "Full name : " ))
		if name in phone.keys():
			print(phone[name].view_info())
		
		else:
			print("The name you entered does not exist.Try again")

		more = str(input("Do you want to view more [Y/n] : "))
		if more.strip() == "Y":
			print(" ")
			continue
		
		else:
			print(" ")
			break	


def number_contacts():
	num_of_contacts = 0
        for i in phone.keys():
            num_of_contacts += 1 
        return("Total number of contacts : {}".format(num_of_contacts))  


def view_number():
	while (True):

		name = str(input( "Full name : " ))
		if name in phone.keys():
			print(phone[name].view_number())
		
		else:
			print("The name you entered does not exist.Try again")

		more = str(input("Do you want to view more [Y/n] : "))
		if more.strip() == "Y":
			print(" ")  
			continue
		
		else:
			print(" ")  
			break


def view_email():	
	while (True):

		name = str(input( "Full name : " ))
		if name in phone.keys():
			print(phone[name].view_email())
		
		else:
			print("The name you entered does not exist.Try again")

		more = str(input("Do you want to view more [Y/n] : "))
		if more.strip() == "Y":
			print(" ")  
			continue
		
		else:
			print(" ")  
			break


def view_names():
	print("All contacts : ")	
	for i in phone.keys():
		print("   {}".format(i))

def delete():

	while (True):

		if len(phone.keys()) == 0:
			print("The contacts list is empty.")
			break

		name = str(input( "Full name : " ))
		if name in phone.keys():
			del phone[name]
			print("Contact deleted successfully.")

		else:
			print("The name you entered does not exist.Try again")

		more = str(input("Do you want to delete more [Y/n] : "))
		if more.strip() == "Y":
			print(" ")  
			continue
		
		else:
			print(" ")  
			break



print("========================Program Started========================")

print("Hello,")

while (True):	

	start_or_end = str(input( "Start or End : " ))
	if start_or_end.strip() == "Start" :
		
		op = str(input( "Add or Update or Delete or View : " ))
		if op.strip() == "Add":
			print(add())
			print(" ")  
			continue

		elif op.strip() == "Update":
			print(update())
			print(" ")  
			continue

		elif op.strip() == "Delete":	
			print(delete())
			print(" ")  
			continue

		elif op.strip() == "View":
			view_op = str(input("View all or View number or View email or View names: "))
			if view_op.strip() in [ "View all", "view all", "view All", "View all", "all" ]:
				print(view_all())
				print(" ")  
				continue

			elif view_op.strip() in [ "View number", "view number", "view Number", "View Number", "number" ]:
				print(view_number())	
				print(" ")  
				continue	

			elif view_op.strip() in [ "View email", "view email", "view Email", "View Email", "email" ]:
				print(view_email())
				print(" ")  
				continue

			elif view_op.strip() in [ "View names", "view names", "view Names", "View Names", "names" ]:
				print(view_names())
				print(" ")  
				print(number_contacts())
				print(" ")  
				continue	

			else:
				print("Invalid Input for View menu.")
				print(" ")  
				continue

		else:
			print("Invalid Input. Try again!")
			print(" ")  
			continue

	elif start_or_end.strip() == "End":
		print("=========================Program Ended=========================")
		break

	else:
		print("Invalid Input. Try again!")
		print(" ")  
		continue
