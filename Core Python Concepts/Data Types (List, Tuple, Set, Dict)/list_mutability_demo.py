#Q2: What will be the output?
a = [1,2,3]
b=a
b.append(4)
print("A:",a) # [1, 2, 3, 4]
print("B:",b) # [1, 2, 3, 4]
# Output: [1, 2, 3, 4] → because lists are mutable and both a and b point to the same object.
