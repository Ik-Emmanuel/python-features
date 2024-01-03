# map 
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (9/5) * c + 32, celsius_temps))
print(fahrenheit_temps)


# filter
# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# reduce
from functools import reduce

# Example 1: Sum all elements in a list
numbers = [1, 2, 3, 4, 5, 10]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


# Example: Check if any or all numbers are greater than 5
numbers = [3, 7, 2, 8, 1]
print(any(x > 5 for x in numbers))
print(all(x > 5 for x in numbers))