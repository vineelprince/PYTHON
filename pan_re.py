import re

s = input("Enter PAN NUMBER : ")
matcher = re.fullmatch('[A-Z]{5}[0-9]{4}[A-Z]',s)
if matcher != None :
                print("VALID","---->","YOUR PAN NUMBER IS : ",s)
else :
                print("NOT VALID")
