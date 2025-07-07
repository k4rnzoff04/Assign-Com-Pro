st_score = float(input("Enter your first score: "))
nd_score = float(input("Enter your second score: "))
rd_score = float(input("Enter your third score: "))

avg = (st_score + nd_score + rd_score) / 3
print(f"The average score is {avg:.2f}")

if avg > 95 :
    print("Congratulations!")