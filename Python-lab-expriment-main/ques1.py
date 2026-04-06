
l = ["Apple","Banana","Mango"]
print("Fruits displayed from last to first index with their lengths :- ")
for i in l[::-1]:
    print(i, "- Length :", len(i))
print("/nList containing reverse of each fruit name :- ")
rev = []
for fruit in l:
    rev.append(fruit[::-1])
print(rev)