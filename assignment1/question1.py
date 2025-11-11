'''Write a Python script that:
Asks the user to enter a decimal number (float).
Converts the number into an integer and a string.
Displays all three values (original float, integer, and string) using string formatting.
'''

number = input("Enter a decimal number: ")
float_num = float(number)
int_num = int(float_num)
str_num = str(float_num)

# used f-string: because it allows variables directly inside the brackets {}. easy for now.
print(f"Original float: {float_num: .3f}") #float upto 3 decimal places only
print(f"Converted to integer: {int_num}")
print(f'Converted to string: "{str_num}"')
