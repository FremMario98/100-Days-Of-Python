total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(f"Total of even numbers --> 1 + ... + 100 = {total}")

total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(f"Total of even numbers --> 1 + ... + 100 = {total2}")
