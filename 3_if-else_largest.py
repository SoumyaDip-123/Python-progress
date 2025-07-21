# 3. Find the largest of two numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if a >= b:
    print("Largest number :",a)
elif b >= a:
    print("Largest number :",b)
else:
    print("Invalid input!")
