# keep_going = "y"

while True:
    rows = int(input("How many rows? : "))
    columns = int(input("How may columns? : "))
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()