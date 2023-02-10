x=int(input("enter the value of a: "))
y=int(input("enter the value of b: "))
z=int(input("enter the value of c: "))

import math
s = math.sqrt((y**2)-(4*x*z))

a1 = (-y+s)/(2*x)
a2 = (-y-s)/(2*x)

print("the roots of a are:", a1, "and", a2)