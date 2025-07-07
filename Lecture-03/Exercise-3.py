h_worked = int(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate per: "))


if h_worked > 40:
    # gross_pay = ((h_worked - 40) *1.5*pay_rate) + (40 * pay_rate)
    overtime_hours = h_worked - 40
    gross_pay = (overtime_hours * (1.5 * pay_rate) + (40 * pay_rate))
    
else:
    gross_pay = h_worked * pay_rate



print(f"The gross pay is ${gross_pay}")