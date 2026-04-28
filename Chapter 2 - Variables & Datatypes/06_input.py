# Chapter 2: The input() Function and Typecasting
# Understanding why "12" + "24" = "1224"

# --- PART 1: The "Tricky Concatenation" ---
# input() always returns a String by default
a = input("Enter the first number: ")
b = input("Enter the second number: ")

print("First number:", a)
print("Second number:", b)

# Because a and b are strings, '+' joins them together (Concatenation)
# It's like adding "Harry" + "Potter" = "HarryPotter"
print("Sum (as strings):", a + b) 

# --- PART 2: The Fix (Hacker's Output) ---
# We wrap input() inside int() to convert the data type immediately
a = int(input("Enter the first number: ")) # String to Integer conversion
b = int(input("Enter the second number: ")) # String to Integer conversion

print("First number is:", a)
print("Second number is:", b)

# Now that a and b are Integers, '+' performs actual Math (Addition)
print("The sum of both the nos is:", a + b)