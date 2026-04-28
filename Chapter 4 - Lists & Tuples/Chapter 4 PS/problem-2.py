#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m1 = input("Enter marks of Shiny : ")
marks.append(m1)
m2 = input("Enter marks of Rudvik : ")
marks.append(m2)
m3 = input("Enter marks of Sunita : ")
marks.append(m3)
m4 = input("Enter marks of Tanvir : ")
marks.append(m4)
m5 = input("Enter marks of Yash : ")
marks.append(m5)
m6 = input("Enter marks of Omar : ")
marks.append(m6)

marks.sort()
print(marks)