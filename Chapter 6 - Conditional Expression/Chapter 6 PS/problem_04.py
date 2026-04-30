#Write a program to find whether a given username contains less than 10 characters or not

username = input("enter username : ")

if(len(username)<10):
    print("valid username")
else:
    print("username must be in 10 characters.")