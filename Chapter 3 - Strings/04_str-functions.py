myself = "Anshuman"

# CORRECTED: .count() returns the TOTAL NUMBER of times a character appears
count = myself.count("u") 
print(count) # Output: 1

# .len() gives the total count of characters (starts from 1, not 0)
print(len(myself)) # Output: 8

# Returns True/False if the string ends with the specified suffix
print(myself.endswith("man")) 

# .replace(old, new) creates a NEW string with the words swapped
a = "Partha is a slut"
print(a.replace("slut","brat")) 

# Only the very first letter of the whole string becomes capital
b = "anshuman"
print(b.capitalize()) 

# Capitalizes the first letter of EVERY word (Great for names/titles!)
c = "amazon inc."
print(c.title()) # Output: Amazon Inc.

# Returns the INDEX (address) of the first time it finds the character
d = "abcdefgh"
print(d.find("d")) # Output: 3

