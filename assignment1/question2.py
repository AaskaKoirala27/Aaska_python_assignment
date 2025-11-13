'''Write a program that:
Ask the user for their full name.
Extracts the first letter of the first and last name using string slicing.
Displays the initials in uppercase.
'''

full_name = input("Enter your full name: ")

name_split = full_name.split() #splits the full name into parts. like "Aaska Koirala"-> "Aaska", "Koirala"
if len(name_split) >= 2:
    first_name = name_split[0][0] #takes the first name and its first letter
    last_name = name_split[-1][0] #takes the last name and its first letter
    initials = (first_name + last_name).upper()
    print(f"Your initials are: {initials}")
else:
    print("Something went wrong.Please enter your first and last name both: ") #if someone only enters first or last name, this will showup.