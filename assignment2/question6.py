'''Write a function largest_word(sentence) that takes a sentence as input and returns the longest word in the sentence. If there are multiple words of the same length, return the first one that appears.
Hint: Split the sentence into words using .split(), then compare the lengths of the words to find the longest one.
largest_word("Python programming is awesome") 
# Output: "programming"
'''

def largest_word(sentence):
    words = sentence.split() 
    longest = words[0]       

    for word in words:
        if len(word) > len(longest):
            longest = word  

    return longest

user_sentence = input("Enter a sentence: ")

print("The longest word is:", largest_word(user_sentence))


