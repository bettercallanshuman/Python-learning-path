# PS 2: Write a python program to find remainder when a number is divided by z.

# Taking input from the user and typecasting to integer
a = int(input("Enter the first number (Dividend): "))
z = int(input("Enter the second number (Divisor): "))

# The Modulus operator (%) calculates the remainder
remainder = a % z

print("The remainder when", a, "is divided by", z, "is:", remainder)