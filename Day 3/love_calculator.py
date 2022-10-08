# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_names = (name1 + name2).lower()
# TRUE LOVE
t_count = combined_names.count("t")
r_count = combined_names.count("r")
u_count = combined_names.count("u")
e_count = combined_names.count("e")
l_count = combined_names.count("l")
o_count = combined_names.count("o")
v_count = combined_names.count("v")
e_count = combined_names.count("e")

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count
percentage_love = int(f"{true_count}{love_count}")

if percentage_love < 10 or percentage_love > 90:
    print(
        f"Your score is {percentage_love}, you go together like coke and mentos.")
elif percentage_love >= 40 and percentage_love <= 50:
    print(f"Your score is {percentage_love}, you are alright together.")
else:
    print(f"Your score is {percentage_love}.")
