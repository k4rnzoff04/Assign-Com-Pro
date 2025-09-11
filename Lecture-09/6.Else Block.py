try:
    value = int(input("Enter a number: "))
    result = 10 / value
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"The result is {result}")


print("End of program")