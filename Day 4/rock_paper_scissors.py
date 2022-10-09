import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
pc_choice = random.randint(0, 2)

if user_choice > 2 or user_choice < 0:
    print("Invalid choice, You lost")
else:
    print("You Chose: ")
    print(options[user_choice])
    print("Pc Chose: ")
    print(options[pc_choice])

    if user_choice == pc_choice:
        print("Draw!")
    elif (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
        print("You win!")
    else:
        print("You lost")

# Option 2:
# if user_choice == pc_choice:
#     print("Draw")
# elif pc_choice == 0 and user_choice == 2:
#     print("You lost")
# elif user_choice == 0 and pc_choice == 2 or user_choice > pc_choice:
#     print("You won")
# else:
#     print("You lost")
