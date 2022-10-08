weight = float(input("What's your current weight? "))
height = float(input("What's your height in meters? "))

bmi = int(weight / (height ** 2))

print(f"Your bmi is {bmi}")
