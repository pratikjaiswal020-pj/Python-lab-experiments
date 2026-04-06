
m = int(input("Enter the starting of the natural number :- "))
n = int(input("Enter the ending of the natural number :- "))
print("The prime numbers are :- ",end="")
for i in range(m,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i, end=", ")