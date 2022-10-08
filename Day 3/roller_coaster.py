print("Welcome to the deno roller coaster")

height = int(input("What's your current height? "))

if height > 120:
    age = int(input("Your age? "))
    total_bill = 0

    if age < 12:
        total_bill += 5
        print("Ok Kid, your ticket is 5$")
    elif age <= 18:
        total_bill += 7
        print("Ok teenager, your ticket is 7$")
    elif age >= 45 and age <= 55:
        print("Everything is ok, have a free ride on us")
    else:
        total_bill += 12
        print("Your ticket is 12$")

    add_photo = input("Do you want photos?(yes/no)? ")
    if add_photo == "yes" or add_photo == "y":
        total_bill += 3

    print(f"Your total bill is {total_bill}")
else:
    print("You cannot ride the rollercoaster 🥲")
