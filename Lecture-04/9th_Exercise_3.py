rows = int(input("How many rows? : "))

num = 100 // rows

for i in range(rows):
    for j in range(1, num + 1):
        print(i * num + j, end= ' ')
    print()