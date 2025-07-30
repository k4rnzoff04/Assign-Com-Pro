keep_going = "y"

while keep_going == "y":
    whole_sale = float(input("Enter the item's wholesale cost: "))
    retail_price = whole_sale * 2.5
    print(f"Retail price: ${retail_price:.2f}")

    keep_going = input("Do you want to continue? (Enter y/n): ")

print("Thank you for using the retail price calculator!")