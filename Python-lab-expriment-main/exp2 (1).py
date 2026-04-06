p = float(input("Enter the principal amount :- "))
r = float(input("Enter the rate of interest :- "))
t = float(input("Enter the time period in year's :- "))
n = int(input("Enter the number of times interest is compounded per year :- "))
si = (p*r*t)/100
print("Simple interest is :- ",si)
a = p*(1 + r/n)**(n*t)
ci = a - p
print("Coumpond interest is :- ",ci)