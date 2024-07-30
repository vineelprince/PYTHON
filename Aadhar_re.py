import re

s = input("Enter AADHAR NUMBER : ")
date = input("Enter DATE OF BIRTH : ")
matcher = re.fullmatch('[1-9][0-9]{3}\s[0-9]{4}\s[0-9]{4}',s)
dob = re.fullmatch('[0123][0-9][.][0][]')

if matcher != None :
                print("VALID")
else :
                print("NOT VALID")



