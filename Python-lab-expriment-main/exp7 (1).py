
m = int(input("Enter the starting of the natural number :- "))
n = int(input("Enter the ending of the natural number :- "))
l = [x for x in range(m,n+1)]
print("The sum of the list is :- ", sum(l))
print("The average of the list is :- ", (sum(l)/len(l)))
print("The largest element in the list is :- ", max(l))
print("The smallest element in the list is :- ", min(l))
l2 = [x for x in l if x%3!=0]
print("The element which are not divisible 3 are :- ", l2)