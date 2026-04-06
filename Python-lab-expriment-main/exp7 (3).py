
inp = input("Enter a paragraph :- ")
l = inp.split()
print("The paragraph contains", len(l), "words .")
count = 0
for i in l:
    if i == i[::-1]:
        count+=1
print("Palindrome = ", count)
print("Printing the words in reversed order :- ")
for i in l:
    print(i[::-1])