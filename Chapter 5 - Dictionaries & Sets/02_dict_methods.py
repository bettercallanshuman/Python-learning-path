marks =  {
    "Anshuman" : 100,
    "Paribrita" : 69,
    "Human" : 0
}

#RHS part is known as "keys" and the LHS is known as "values"

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Anshuman" : 99, "Renuka" : 78})
print(marks)

### INTERVIEW QUESTION ( TRICKY )
# Whats's the diffrence between using "()" and "[]", if these functions returns the same value.
print(marks.get("Anshuman"))
print(marks["Anshuman"])
#Output : 100
#Output : 100

#Answer : if we change the keys, the .get method will return "None", whereas the other won't return it'll show "Key Error"
print(marks.get("Anshuman1"))
print(marks["Anshuman1"])

#Check out other Dictionaries ".pop", ".pop item"