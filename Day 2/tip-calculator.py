print('Welcome to tip calculator my friends')
total_bill = float(input('What was the total bill? '))
tip_percentage = int(
    input('How much tip would you like to give? 12, 15, 20 or ...? '))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill * (1 + tip_percentage / 100)) / number_of_people

rounded_bill_per_person = round(bill_per_person, 2)
print(f'Each should pay {rounded_bill_per_person}$')
