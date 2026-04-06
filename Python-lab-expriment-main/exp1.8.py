a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))

sum = a+b+c
s = sum/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area is : ", area)
print("Perimeter is : ", sum)