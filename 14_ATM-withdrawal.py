# ATM withdrawal system

balence = 50000
withdraw = int(input("Enter valid input :"))

if withdraw <= 0:
    print("Invalid input !")
elif balence < withdraw:
    print("Insufficient money.")
else:
    balence -= withdraw
    print(f"Withdraw successful: Remaining balence: {balence}")
    