#  Check if a cheracter is a vowel or consonant

ch = input("Enter the cheracter: ")
   
if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input. Please enter a single alphabet letter.")
