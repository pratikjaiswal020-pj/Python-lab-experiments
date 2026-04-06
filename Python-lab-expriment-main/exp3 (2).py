import math
a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
c = int(input("Enter third number :- "))

d = b*b - 4*a*c
if d > 0 :
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots :- ",r1,r2)
elif d == 0:
    r = -b / (2*a)
    print("One real root :- ",r)
else :
    print("No real roots")    