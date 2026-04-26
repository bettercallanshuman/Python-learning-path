# PS 3 : Install an external module and use it to perform an operation of your interest.  

import pytest

def function_to_test(x):
    return x * 2

# This is the "active" part that actually runs
print(f"Testing with 2: {function_to_test(2)}") 
print(f"Testing with -1: {function_to_test(-1)}")