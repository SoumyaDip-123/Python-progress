# Check if a given year, month, and day is a valid date

year = int(input("Enter the year :"))
month = int(input("Enter the month :"))
day = int(input("Enter the day :"))



if month < 1 or month > 12:
    print("Invalid Month.")
elif day < 1:
    print("Invalid Day.")
elif month in [1,3,5,7,8,10,12] and day <= 31:
    print("Valid Day")
elif month in [2,4,6,9,11] and day <= 30:
    print("Valid Day")
elif month == 2:
    leap = (year % 4 == 0 or year % 100 != 0) and (year % 400 == 0)
    if (leap and day <= 29) and (not leap and day <= 28):
        print("Valid Date For February.")
    else:
        print("Invalid Day For February.")
        
else:
    print("Invalid Day.")

