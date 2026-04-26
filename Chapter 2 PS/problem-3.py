#Check the type of variable assigned using input () function.


#1st approch: Using type() function to check the data type of the variable assigned using input() function.
# The input() function always returns a string by default, even if you enter a number.
user_input = input("Enter the variable: ")
print("You entered :", user_input)

# To check the type of the variable, we can use the type() function.
print("I detected the data type as : ", type(user_input))

#2nd approach 

user_input = input("Enter anythinggggg: ")

if user_input == "True" or user_input == "False":
    # If the user literally typed True or False
    value = (user_input == "True") # This turns the string into an actual Boolean
    print(f"I detected a Boolean: {type(value)}")

elif "." in user_input:
    # If it has a dot, try to make it a float
    try:
        value = float(user_input)
        print(f"I detected a Float: {type(value)}")
    except ValueError:
        print(f"'{user_input}' is a String (contains a dot but isn't a number)")

elif user_input.isdigit():
    # If it's all numbers, it's an integer
    value = int(user_input)
    print(f"I detected an Integer: {type(value)}")

else:
    # Everything else is just a string
    print(f"This is a String: {type(user_input)}")