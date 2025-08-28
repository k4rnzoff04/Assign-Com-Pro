with open("sales.txt", "r") as sales_file:
    total = 0.0
    for line in sales_file:
        amount = float(line)
        total += amount

        print(f"Sales amount: {amount:.2f}")

    
    print(f"Sales total: {total:.2f}")