# syntax
# [i for i in iterable if expression]

# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# syntax
""" x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3)) """


""" add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))
 """
print((lambda a, b: a + b)(2, 3))

square: int = lambda x: x**2
print(square(3))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [i for i in numbers if i < 0]
print(f"Los numeros negativos son: {negatives}")

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

only = [x for sublist in list_of_lists for inner_list in sublist for  x in inner_list]
print(only)

# It is also possible to make a list of tuples
numbers = [(i, i ** 0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(numbers)  