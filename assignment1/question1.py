'''Write a Python script that:
Asks the user to enter a decimal number (float).
Converts the number into an integer and a string.
Displays all three values (original float, integer, and string) using string formatting.
'''

number = input("Enter a decimal number: ")
is_float = float(number)
is_int = int(is_float)
is_str = str(is_float)

# used f-string: because it allows variables directly inside the brackets {}. easy for now.
print(f"Original float: {is_float: .3f}") #float upto 3 decimal places only
print(f"Converted to integer: {is_int}")
print(f'Converted to string: "{is_str}"')
