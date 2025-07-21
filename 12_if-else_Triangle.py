# Find the type of triangle (scalene, isosceles, equilateral)
a = int(input("Enter first value :"))
b = int(input("Enter second value :"))
c = int(input("Enter third value :"))

if a == b == c:
    print("This is equilateral.")
elif a == b or b == c or c == a:
    print("This is isosceles.")
else:
    print("this is scalene.")