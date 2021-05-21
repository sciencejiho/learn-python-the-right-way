# Print the date and time based on the following format.
#
# Example 1:
# Output: 2020/12/25 11:59:59

# declare variables for the date and time
year = 2020
month = 12
day = 25
hour = 11
minute = 59
second = 59

# date format (YYYY/MM/DD)
# ! make sure to not print new line in the end
print(year, month, day, sep = '/', end = ' ')
# time format (HH:MM:SS)
print(hour, minute, second, sep = ':')
