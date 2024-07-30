print("*"*10,"ANURAG UNIVERSITY","*"*10)

import re

rollno = input("Enter ROLL NUMBER : ")
au = re.fullmatch('[2][3][E][G][112]{3}[A-Z][01-66]{2}')
if rollno != None :
                print("VALID ROLL NUMBER")
else :
                print("NOT VALID")
