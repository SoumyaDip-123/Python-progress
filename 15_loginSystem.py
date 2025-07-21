# Nested If-Else: Login System

username = input("Enter valid username: ")
password = input("Enter valid password: ")

if username == "admin" :
    if password == "1234":
        print("Login successful.")
    else:
        print("Invalid password.")
        
else:
    print("Username not found:")