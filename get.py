import os
import sys
import requests

file_name = sys.argv[1] 
password = str(raw_input("Enter the password for the file"))

if (password == ""):
    password = "null"

r = requests.post("http://sharecode.co.nf/getcode.php?filename="+file_name+"&password="+password+"&getname=true")
local_name = r.text

r = requests.post("http://sharecode.co.nf/getcode.php?filename="+file_name+"&password="+password)
if (r.text == "False"):
    print "Wrong combination of filename and password"
    exit(0)

for i in os.listdir(os.getcwd()):
	if (i == local_name):
		print "A file with the name " + local_name + " already exists"
		new_name = str(raw_input("Enter new file name "))
		if (new_name != ""):
			local_name = new_name
		break
		
file = open(local_name,'w+')
file.write(r.text)
file.close()


