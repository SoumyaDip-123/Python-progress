# Q: Is the number prime?


num = int(input("Enter the number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
        else:
            print("Is prime")
            
if is_prime:
    print(" Is prime")
else:
    print("Not prime")