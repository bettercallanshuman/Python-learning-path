user_input = input("Enter your text : ")
character_count = len(user_input)
space_count = (user_input.count(" "))
b = (space_count)
word_count = (space_count+1) # there's a bug in this logic, if user enters nothing it will still return 1. Can be fixed by "if-else condition" in chapter 4. till then let it be.

print("Entered text's character count : ", character_count)
print("Entered text's word count : ", word_count)

user_input_2 = input("Enter the repeated word : ")
find_user_input_2 = user_input.find(user_input_2)
duplicate_word = user_input.count(user_input_2)

print("Entered text's duplicate found count : ", duplicate_word)
print("Entered text's word address is : ", find_user_input_2)

user_input_3 = input("Enter the text you want to censor : ")
character_count_censor_word = len(user_input_3)
censor_word = user_input.replace(user_input_3, character_count_censor_word*"*")
print(censor_word)
