# score = int(input("Enter your score: "))
# if score >= 80 and score < 100:
#     print("Grade : A")
# elif score >= 70:
#     print("Grade : B")
# elif score >= 60:
#     print("Grade : C")
# else:
#     print("Grade : D or F")

###############
#เริ่มเงื่นไขตรวจสอบที่ 60 คะแนนก่อน

score = int(input("Enter your score: "))
if score >= 60 and score < 70:
    print("Grade : C")
elif score >= 70 and score < 80:
    print("Grade : B")
elif score >= 80 and score < 100:
    print("Grade : A")
else:
    print("Grade : D or F")