#Example I
age = input("Enter your age: ")
age = int(age)

height = input("Enter your height: ")
height = float(height)
print("You are " + str(age) + " years old and " + str(height) + " feet tall.")
#หรือ
print(f"You are {str(age)} years old and {str(height)} feet tall.")

# Example II
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.6f}")

#Example III
celsius = float(input("Enter temerature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is {fahrenheit}")