s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2)) # it prints the output of both the sets in one curly braces.
#But if both sets have 1 number in common then it will return with anyone of the value
#Output : {1, 6, 7, 8, 78} whereas 78 occured in  both the sets but it only returned 78 once.

print(s1.intersection(s2)) # it prints the intersection of the sets
# Basically the common numbers in both the sets.

print({1,78}.issubset(s2)) #sub set ensures whether the values are there in the given set or not
#Always returns boolean.
print({2, 67}.issubset(s1)) # Output : False, because the values don't fall under the given subset.

print(s1.difference(s2))