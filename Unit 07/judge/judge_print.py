# Given the date and time as an input, 
# return the date and time based on the following format.
#
# Example 1:
# Input: 1999 12 31 10 37 21
# Output: 1999-12-31T10:37:21
#
# Example 2:
# Input: 2017 10 27 11 43 59
# Output: 2017-10-27T11:43:59

# get the input and declare variables accordingly
year, month, day, hour, minute, second = input().split()

# date format (YYYY-MM-DDT)
# ! make sure to print 'T' in the end
print(year, month, day, sep = '-', end = 'T')
# time format (HH:MM:SS)
print(hour, minute, second, sep = ':')
