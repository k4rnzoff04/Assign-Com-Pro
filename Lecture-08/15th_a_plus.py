def a_plus():
    with open("a_plus.txt", "w+") as file:
        # file.seek(0)

        content = file.read()
        print("Current content of the file: ")
        print(content)

        file.write("Appending a new line at the end.\n")

        file.seek(0)
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)

a_plus()