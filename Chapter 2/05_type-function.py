# Chapter 2: Variables and Data Types
# Practice on identifying types and typecasting

a = 12
print(type(a))  # <class 'int'>

b = "13"
print(type(b))  # <class 'str'>

c = "True"      # Wrapped in quotes, so it's a string!
print(type(c))  # <class 'str'>

d = False       # No quotes, so it's a boolean [cite: 108]
print(type(d))  # <class 'bool'>

e = 67.3434
print(type(e))  # <class 'float'>

# --- Typecasting Section ---
# Converting one data type into another 

# String to Float conversion
b_string = "43"
c_float = float(b_string) 
print(type(c_float))  # <class 'float'>

# Boolean to Integer conversion
# True becomes 1, False becomes 0
d_bool = True
f_int = int(d_bool)
print(f"Value: {f_int}, Type: {type(f_int)}") # <class 'int'>

# None to String conversion
g_none = None
h_str = str(g_none)
print(type(h_str))    # <class 'str'>