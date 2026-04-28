#Write a program to fill in a letter template given below with name and date.

'''letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

'''name = ("Anshuman Das")
date = ("27 April 2026")
print(f"Dear {name}, \nYou are selected as an SDE @GOOGLE.\nCongratulations.\n{date}")'''


#Approach - 2


letter ='''Dear <|Name|>,
           You are selected!
           <|Date|>'''


print(letter.replace("<|Name|>","Anshuman").replace("<|Date|>","27 April 2026"))