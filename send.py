import os
import sys
import requests

filename = sys.argv[1]

file_found = False

for i in (os.listdir(os.getcwd())):
    if (i == filename):
        file_found = True
        
if (not file_found):
    print "The file '" + filename + "' could not be found."
    exit(0)
    
file = {'file': open(filename, 'rb')}

password = str(raw_input("Enter password for protection, or press 'Enter' to skip:"))

if (password == ""):
    password = "null"
    
r = requests.post("http://sharecode.co.nf/server.php?filename="+filename+"&password="+password,files=files)

print r.text

