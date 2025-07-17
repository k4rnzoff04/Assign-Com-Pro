input_string = input("Enter a string: ")#รับค่า string


modified_string = "" #ตัวแปรที่เก็บไว้ สำหรับเปลี่ยนแปลงค่า

vowels = "aeiouAEIOU" #ตัวแปรเก็บค่าตัวอักษรสระ ตัวเล็กตัวใหญ่

for char in input_string: #ลูป for สำหรับเช็คตัวอักษรในตัวแปรที่รับค่าเข้ามา
    upper_char = char.upper() #ให้ค่าในตัวแปร ปรับค่าเป็ฯตัวพิมพ์ใหญ่
    if upper_char in vowels: #สร้างเงื่อนไข ถ้าตัวอักษรที่รับเข้ามามีอักษรสระ
        modified_string += "*" #ให้แทนค่าเป็น *
    else:
        modified_string += upper_char #ถ้าไม่ใช่อักษรสระ ให้เป็นตัวพิมพ์ใหญ่ตามเดิม
    
print("Modified string: ", modified_string)