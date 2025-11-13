'''Write a Python program that:
 Takes a password as input and checks its strength based on the following conditions:
Weak: If the password is less than 6 characters or only contains letters.
Moderate: If the password has at least 6 characters and contains both letters and numbers.
Strong: If the password has at least 8 characters, contains letters, numbers, and special characters (@, #, $, %, &).
'''

password = input("Enter your password: ")
count = 0
isNum = False
isSpecialChar = False
isLetter = False

for char in password:
    count += 1
    if char >= '0' and char <= '9':
        isNum = True
    elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        isLetter = True
    elif char in ['@', '#', '$', '%', '&']:
        isSpecialChar = True
    
    if isLetter and  not (isNum) and not (isSpecialChar) and count < 6:
        strength = "Weak"
    elif isLetter and isNum and not (isSpecialChar) and count >= 6:
        strength = "Moderate"
    elif isLetter and isNum and isSpecialChar and count >= 8:
        strength = "Strong"
    else:
        strength = "Weak"
print(f"Your password's strength is: {strength}")