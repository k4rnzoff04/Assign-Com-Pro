from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

even_squared_numbers = list(filter(lambda x : x % 2 == 0, squared_numbers))
print(even_squared_numbers)

sum_of_even_squared_numbers = reduce(lambda x, y: x + y, even_squared_numbers)
print(sum_of_even_squared_numbers)