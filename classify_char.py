#16. Detect Character Type (Digit, Alpha, Special)
# Q: Classify '@'

char = input("Enter the character :")

if char.isdigit():
    print("Digit")
elif char.isalpha():
    print("Alphabet")
else:
    print("Special character")