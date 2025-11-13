'''Write a Python program that takes a string from the user and counts 
the number of vowels and consonants in it.Ignore spaces and special characters.
'''

user = input("Enter a string: ")
isVowels = 0
isConsonants = 0
for char in user:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'): #making sure the charaters are letters A-Z or a-z
  
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            isVowels += 1
        else:
            isConsonants += 1
print(f"Number of vowels: {isVowels}")
print(f"Number of consonants: {isConsonants}")