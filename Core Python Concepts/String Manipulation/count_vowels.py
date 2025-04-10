def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
string = "Hello World"
print("Number of vowels:", count_vowels(string))

#Version 2.0

# def count_vowels(input_string):
#     # Define a string containing all vowels (both lowercase and uppercase)
#     vowels = "aeiouAEIOU"
    
#     # Initialize a counter variable to keep track of the number of vowels
#     count = 0
    
#     # Iterate through each character in the input string
#     for char in input_string:
#         # Check if the current character is in the vowels string
#         if char in vowels:
#             # If it is a vowel, increment the counter by 1
#             count += 1
    
#     # Return the total count of vowels found in the input string
#     return count

# # Example usage
# string = "Hello World"  # Define a sample string
# # Call the count_vowels function with the sample string and print the result
# print("Number of vowels:", count_vowels(string))
