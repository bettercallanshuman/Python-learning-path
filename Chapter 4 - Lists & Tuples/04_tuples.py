# Tuples are ordered immutable collection of elements used in python

a = (1, 3, "rohan", 4.098, "lila")
print(type(a))

a = () # Empty tuple.
print(a)

a = (1)
print(type(a)) # this type is showing "int" because, python undestood it's an int.

# If assign a single value to a variable to make it tuple, we must use a "," comma after that.

a = (1,)
print(type(a))