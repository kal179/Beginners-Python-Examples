
import os
import platform as plt

def ping_host(host_name):
	ping_str = "-c 1"
	if plt.system().lower() == "Windows":
		ping_str = "-n 1"
	ping = "ping " + ping_str + " " + host_name
	resp = os.system(ping)
	return resp == 0
	
# Test 
test_host = "www.google.co.in"
result = ping_host(test_host)
if result:
	print("\nStatus ({}): Is Alive".format(test_host))
else:
	print("\nStatus ({}): Is Dead".format(test_host))
