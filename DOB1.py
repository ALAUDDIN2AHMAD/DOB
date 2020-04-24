from datetime import datetime
DOB = input("Enter your DOB with \
format like  24/11/1978\n")
x = datetime.strptime(DOB, \
                      "%d/%m/%Y")
ddd = abs(datetime.now()-x).days
y = int(ddd//365.2425)
r = ddd % 365.2425
m = int(r//30.436875)
d = int(ddd - (y*365.2425 + m*30.436875))
print("Your age is: %d years,\
%d months, and %d days"%(y,m,d))
