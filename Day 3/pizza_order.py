print("Welcome to my Python Pizza store 🍕")

size = input("What size do you want? S, M or L?")
add_pepperoni = input("Do you want to add pepperoni? y or n? ")
add_extra_cheese = input("Do you want extra chewy cheese 🧀? y or n? ")

total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25

if add_pepperoni.lower() == "y" and size == "s":
    total_bill += 2
elif add_pepperoni.lower() == "y":
    total_bill += 3

if add_extra_cheese.lower() == "y":
    total_bill += 1


print(f"Here's your pizza 🍕, Total Bill {total_bill}$")
