#Write a program to create a dictionary of Hindi words with values as their 
# English translation. Provide user with an option to look it up!


translation_dictionary = { 
    "shant" : "calm",
    "subah" : "morning",
    "saab changa si" : "everything good",
    "darwaza" : "door"
}

user_input = input("Enter the word to look up : ")
print(translation_dictionary[user_input])