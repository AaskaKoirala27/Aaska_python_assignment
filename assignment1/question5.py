'''Write a Python program to display the frequency of each character in a given string.
Ignore case differences. 
'''

user = input("Enter a string: ")
arr = []
freq = []
ifLower = user.lower()
for char in user.lower():
    if char not in arr:
        arr.append(char)
        freq.append(1)
    else:
        index = arr.index(char)
        freq[index] += 1
for i in range(len(arr)):
    print(f"{arr[i]} : {freq[i]}")

#append = list ma add garxa
#lower() = lowercase ma convert garxa