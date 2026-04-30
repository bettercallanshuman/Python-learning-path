#Write a program to input eight numbers from the user and display all 
# the unique numbers (once). 

a1 = int(input("Enter number 1 : "))
a2 = int(input("Enter number 2 : "))
a3 = int(input("Enter number 3 : "))
a4 = int(input("Enter number 4 : "))
a5 = int(input("Enter number 5 : "))
a6 = int(input("Enter number 6 : "))
a7 = int(input("Enter number 7 : "))
a8 = int(input("Enter number 8 : "))


input_set1 = {a1,a2,a3,a4}
input_set2 = {a5,a6,a7,a8}
input_union = (input_set1.union(input_set2)) # to ensure that only the unique numbers 
#get printed rather that iterating the same nummber.
print(input_union)