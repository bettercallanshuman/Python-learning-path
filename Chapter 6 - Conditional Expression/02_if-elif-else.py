a = int(input("Enter your age : "))

#if-elif-else ladder.

if(a>=18):
    print("You are above the age.") #the space before print is known as "Indentation"
    print("Good to go.")

elif(a<0):
    print("You are entering a invalid negetive age.")

elif(a==0):
    print("You are entering an invalid age.")

else:
    print("Sorry, you are under age.")