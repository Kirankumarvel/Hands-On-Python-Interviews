# Using map() and lambda to square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Explanation:
# 1. Lambda: A lambda function is an anonymous function defined using the `lambda` keyword. 
#    Here, `lambda x: x ** 2` is a function that takes an input `x` and returns its square.
# 2. map(): The `map()` function applies a given function (in this case, the lambda function) 
#    to each item in an iterable (like a list) and returns a map object. 
#    We convert it to a list using `list()` to see the results.
# 3. filter(): This function is used to filter elements from an iterable based on a condition.
#    It is not used here but is useful for filtering data.
# 4. reduce(): This function (from `functools`) is used to apply a rolling computation to a sequence 
#    (e.g., summing all elements). It is not used here but is helpful for cumulative operations.
