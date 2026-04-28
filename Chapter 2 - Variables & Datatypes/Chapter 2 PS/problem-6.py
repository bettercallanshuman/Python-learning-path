# PS 6: Write a python program to calculate the square of a number entered by the user.

# Taking the number as input and converting to integer
a = int(input("Enter a number to find its square: "))

# Method 1: Basic Multiplication
square = a * a

# Method 2 (The Pro Way): Using the Exponentiation Operator (**)
# square = a ** 2

print(f"The square of {a} is: {square}")