def is_armstrong(num):
    num_str = str(num)
    len_num = len(num_str)

    total = 0
    for digit in num_str:
        total += int(digit) ** len_num
    return total == num


print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))


