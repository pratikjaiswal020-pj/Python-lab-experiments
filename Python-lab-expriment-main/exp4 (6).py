n = int(input("Enter a number :- "))
fact = 1
temp = n
while(n >= 1):
    fact *= n
    n -= 1
print(f"factorial of {temp} is {fact}")