list = ["India", "Russia", "European Union", "Pakistan", "America"]

list.append("China") # adds an element at the end of the list
print(list)

list.remove("Pakistan") # Removes an element from the list, directly.
print(list)

list.insert(2,"Brazil") # ( index, "str"), inserts the element in the list.
print(list)

list.clear() # It clears the whole string
print(list)

l1 = [88,34,6,12,9990,433,2234,12,0] 
l1.sort() # sorts the elements in ascending order in numbers and alphabetically in strings.
print(l1)

l1.reverse() # reverses the elements.
print(l1)

l1.pop(8) # pops out the element by entering the index of it in parenthesis.
print(l1)

# these two methods which are above and below this line cannot run simultaneously because it shares the same list.

#value = l1.pop(8) #it also returns the value which it popped out earlier.
#print(value)