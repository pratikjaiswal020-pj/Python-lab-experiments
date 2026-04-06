a = float(input("Enter first subject mark :- "))
b = float(input("Enter second subject mark :- "))
c = float(input("Enter third subject mark :- "))
d = float(input("Enter fourth subject mark :- "))
e = float(input("Enter fifth subject mark :- "))
sum = a+b+c+d+e
per = (sum/250)*100
if(per >= 90 and per <= 100) :
    print("Grade is O")
elif(per >= 80 and per < 90):
    print("Grade is E")
elif(per >= 70 and per < 80):
    print("Grade is A")
elif(per >= 60 and per < 70):
    print("Grade is B")
elif(per >= 50 and per < 60):
    print("Grade is C")
elif(per >= 0 and per < 50):
    print("Grade is F")