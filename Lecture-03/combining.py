age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

# ตรวจสอบเงื่อนไขการอนุมัติเงินกู้
# เงื่อนไข: อายุระหว่าง 18 ถึง 65 ปี และรายได้มากกว่า 30,000 บาท
if age >= 18 and age <= 65 and income > 30000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")