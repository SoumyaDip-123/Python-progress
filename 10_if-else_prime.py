# Check if a number is prime

num = int(input("Enter the number : "))
is_prime = True # For prime 

if num <= 1:
    is_prime = False # For not a prime num
else:
    for i in range (2, int(num**0.5)+1): 
        if num % 2 == 0:
            is_prime = False
        
if is_prime:
    print("Is Prime:",num)
else:
    print("Not Prime:",num)