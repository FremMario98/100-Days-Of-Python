# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height ** 2)
rounded_bmi = round(bmi, 2)

if rounded_bmi < 18.5:
    print('Underweight')
elif rounded_bmi < 25:
    print('Perfect! Keep it up')
elif rounded_bmi < 30:
    print('Slightly overweight')
elif rounded_bmi < 35:
    print('Obese!')
else:
    print('Clinically obese! Go see a doctor')
