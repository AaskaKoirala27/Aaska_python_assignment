'''Write a program in python which takes a list of words as input and store the frequency of each word in dictionary  
Input [“This”,”is”,”good”,”is”]
Output {“this”:1,”is”:2}
'''

words = input("Enter words separated by spaces: ").split()

frequency = {}

for word in words:
    w = word.lower()
    if w in frequency:
        frequency[w] += 1
    else:
        frequency[w] = 1

print("Word frequency:", frequency)



