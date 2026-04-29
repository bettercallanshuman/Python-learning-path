#If the names of 2 friends are same; what will happen to the program in problem 6? 

d = {}

name = input("Enter friend's name : ")
lang = input("Enter your fav language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter your fav language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter your fav language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter your fav language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter your fav language : ")
d.update({name : lang})

print(d)

# Answer : The latest friend's language i.e. the value will update i.e. maps the early value and return the latest one.
# Output : 
# Enter friend's name : Anshuman
#Enter your fav language : Bengali
#Enter friend's name : Paribrita
#Enter your fav language : Bengali
#Enter friend's name : Mohan
#Enter your fav language : Punjabi
#Enter friend's name : Shinde
#Enter your fav language : Marathi
#Enter friend's name : Anshuman
#Enter your fav language : English
#{'Anshuman': 'English', 'Paribrita': 'Bengali', 'Mohan': 'Punjabi', 'Shinde': 'Marathi'}