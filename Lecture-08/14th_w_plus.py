def write_plus():
    with open("w_plus.txt", "w+") as file:
        file.write("Hello World!\n")
        file.write("This is a test file.\n")

        file.seek(0)
        content = file.read()
        print(content)

write_plus()