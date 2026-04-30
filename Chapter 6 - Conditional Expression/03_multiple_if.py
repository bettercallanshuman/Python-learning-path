a = int(input("Enter your age : "))

#if statement 1.
if(a%2 == 0):
    print("Entered age is even.")

#if statement 1 ended.

#if statemen 2.
if(a>=18):
    print("You are above the age.") #the space before print is known as "Indentation"
    print("Good to go.")

elif(a<0):
    print("You are entering a invalid negetive age.")

elif(a==0):
    print("You are entering an invalid age.")

else:
    print("Sorry, you are under age.")
#if statement 2 ended.

print("--End of the program--")