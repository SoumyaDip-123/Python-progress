# Q: What's the tax rate for ₹5,00,000? 2.5l 0% , 50l 5%, 100l 20% else 30 %

income = int(input("Enter the income : "))
if income <= 250000:
    print("No tax")
elif income <= 500000:
    print("5 % tax")
elif income <= 1000000:
    print("20% tax")
else:
    print("30 % tax")