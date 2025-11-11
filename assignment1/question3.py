'''Write a program that:
Asks the user to enter a word and a starting index.
Extracts and prints the substring from that index to the end using string slicing.
'''

word = input("Enter a word: ")
start_index = int(input("Enter the starting index: "))
substring = word[start_index:]
print(f"Substring from index {start_index} to end: '{substring}'")
