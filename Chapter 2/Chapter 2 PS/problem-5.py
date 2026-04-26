# PS 5: Write a python program to find an average of two numbers entered by the user.

# Taking inputs and converting them to integers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculating average: Sum divided by total count
# Parentheses are used to ensure addition happens before division
avg = (a + b) / 2

print(f"The average of {a} and {b} is: {avg}")