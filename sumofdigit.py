# Sum of digit of a number
'''num = int(input("Enter numbers: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10 # to find the last digit of a numbers and add sum_digits(123 % 10 ->3 // 12-> 2 // 1->1)
    num //= 10 # remove the last digit (123 -> 12 -> 1 -> 0 end)
    
print(f"The sum of digits are : {sum_digits}")
'''

def sum_of_digits(num):
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    return sum_digits
num = int(input("Enter the number : "))
result = sum_of_digits(num)
print("The sum of digits is :",result)
    

