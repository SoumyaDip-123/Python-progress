# Find the largest among three numbers

a = int(input("Enter 1st Number :"))
b = int(input("Enter 2st Number :"))
c = int(input("Enter 3st Number :"))

if a >= b and a >= c:
    print("Largest number :",a)
elif b >= a and b >= c:
    print("Largest number :",b)
elif c >= a and c >= b:
    print("Largest number :",c)
else:
    print("Invalid Input !")