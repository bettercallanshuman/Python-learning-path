#Write a program to calculate the grade of a student from his marks from the following scheme:

marks_input = int(input("Enter the marks : "))

#g1 = (90 to 100)
#g2 = (80 to 90)
#g3 = (70 to 80)
#g4 = (60 to 70)
#g5 = (50 to 60)
#g6 = <50

if(marks_input<=100 and marks_input>=90):
    grade = "O"
elif(marks_input<90 and marks_input>=80):
    grade = "A"
elif(marks_input<80 and marks_input>=70):
    grade = "B"
elif(marks_input<70 and marks_input>=60):
    grade = "C"
elif(marks_input<60 and marks_input>=50):
    grade = "D"
elif(marks_input<50 and marks_input>=0):
    grade = "F"

print("Your Grade is :", grade)

