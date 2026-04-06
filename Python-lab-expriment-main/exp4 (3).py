a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
c = int(input("Enter third number :- "))

while(b != 0):
    if(b == 0):
        break
    temp = a
    a = b
    b = temp%b

while(c != 0):
    if(c == 0):
        break
    temp = a
    a = c
    c = temp%c

print(a)