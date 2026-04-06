a = 0
b = 1
sum = 0
print("Fibonacci series between 0 to 1000 is :- ")
for i in range(1000):
    if(a > 1000):
        break
    print(a, end = ", ")
    if(a%2 == 0):
        sum += a
    temp = a
    a = b
    b = temp + b
print("\nAnd the sum of all the even terms is :- ", sum)