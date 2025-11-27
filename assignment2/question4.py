'''Create a dictionary called books where the keys are book titles (strings) and the values are the number of copies available for each book (integers). 
For example:
books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,  # You can add more books
}
Write a Python program that does the following:
Prompts the user to enter the name of the book they want.
Prompts the user to enter the number of copies they want to buy.
Checks if the book exists in the books dictionary.
Prints the following messages based on availability:
- "Available": If the book is in the dictionary and there are enough copies to fulfill the user's request.
- "Partially Available": If the book is in the dictionary, but there are fewer copies than the user wants.
- "Unavailable": If the book is not in the dictionary.
Important: Your program should handle the case where the user might enter something that is not a valid 
number of copies (e.g., letters, a blank input). Provide a clear message to the user if this happens and 
ask for number of copies again if the input by user is not an integer type
'''

books = {
    'Harry Potter': 5,
    'The Alchemist': 8,
    'The Oval Portrait': 6,
    'Godan': 4,
    'Panchatantra': 6,
    'Muna Madan': 10,
    'Karnali Blues': 3
}

     
print("Available books:")
for title in books:
    print("-", title)

book_name_input = input("\nEnter the name of the book you want: ")

book_name_lower = book_name_input.lower()

book_name = None
for title in books:
    if title.lower() == book_name_lower:
        book_name = title
        break

while True:
    copies_input = input("Enter the number of copies you want to buy: ")
    if copies_input.isdigit():  
        requested_copies = int(copies_input)
        break
    else:
        print("Invalid input! Please enter a valid number.")

if book_name:
    available_copies = books[book_name]
    if requested_copies <= available_copies:
        print("Available")
    else:
        print("Partially Available")
else:
    print("Unavailable")
