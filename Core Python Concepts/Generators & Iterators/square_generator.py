# Generator yielding squares
#def square_generator(n):
# This function generates squares of numbers from 0 to n-1.
# The 'yield' keyword is used to produce a value and pause the function's state.
def square_generator(n):
    for i in range(n):
        yield i ** 2  # Yield the square of the current number 'i'

# Example usage:
if __name__ == "__main__":
    n = 5
    for square in square_generator(n):
        print(square)

# Explanation:
# - Generators are a way to create iterators in Python.
# - The 'yield' statement allows the function to return a value and resume later.
# - This is memory-efficient because it doesn't store all the squares in memory at once.
# - You can iterate over the generator to get the squares one by one.
