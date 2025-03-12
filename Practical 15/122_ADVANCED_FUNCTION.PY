from functools import reduce

# 1. Lambda function (Anonymous function)
square = lambda x: x ** 2
print("Square of 5:", square(5))

# 2. map() function - Applies a function to all items in an iterable
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# 3. reduce() function - Reduces an iterable to a single value
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)