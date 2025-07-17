rows = int(input("How many rows? : "))

num = int(input("How many numbers? : "))

for i in range(1, rows):
    print(i)
    for j in range(1, num):
        
         if j < num:
            print(j, end=" ")
              
    print()