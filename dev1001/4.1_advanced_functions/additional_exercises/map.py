# Given a list of numbers, return a list with each number doubled.
nums = [1, 2, 3, 4, 5]
# → [2, 4, 6, 8, 10]

doubled_nums = map(lambda x: x*2, nums)
print(list(doubled_nums))

# Convert each name in the list to uppercase.
names = ['alice', 'bob', 'charlie']
# → ['ALICE', 'BOB', 'CHARLIE']

upper_name = map(lambda name: name.upper(), names)
print(list(upper_name))

# Return a list of squares of the numbers.
nums = [2, 3, 4]
# → [4, 9, 16]
squared = map(lambda x: x**2, nums)
print(list(squared))

# INTERMEDIATE LEVEL 
# Convert a list of strings into integers.
str_nums = ['1', '20', '300']
# → [1, 20, 300]

integer_nums = map(lambda num: int(num), str_nums)
print(list(integer_nums))

# Given a list of floats, return a list of strings formatted to 2 decimal places.
floats = [3.14159, 2.71828, 1.61803]
# → ['3.14', '2.72', '1.62']

strings_2d = map(lambda num: str(round(num, 2)), floats)
print(list(strings_2d))

# Add "$" to each price in the list.
prices = [10.5, 20.99, 5.0]
# → ['$10.50', '$20.99', '$5.00']

price_dollar_sign = map(lambda price: f"${price}", prices)
print(list(price_dollar_sign))

#CHALLENGE LEVEL