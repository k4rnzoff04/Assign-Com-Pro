print("Please select operation - \n" \
"1. Add \n" \
"2. Subtract \n" \
"3. Multiply \n" \
"4. Divide \n")

choice = input("Select operations form 1, 2, 3, 4 : ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} x {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid Input")