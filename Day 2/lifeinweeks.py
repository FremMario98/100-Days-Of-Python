age = int(input("Age: "))
# let me live till 60 max 😂😂
expected_living_age = 90

years_left = expected_living_age - age

months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(
    f"You still have {days_left} days, {weeks_left} weeks, and {months_left} months left")
