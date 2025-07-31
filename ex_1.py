# def cal_row(row):
#     num = 100 // row
#     for i in range(row):
#         for j in range(1,num + 1):
#             print(i * num + j ,end= '      ')
#         print()

# cal_row(10)
    

rows = int(input("Enter rows: ")) #รับค้าจำนวนแถวจาก User

num = 100 // rows #คำนวณจำนวนตัวเลขในแต่ละแถว
for i in range(rows): #วนลูปตามจำนวนแถวที่รับมา
    for j in range(1, num + 1): #วนลูปตามจำนวนตัวเลขในแต่ละแถว
        print(i * num + j, end = " ")
    print() #จบแถวแล้วขึ้นบรรทัดใหม่