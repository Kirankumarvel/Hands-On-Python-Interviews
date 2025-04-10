# Generator expression
gen_exp = (x**2 for x in range(5))  # Creates a generator that yields squares of numbers from 0 to 4

# Using next() to retrieve values from the generator
print(next(gen_exp))  # Output: 0 (0 squared)
print(next(gen_exp))  # Output: 1 (1 squared)
print(next(gen_exp))  # Output: 4 (2 squared)

# The generator maintains its state, so it continues from where it left off
print(next(gen_exp))  # Output: 9 (3 squared)
print(next(gen_exp))  # Output: 16 (4 squared)

# If you call next() after the generator is exhausted, it raises StopIteration
try:
    print(next(gen_exp))  # This will raise StopIteration
except StopIteration:
    print("Generator is exhausted")
