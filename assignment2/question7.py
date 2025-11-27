'''Write a function to_title_case(sentence) that takes a sentence as input and returns the sentence in title case, where the first letter of each word is capitalized.

to_title_case("hello world from python") 
# Output: "Hello World From Python"
'''

def to_title_case(sentence):
    words = sentence.split()
    title_sentence = "" 

    for word in words:
        if word:  
            title_sentence += word[0].upper() + word[1:].lower() + " "
    
    return title_sentence.strip()  

input_sentence = input("Enter a sentence: ")
print("Title case sentence:", to_title_case(input_sentence))
