user_input = input("Enter your text : ")
character_count = len(user_input)
#replace = (user_input.replace(" ",""))
space_count = (user_input.count(" "))
b = (space_count)
word_count = (space_count+1) 

print("Entered text's character count : ", character_count)
print("Entered text's word count : ", word_count)

user_input_2 = input("Enter the word you want to find : ")
find_user_input_2 = user_input.find(user_input_2)
duplicate_word = user_input_2.count()

print("Entered text's duplicate found count : ", duplicate_word)
print("Entered text's word address is : ", find_user_input_2)
