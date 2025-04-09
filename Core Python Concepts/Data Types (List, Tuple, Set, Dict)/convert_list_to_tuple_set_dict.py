#Q1: Convert the following list into a tuple, set, and dictionary.

data = ['apple', 'banana', 'cherry']
print("List:", data)

tuple_data = tuple(data) 
print("Tuple:", tuple_data)

set_data = set(data)
print("Set:", set_data)

dict_data = {i: v for i, v in enumerate(data)}
print("Dictionary:", dict_data)
# Output:
# List: ['apple', 'banana', 'cherry']
# Tuple: ('apple', 'banana', 'cherry')
# Set: {'banana', 'apple', 'cherry'}
# Dictionary: {0: 'apple', 1: 'banana', 2: 'cherry'}
