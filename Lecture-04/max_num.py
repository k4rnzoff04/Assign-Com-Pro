max = 5

total = 0.0

print(f"This program calculates the sum of {max} " \
     + "numbers you will enter")

for counter in range(max):
    number = int(input("Enter a number : "))
    total += number

print(f"The total is {total}")