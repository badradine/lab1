x=int(input("enter the value of a: "))
y=int(input("enter the value of b: "))
z=int(input("enter the value of c: "))

import math
p=((y**2)-(4*x*z))

if p==0:
    s = math.sqrt(p)
    a1 = (-y + s) / (2 * x)
    a2 = (-y - s) / (2 * x)
    print("The value of x is: ", a1)
elif p<0:
    print("no result")
else:
    s = math.sqrt(p)
    a1 = (-y + s) / (2 * x)
    a2 = (-y - s) / (2 * x)
    print("the roots of a are: ", a1, "and", a2)


