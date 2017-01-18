import bsddb
import os

def new_db(name = "my_db"):
	os.chdir("D:\\")
	db = bsddb.btopen(name + ".db" , "c")
	db["Default"] = "Erika"
	return db["Default"]
	db.close()

get_db_name = str(raw_input("db name : "))
print new_db(get_db_name)	
