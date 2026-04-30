#Write a program which finds out whether a given name is present in a list or not.

enter_name = input("Enter the name : ")
name_list = ["Anshuman", "Michael", "Alex"]

if(enter_name in name_list):
    print("Name is in list")

else:
    print("Name is not in the list, \nPlease try again after sometime.")