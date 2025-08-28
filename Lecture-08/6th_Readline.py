with open("philosophers.txt", "r") as file:
    Line = file.readline()
    while Line:
        print(Line.strip())
        Line = file.readline()