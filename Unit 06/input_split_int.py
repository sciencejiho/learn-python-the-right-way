# Given two integers as an input, return its sum.
#
# Example 1:
# Input: 10 20
# Output: 30

# get the string as an input, and split them into a and b
a, b = input('Enter two integers: ').split()

# ! cast a and b, which are currently string, as integer
a = int(a)
b = int(b)

# print the sum of a and b
print(a + b)
# this also works:
# print(int(a) + int(b))
