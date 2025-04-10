from functools import reduce

# Using reduce() to calculate factorial
# Factorial of a number n is the product of all integers from 1 to n
n = 5  # Example number
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"Factorial of {n} is {factorial}")

# Explanation:
# 1. Lambda: A lambda function is an anonymous function defined using the `lambda` keyword.
#    In this case, `lambda x, y: x * y` is used to multiply two numbers.
# 2. reduce(): The `reduce()` function applies a rolling computation to a sequence of items.
#    Here, it multiplies all numbers in the range from 1 to n to compute the factorial.
#    Example: For n=5, reduce() computes (((1*2)*3)*4)*5.
# 3. map(): The `map()` function applies a given function to all items in an iterable.
#    Example: `map(lambda x: x**2, [1, 2, 3])` returns [1, 4, 9].
# 4. filter(): The `filter()` function filters elements in an iterable based on a condition.
#    Example: `filter(lambda x: x % 2 == 0, [1, 2, 3, 4])` returns [2, 4].
