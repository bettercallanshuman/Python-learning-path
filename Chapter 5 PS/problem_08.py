#If languages of two friends are same; what will happen to the program in problem 6? 

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

# Answer : No changes ; The values will remain same, because dictionaries have identifiers which indentifies the same keys with different values.


# Output : 

#Enter friend's name : Anju
#Enter your fav language : py  
#Enter friend's name : Bill
#Enter your fav language : js
#Enter friend's name : Comma
#Enter your fav language : ruby
#Enter friend's name : Yuvi
#Enter your fav language : py
#Enter friend's name : Uri
#Enter your fav language : c
#{'Anju': 'py', 'Bill': 'js', 'Comma': 'ruby', 'Yuvi': 'py', 'Uri': 'c'}