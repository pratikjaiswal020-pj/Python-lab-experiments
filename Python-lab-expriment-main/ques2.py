
d = {}
n = int(input("Enter number of key-value pair :- "))
for i in range(n):
    k = input("Enter key :- ")
    v = input("Enter value :- ")
    d[k] = v
rev = {}
for k,v in d.items():
    rev[v] = k
print("The original dictionary is :- ", d)
print("The new dictionary is :- ", rev)
