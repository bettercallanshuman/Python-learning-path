# Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter the number 1 : "))
a2 = int(input("Enter the number 2 : "))
a3 = int(input("Enter the number 3 : "))
a4 = int(input("Enter the number 4 : "))

if(a1>=a2 and a1>=a3 and a1>=a4):
    print("Number 1 is the greatest among all numbers.")

elif(a2>=a1 and a2>=a3 and a2>=a4):
    print("Number 2 is the greatest among all the numbers.")

elif(a3>= a1 and a3>=a2 and a3>=a4):
    print("Number 3 is the greatest among all the numbers.")

else:
    print("Number 4 is the greatest among all the numbers")

print("--End of the Program--")
