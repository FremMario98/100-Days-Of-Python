import random

names_string = input(
    "Give me everbody's name seperated by a comma then space name: ")

names = names_string.split(", ")
names_len = len(names)

who_pays = names[random.randint(0, names_len - 1)]

print(f"{who_pays} will pay the bill😉")
