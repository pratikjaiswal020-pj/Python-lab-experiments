
def fact(a):
    return (1 if a == 1 else a*fact(a-1))
      
a = int(input("Enter a number :- "))
print(f"The factorial of {a} is {fact(a)}")