#Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write to post : ")
find = "Anshuman"

if(find.lower() in post.lower()): # this .lower() is great, it firstly turns the find str and post str in lower case and do its work, in this case searches
    print("This post is talking about Anshuman")
else:
    print("This post is not talking about Anshuman")

#Output :

#Write to post : aNshumaN is a good boi
#This post is talking about Anshuman