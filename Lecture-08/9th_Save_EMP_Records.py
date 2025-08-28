num_emps = int(input("How many employee records do you want to create? "))

with open("employees.txt", "w") as emp_file:

    for count in range(1, num_emps + 1):
        print(f"Enter data for employee #{count}", end='')
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")

        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")

        print()

print("Employee records written to employees.txt.")

with open("employees.txt", "r") as content_file:
    lines = content_file.readlines()
    for line in range(0, len(lines), 3):
        name = lines[line].strip()
        id_num = lines[line + 1].strip()
        dept = lines[line + 2].strip()

        print(f"Name: {name}")
        print(f"ID: {id_num}")
        print(f"Department: {dept}")