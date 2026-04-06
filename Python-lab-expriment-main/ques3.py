
inp = input("Enter a string :- ")
LIST1 = inp.split(" ")
print(LIST1)
print("\nElements of LIST1 with index are :- ")
for i,v in enumerate(LIST1):
    print(i,v)
LIST2 = [x for x in range(len(LIST1))]
LIST3 = list(zip(LIST1,LIST2))
print(LIST3)