'''Write a Python program that takes a list of words and finds all words that appear more than once, storing them in a dictionary with their frequency count.
Example Input/Output:
Input: ["apple", "banana", "apple", "orange", "banana", "banana"]
Output: {'apple': 2, 'banana': 3}
'''

words = input("Enter words separated by spaces: ").split()

frequency = {}
duplicates = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word in frequency:
    if frequency[word] > 1:
        duplicates[word] = frequency[word]

print("Repeated words:", duplicates)
