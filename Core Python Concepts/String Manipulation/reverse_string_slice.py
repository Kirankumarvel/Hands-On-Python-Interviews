# Reverse a string using slicing
def reverse_string(s):
    # Slice the string from end to start
    return s[::-1]

# Example usage
original_string = "Interview"
print("Original String:", original_string)
print("Reversed String:", reverse_string(original_string))
