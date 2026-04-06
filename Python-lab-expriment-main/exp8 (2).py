
def check(a):
    return "Even" if a%2==0 else "Odd"
n =int(input("Enter a number :- "))
print(n, "is", check(n))