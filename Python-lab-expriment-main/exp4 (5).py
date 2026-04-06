n = int(input("Enter a number :- "))
temp = n
sum = 0
while(n != 0):
    sum += (n%10)
    n //= 10
print(f"The sum of all the digit of {temp} is {sum}")