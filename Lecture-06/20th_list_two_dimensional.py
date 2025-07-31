import random

ROWS = 3
COLS = 4

def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],]
    
    for i in range(ROWS):
        for j in range(COLS):
            values[i][j] = random.randint(1, 100)
    
    print(values)

main()