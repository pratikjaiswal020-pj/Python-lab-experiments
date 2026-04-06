l = []
for i in range(0,5):
    l.append(input("Enter the "+str(i)+"th fruit name :- "))

print("The entered fruit names are :- ", end=" ")
for i in range(0,5):
    print(l[i], end=", ")