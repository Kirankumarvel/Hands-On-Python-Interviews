# Using filter() to remove odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() applies the lambda function to each element in the list
# The lambda function checks if the number is even (i.e., divisible by 2)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Explanation:
# - filter(): Used to filter elements from an iterable based on a condition.
# - lambda: An anonymous function defined in a single line. Here, it checks if a number is even.
# - map(): Applies a function to all elements in an iterable and returns the transformed elements.
# - reduce(): Reduces an iterable to a single value by applying a function cumulatively (requires functools.reduce).
