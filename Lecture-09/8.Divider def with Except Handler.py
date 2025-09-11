def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"Error Exception: {e}")
    else:
        return result

try:

    a, b = map(int, input("Enter number(Ex.: 20 10): ").split())

except Exception as e:
    print(f"Exception: {e}")
    print("End program")
    exit()

print(f"Result: {divide(a, b)}")
