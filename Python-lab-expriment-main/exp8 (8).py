
def SI(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter the principal amount :- "))
r = float(input("Enter the rate of interest :- "))
t = float(input("Enter the time period in year :- "))

print("Simple interest is", SI(p, r, t))