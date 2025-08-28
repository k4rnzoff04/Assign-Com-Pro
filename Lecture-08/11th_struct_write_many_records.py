import struct

num_records = int(input("How many records do you want to create? "))

with open("records.bin", "wb") as outfile:

    for i in range(num_records):
        id_num = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))

        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)

        outfile.write(data)

print(f"{num_records} record have been written to records.bin")
