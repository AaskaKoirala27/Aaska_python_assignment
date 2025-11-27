'''Write a Python program that takes a string as input and returns a new string where every alternate word is reversed while keeping the order of the words intact.
Example Input/Output:
Input: "Python is an amazing programming language"
Output: "Python si an gnizama programming egaugnal” 
'''

text = input("Enter a sentence: ")

words = text.split()
result = ""

for i in range(len(words)):
    if i % 2 == 1:        
        result += words[i][::-1] + " "
    else:
        result += words[i] + " "

print("Output:", result.strip())




