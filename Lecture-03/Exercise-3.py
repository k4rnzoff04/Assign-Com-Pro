h_worked = int(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate per: "))

gross_pay = h_worked * pay_rate

print(f"The gross pay is ${gross_pay:,.2f}")