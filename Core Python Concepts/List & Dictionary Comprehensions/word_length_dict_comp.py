# Word-length dictionary using dict comprehension
# Step 1: Define a list of words
# The list `words` contains a set of strings for which we want to calculate the length.
words = ["interview", "preparation", "python", "code", "example"]

# Step 2: Create a dictionary using dictionary comprehension
# The dictionary comprehension iterates over each word in the `words` list.
# For each word, it calculates the length using the built-in `len()` function.
# The word itself becomes the key, and its length becomes the value in the dictionary.
word_length_dict = {word: len(word) for word in words}

# Step 3: Print the resulting dictionary
# The `print()` function outputs the dictionary to the console.
# The dictionary will look like this:
# {'interview': 9, 'preparation': 11, 'python': 6, 'code': 4, 'example': 7}
print(word_length_dict)


"""
Process Breakdown:
Input Data: A list of words is defined (words).
Dictionary Comprehension:
Iterates over each word in the list.
Uses len(word) to calculate the length of each word.
Constructs a dictionary where each word is a key, and its length is the corresponding value.
Output: The resulting dictionary is printed to the console.
This approach is concise and leverages Python's dictionary comprehension for clean and efficient code.


"""
