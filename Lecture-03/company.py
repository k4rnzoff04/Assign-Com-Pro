num_employees = int(input("Enter the number of employees: "))

if num_employees < 50:
    print("This is a small company.")

elif num_employees < 250:
    print("This is a medium-sized company.")

elif num_employees >= 250:
    print("This is a large company.")

else:
    print("Invalid input")