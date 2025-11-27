'''Write a Python program that takes a list of numbers and:
Print the numbers in the list but skip numbers that are divisible by 5.
Stops the loop if a number greater than 50 is encountered.
'''

n = int(input("Enter how many numbers you want in the list: "))
numbers = []  

for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    numbers.append(value)
    
print("\nProcessed Output:")
for num in numbers:
    if num > 50:
        print(f"Encountered number > 50 ({num}). Stopping the loop.")
        break
    if num % 5 == 0:
        continue
    print(num)
