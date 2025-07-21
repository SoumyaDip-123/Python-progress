# 17. Nested Conditions in Shopping Cart

# Q: Apply discount if member and cart total > ₹1000

is_member = True
cart_total = int(input("Total cart amount :"))

if is_member:
    if cart_total >= 1000:
        print("Discount Applied")
    else:
        print("No discount applied ! Amount less then 1000")
else:
    print("Is not a Member!")